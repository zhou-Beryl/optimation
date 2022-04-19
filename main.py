# --------------------------------两阶段法纯形法的实现--------------------------
import numpy as np
# --------------------定义LP方程以及相应的运算函数-----------------------
class Simplex(object):
    def __init__(self, c, a_ub, a_eq, b_ub, b_eq):
        self.c = c
        self.a_ub = a_ub
        self.b_ub = b_ub
        self.a_eq = a_eq
        self.b_eq = b_eq
        self.n_x = 0          #变量的个数
        self.meq = 0          #等式的个数
        self.mub = 0          #不等式的个数
        self.m = 0            #约束总个数
        self.dt = []          #创建单纯性表
        self.sign = []        #记录基变量的个数
        self.f = 1            #判断迭代是否进行

    #单纯形表对应矩阵创建
    def initial_value(self):
        self.n_x = len(self.c)
        #计算单纯形表的行数和列数
        if self.b_eq.any():
            self.meq = len(self.b_eq)
        if self.b_ub.any():
            self.mub = len(self.b_ub)
        self.m = self.mub + self.meq
        self.dt = np.zeros([self.m + 1, self.m + self.n_x + 1],dtype = 'float')
        #把各个数据填入座位
        if self.meq > 0:
            self.dt[1:self.meq+1 ,:self.n_x] = self.a_eq
            self.dt[1:self.meq+1, -1] = self.b_eq
        if self.mub > 0:
            self.dt[-self.mub:,:self.n_x] = self.a_ub
            self.dt[-self.mub:,-1] = self.b_ub
        #人工变量和松弛变量
        np.fill_diagonal(self.dt[1:, self.n_x:self.n_x+self.m],1)
        #矩阵第一行
        self.dt[0,self.n_x:self.n_x+self.m] = -1 * np.ones(self.meq)
        #第一阶段
        for i in range(0,self.meq):
            self.dt[0] +=self.dt[1+i]
        l = [i for i in range(self.n_x,self.n_x+self.m)]
        self.sign = list(l)

    #计算最有检验函数并调用换基迭代
    def solve(self):
        num = 0
        flag = True
        while flag:
            if max(list(self.dt[0][:-1])) <= 0:
                flag = False
            else:
                num += 1
                self.f = self.calculate()
            if self.f == 0:
                break

    #迭代函数
    def calculate(self):
        h = list(self.dt[0, :-1])
        j_num = h.index(max(h))
        dd = []
       # i = max(self.dt[1:][j_num])

        for i in range(1, self.m + 1):
            if self.dt[i][j_num] == 0:
                dd.append(float("inf"))
            else:
                dd.append(self.dt[i][-1]/self.dt[i][j_num])

        if max(dd) <= 0:
            print('该问题无界')
            return 0

        #确定旋转元
        i_num = dd.index(min([x for x in dd if x >= 0 ]))
        self.sign[i_num]=j_num
        t = self.dt[i_num + 1][j_num]

        #高斯消元法换基迭代
        self.dt[i_num + 1] /= t
        for i in [x for x in range(0,self.m+1) if x != (i_num + 1)]:
            self.dt[i] -= self.dt[i_num+1] * self.dt[i][j_num]
        return 1

    #消去人工变量,人工变量所在列全部变为0，替代第二阶段的c
    def change(self):
        self.dt[:,self.n_x:self.n_x + self.meq] = 0
        self.dt[0,0:self.n_x] = -self.c
        for i in range(0,self.m):
            self.dt[0] -= self.dt[i+1] * self.dt[0][int(self.sign[i])]

    #主函数用以选择求解方式
    def main(self):
        self.initial_value()
        if self.meq > 0:        #采用两阶段法
            #第一阶段求解
            print('phase 1')
            self.solve()
            #消去人工变量
            self.change()
            #第二阶段求解
            print('phase 2')
            self.solve()
        else:
            #直接进入第二阶段
            print("simple")
            #消去人工变量
            self.change()
            self.solve()

        if self.f == 1:
            print("Optimal solution")
            j=1
            for i in range(0,self.n_x):
                if i+1 not in self.sign:
                    print("x"+str(i+1)+"=0")
                else:
                    print("x"+str(i+1)+"=",self.dt[j][-1])
                    j+=1
            print("Best Value:\n",self.dt[0][-1])
        else:
            print("出现无界解")

if __name__ == '__main__':
    # 主体函数预算过程：
    c = np.array([-2,3,0,0])
    # 不等式约束<=
    a_ub = np.array([])
    b_ub = np.array([])
    # 等式约束
    a_eq = np.array([[1,-1,1,0],[-3,1,0,1]])
    b_eq = np.array([2,4])
    Problem=Simplex(c, a_ub, a_eq,b_ub, b_eq)
    Problem.main()


