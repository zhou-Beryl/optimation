import numpy as np
from fractions import Fraction as f

# 求解问题的目标为最小值；
# 且定义的变量c时直接用-cB，-cT写入，变量c的个数要和约束中变量的个数保持一致，没有就写为0，比如【-1，-2，0，0】
# 对于等式约束、不等式约束均为二维numpy数组，就算该类型只有一个约束，也要用二维数组

class Simplex(object):
    def __init__(self,c,A_ge,A_le,A_eq,b_ge,b_eq,b_le):
        ''' 初始化，获得问题各项参数 '''
        self.c = c  # 系数矩阵
        self.A_eq = A_eq  # 约束矩阵
        self.b_eq = b_eq # 约束边界
        self.A_ge = A_ge
        self.A_le = A_le
        self.b_ge = b_ge
        self.b_le = b_le
        self.neq = len(A_le)+len(A_eq)+len(A_ge)  # 约束的个数
        self.neq2 = len(c)+len(A_ge)+len(A_le) # 原本变量的个数
        self.T = []  # 单纯形表
        self.sign = np.full(self.neq, np.nan)  # 基变量序号，行索引--索引，值--基变量
        self.art = []  # 人工变量的序号--行索引
        self.F = 1  # 迭代情况，1继续迭代

    def standed_form(self):
        num = len(self.c)
        num1 = len(self.A_eq)
        num2 = len(self.A_ge)
        num3 = len(self.A_le)
        A = np.zeros([num1 + num2 + num3, num + num2 + num3], dtype=float)
        b = np.zeros([num1 + num2 + num3], dtype=float)
        if num1 > 0:
            A[:num1, :num] = self.A_eq
            b[:num1] = self.b_eq
        if num2 > 0:
            A[num1:num1 + num2, :num] = self.A_ge
            np.fill_diagonal(A[num1:num1 + num2, num:num + num2], -1)
            b[num1:num1 + num2] = self.b_ge
        if num3 > 0:
            A[num1 + num2:num1 + num2 + num3, :num] = self.A_le
            np.fill_diagonal(A[num1 + num2:num1 + num2 + num3, num + num2:num + num2 + num3], 1)
            b[num1 + num2:num1 + num2 + num3] = self.b_le
        self.A_eq = A
        self.b_eq = b

    def Initial_value(self):
        '''检索基变量，添加人工变量，生成单纯形表'''
        self.standed_form()
        # 查找 已有的基变量
        unit = []
        for col_idx in range(self.neq2):
            col = self.A_eq[:, col_idx]
            if np.count_nonzero(col) == 1 and np.sum(col) == 1:
                unit.append([np.argmax(col), col_idx])
        for i in unit:
            self.sign[i[0]] = i[1]
        # 添加 人工变量
        self.art = np.where(np.isnan(self.sign))[0]
        art_var0 = self.neq2
        for i in self.art:
            self.sign[i] = art_var0
            art_var0 += 1
        # 生成 单纯形表
        if np.size(self.art) == 0:
            # 不需要 添加人工变量
            self.T = np.zeros([self.neq + 1, self.neq2 + 1], dtype=float)
            self.T[1:, :-1] = self.A_eq
            self.T[0, :np.size(self.c)] = self.c
            self.T[1:, -1] = self.b_eq
        else:
            # 需要 添加人工变量
            self.T = np.zeros([self.neq + 1, art_var0 + 1], dtype=float)
            self.T[1:, :self.neq2] = self.A_eq
            for i in self.art:
                j = int(self.sign[i])
                self.T[i + 1, j] = 1
                self.T[0, j] = -1
            self.T[1:, -1] = self.b_eq

    def typical_form(self):
        '''化为典式，修改Z或G'''
        for index, value in enumerate(self.sign):
            factor = self.T[0][int(value)]
            self.T[0, :] -= factor * self.T[index + 1, :]

    def solve(self):
        '''解的判断'''
        flag = True
        while flag:
            # 检验数小于等于0，就得到最优解
            if max(list(self.T[0, :-1])) <= 0:
                flag = False
            else:
                self.F = self.calculate()
                if self.F == 0:
                    print('该问题无界')
                    break

    def calculate(self):
        '''迭代计算'''
        come = np.argmax(self.T[0, :-1])
        D = []
        for i in range(self.neq):
            if self.T[i + 1, come] <= 0:
                # 该列等于0 小于0 行对应的变量不能出基，故都设为-inf
                D.append(float('-inf'))
            else:
                D.append(self.T[i + 1, -1] / self.T[i + 1, come])

        if np.max(D) <= 0:
            return 0
        else:
            leave = D.index(min([x for x in D if x >= 0]))
            self.sign[leave] = come

            temp1 = np.where(self.art == leave)[0]
            if len(temp1) != 0:
                for k in temp1:
                    self.art[k] = -999  # 表示人工变量已经离基

            temp2 = self.T[leave + 1][come]
            # print(temp2)
            # 换基迭代
            self.T[leave + 1] /= temp2
            for i in [x for x in range(self.neq + 1) if x != leave + 1]:
                self.T[i, :] -= self.T[leave + 1, :] * self.T[i][come]
            return 1

    def change(self):
        '''去除人工变量，全部设置为0'''
        self.T[:, -np.size(self.art) - 1:-1] = 0
        self.T[0, 0:np.size(self.c)] = self.c
        self.typical_form()

    def control(self):
        '''控制求解流程'''
        self.Initial_value()
        self.typical_form()
        if len(self.art) == 0:
            print('不需要添加人工变量，直接利用单纯形法:')
            self.solve()
        else:
            print('利用两阶段法求解:')
            self.solve()
            if self.T[0][-1] > 0:
                print('原问题无解')
                return 0
            else:
                self.change()
                self.solve()
        self.formatting()
        return 1

    def formatting(self):
        if self.F == 1:
            print('z', end='\t')
            for j in self.T[0, :]:
                str_f = str(f(str(j)).limit_denominator())
                print(f"{str_f:5}", end='\t')
            print()
            for i in range(self.neq):
                print('x_{}'.format(i + 1), end='\t')
                for j in self.T[i + 1, :]:
                    str_f = str(f(str(j)).limit_denominator())
                    print(f"{str_f:5}", end='\t')
                print()
            print('基变量取值:', end='  ')
            for i in range(self.neq):
                if i not in self.sign:
                    print(f'x{i + 1}', '= 0', end=' ')
                else:
                    j = np.where(self.sign == i)[0][0]
                    print(f'x{i + 1}', '=', f(str(self.T[j + 1][-1])).limit_denominator(), end=' ')
            print('\n最优解:',str(f(str(self.T[0][-1])).limit_denominator()))

class Dual_Simplex(Simplex):
    def __init__(self,c,A_ge,A_le,A_eq,b_ge,b_eq,b_le):
        '''初始化，获得参数'''
        super().__init__(c,A_ge,A_le,A_eq,b_ge,b_eq,b_le)
        self.N = 1 #判断是否可以利用对偶单纯形表求解

    def Initial_value(self):
        '''检测是否可以生成对偶单纯形表，可以则生成'''
        self.standed_form()

        unit1 = []
        unit2 = []
        for col_idx in range(self.neq2):
            col = self.A_eq[:,col_idx]
            if np.count_nonzero(col) == 1 and np.sum(col) == 1:
                unit1.append([np.argmax(col),col_idx])
            if np.count_nonzero(col) == 1 and np.sum(col) == -1:
                unit2.append([np.argmin(col),col_idx])
        if (len(unit1) + len(unit2) < self.neq):
            print('无法直接利用对偶单纯形法求解')
            return 0
        else:
            #生成单纯形表
            self.T = np.zeros([self.neq+1,self.neq2+1],dtype=float)
            self.T[1:,:-1] = self.A_eq
            self.T[0,:np.size(self.c)] = self.c
            self.T[1:,-1] = self.b_eq
            for i in unit1:
                self.sign[i[0]] = i[1]
            for i in unit2:
                self.sign[i[0]] = i[1]
                self.T[i[0]+1,:] = -1 * self.T[i[0]+1,:]
        self.typical_form()
        if np.max(self.T[0,:]) > 0:
            print('无法利用对偶单纯形法求解')
            return 0
        return 1

    def solve(self):
        '''解的判断，原问题无解或者达到最优解(输出)'''
        self.N = self.Initial_value()
        if self.N == 1:
            flag = True
            while flag:
                if min(list(self.T[1:,-1])) >= 0:
                    self.formatting()
                    flag = False
                else:
                    self.F = self.calculate()
                    if self.F == 0:
                        print('对偶问题无界，原问题无解')
                        break

    def calculate(self):
        '''迭代计算'''
        leave = np.argmin(self.T[1:,-1])
        D = []
        for i in range(self.neq2):
            if self.T[leave+1,i] >= 0:
                # 负值全部记为负无穷
                D.append(float('-inf'))
            else:
                D.append(self.T[0,i]/self.T[leave+1,i])
        if np.max(D) <= 0:
            return 0
        else:
            come = D.index(min([x for x in D if x>= 0]))
            self.sign[leave] = come
            temp = self.T[leave+1, come]
            self.T[leave+1,:] /= temp
            #换基迭代
            for i in [x for x in range(self.neq+1) if x != leave+1]:
                self.T[i,:] -= self.T[leave+1,:] * self.T[i][come]
            return 1

if __name__ == '__main__':
    problems = {}
    #16题（1）
    c1 = np.array([2, 1, -1])
    A_ge1 = np.array([])
    A_le1 = np.array([[3, 1, 1],[1,-1,2],[1,1,-1]])
    A_eq1 = np.array([])
    b_ge1 = np.array([])
    b_le1 = np.array([60,10,20])
    b_eq1 = np.array([])
    problems[1] = [c1,A_ge1,A_le1,A_eq1,b_ge1,b_eq1,b_le1]

    #16题（2）
    c2 = np.array([-3, -1, -1,-1])
    A_ge2 = np.array([])
    A_le2 = np.array([])
    A_eq2 = np.array([[-2,2,1,0],[3,1,0,1]])
    b_ge2 = np.array([])
    b_le2 = np.array([])
    b_eq2 = np.array([4,6])
    problems[2] = [c2, A_ge2, A_le2, A_eq2, b_ge2, b_eq2, b_le2]

    #23题（1）
    c3 = np.array([-2, -3, -4])
    A_ge3 = np.array([[1, 2, 1], [2, -1, 3]])
    A_le3 = np.array([])
    A_eq3 = np.array([])
    b_ge3 = np.array([3, 4])
    b_le3 = np.array([])
    b_eq3 = np.array([])
    problems[3] = [c3, A_ge3, A_le3, A_eq3, b_ge3, b_eq3, b_le3]

    #23题（2）
    c4 = np.array([-3, -2, -1])
    A_ge4 = np.array([[1, 0, -1], [0, 1, -1]])
    A_le4 = np.array([[1, 1, 1]])
    A_eq4 = np.array([])
    b_ge4 = np.array([4, 3])
    b_le4 = np.array([6])
    b_eq4 = np.array([])
    problems[4] = [c4, A_ge4, A_le4, A_eq4, b_ge4, b_eq4, b_le4]

    S = {}
    M = {}
    print('*' * 20, '利用两阶段法求解', '*' * 20)
    print('\n')
    for i in [1,2,3,4]:
        S[i] = Simplex(problems[i][0],problems[i][1],problems[i][2]
                       ,problems[i][3],problems[i][4],problems[i][5],problems[i][6])
        S[i].control()
        print('\n')
    print('*'*20,'利用对偶单纯形法求解','*'*20)
    for i in [1,2,3,4]:
        M[i] = Dual_Simplex(problems[i][0],problems[i][1],problems[i][2]
                       ,problems[i][3],problems[i][4],problems[i][5],problems[i][6])
        M[i].solve()
        print('\n')
