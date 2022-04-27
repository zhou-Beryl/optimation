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
		c=b
		b=a+b
		a=c
		f_list.append(b)
	#f_list.pop()
	return f_list

# 进行斐波那契搜索
def f_search(a,b,f_list):
	n = len(f_list)-1
	if n< 2:
		return "精度过低，无法进行搜索"
	x1 = a + (f_list[n-2]/f_list[n])*(b-a)
	x2 = b - (f_list[n-2]/f_list[n])*(b-a)
	data=list()
	data2 = list()
	data2.append(float(f_list[n-2]/f_list[n]))
	data.append([a,b])
	while(n>2):
		if function(x1)<function(x2):
			plt.plot(x2,function(x2),'r*')
			data.append([a,x2])
			b = x2
			x2 = x1
			x1 = a + (f_list[n-2]/f_list[n])*(b-a)
			data2.append(float(f_list[n-2]/f_list[n]))
		elif function(x1)>function(x2):
			plt.plot(x1,function(x1),"b*")
			data.append([x1,b])
			a = x1
			x1 = x2
			x2 = b - (f_list[n-2]/f_list[n])*(b-a)
			data2.append(float(f_list[n-2]/f_list[n]))
		else:
			a = x1
			b = x2
			x1 = a + (f_list[n-2]/f_list[n])*(b-a)
			x2 = b - (f_list[n-2]/f_list[n])*(b-a)
			data2.append(float(f_list[n-2]/f_list[n]))
			plt.plot(x1,function(x1),'r*',x2,function(x2),'r*')
			data.append([x1,x2])
		n -=1
	# 迭代点结束，判断解的区间
	x1 = a + 0.5 * (b - a)
	x2 = x1 + 0.1 * (b - a)
	if function(x1) > function(x2):
		plt.plot(x2, function(x2), 'g*')
		data.append([x1, b])
		data2.append(float((b-x1)/(b-a)))
		a = x1
	elif function(x1) < function(x2):
		b = x2
		data.append([a,x2])
		data2.append(float((x2-a)/(b-a)))
		plt.plot(x2,function(x2),"g*")
	else:
		plt.plot(x1,function(x1),"g*",x2,function(x2),"g*")
		data.append([x1,x2])
		data2.append(0)
	# 写入文件
	with open(r"13.text",mode='w',encoding='utf-8') as f:
		for i in range(0,len(data)):
			f.write("%d: \t" % (i+1))
			f.write("%d: \t" % data2[i])
			for j in range(0,2):
				f.write('f(%.3f)=%.7f\t' % (data[i][j],
					function(data[i][j])))
			f.write("\n")
		print("写入成功")
		return [a,b]
#if __name__ == "__name__":
init_str = "e^(-x)+x^2"
para = ("0 1 0.005").split()
para = [float(ele) for ele in para]
low,high,esp = para
str_fx = init_str.replace("^","**")
print(f_search(low,high,f_list(int(ceil((high-low)/esp)))))
print(f_list(int(ceil((high-low)/esp))))
draw(low,high,(high-low)/2000)
				
		
		
			
	
	
