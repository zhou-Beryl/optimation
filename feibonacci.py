from math import *
import matplotlib.pyplot as plt
from pylab import * 

# 通用函数输入
def function(x):
	fx = str_fx.replace("x","%(x)f")
	return eval(fx % {"x":x})

# 绘图函数 
def draw(a,b,interp=0.05):
	x = [a + ele*interp for ele in range(0,int((b-a)/interp))]
	y = [function(ele) for ele in x]
	plt.figure(1)
	plt.plot(x,y)
	xlim(a,b)
	title(init_str,color="b")
	plt.show()
	return" 绘图完成！"
	
# 生成n个数的斐波那契数列,n为计算函数值的次数
def f_list(Fmax):
	a,b=0,1
	f_list =[a,b]
	while f_list[-1] < Fmax:
		b=a+b
		a=b
		f_list.append(b)
	#f_list.pop()
	return f_list

# 进行斐波那契搜索
def f_search(a,b,f_list):
	n = len(f_list)-1
	if n< 3:
		return "精度过低，无法进行搜索"
	x1 = a + (f_list[n-2]/f_list[n])*(b-a)
	x2 = b - (f_list[n-2]/f_list[n])*(b-a)
	m=n-1
	data=list()
	data.append([a,b])
	while(m>3):
		if function(x1)<function(x2):
			
			plt.plot(x2,function(x2),'r*')
			data.append([a,x2])
			b = x2
			x2 = x1
			x1 = a + (f_list[m-2]/f_list[m])*(b-a)
		elif function(x1)>function(x2):
			plt.plot(x1,function(x1),"r*")
			data.append([x1,b])
			a = x1
			x1 = x2
			x2 = b - (f_list[m-2]/f_list[m])*(b-a)
		else:
			a = x1
			b = x2
			x1 = a + (f_list[m-2]/f_list[m])*(b-a)
			x2 = b - (f_list[m-2]/f_list[m])*(b-a)
			plt.plot(x1,function(x1),'r*',x2,function(x2),'r*')
			data.append([x1,x2])
		m -=1
	# 迭代点结束，判断解的区间
	x1 = a + 0.5 * (b - a)
	x2 = x1 + 0.1 * (b - a)
	if function(x1) > function(x2):
		plt.plot(x2, function(x2), 'r*')
		data.append([x1, b])
		a = x1
	elif function(x1) < function(x2):
		b = x2
		data.append([a,x2])
		plt.plot(x2,function(x2),"g*")
	else:
		plt.plot(x1,function(x1),"g*",x2,function(x2),"g*")
		data.append([x1,x2])
	# 写入文件
	with open(r"12.text",mode='w',encoding='utf-8') as f:
		for i in range(0,len(data)):
			f.write("%d: \t" % (i+1))
			for j in range(0,2):
				f.write('f(%.3f)=%.7f\t' % (data[i][j],
					function(data[i][j])))
			f.write("\n")
		print("写入成功")
		return [a,b]
# if __name__ == "__name__":
init_str = input("请输入一个函数，默认变量为x：\n")
para = input("请输入区间a,b及最终精确值，含空格符").split()
para = [float(ele) for ele in para]
low,high,esp = para
str_fx = init_str.replace("^","**")
print(f_search(low,high,f_list(int(ceil((high-low)/esp)))))

draw(low,high,(high-low)/2000)
				
		
		
			
	
	
