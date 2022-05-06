import math
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist


x1,x2,t = symbols('x1,x2,t')
def function():
	fx = x1**2+x2**2+x2**2-x1*x2-x1*x2-x2-x2
	return fx
	
def dif(data):
	f = function()
	grand1 = [diff(f,x1),diff(f,x2)]
	p = grand1[0].subs(x1,data[0]).subs(x2,data[1])
	q = grand1[1].subs(x1,data[0]).subs(x2,data[1])
	grand2=[p,q]
	return grand2
	
def mo(grand):
	x_len = math.sqrt(pow(grand[0],2)+pow(grand[1],2))
	return x_len

def minn(f):
	t_diff = diff(f)
	t_min = solve(t_diff)
	return t_min

def main(x0,theta):
	data = list()
	grand = dif(x0)
	data1 = x0
	data.append(data1)
	grand_len = mo(grand)
	while grand_len > theta:
		p = -np.array(grand)
		x = x0 + t*p
		t_f = function().subs(x1,x[0]).subs(x2,x[1])
		t_min = minn(t_f)
		
		x0= x0 +t_min*p
		grand = dif(x0)
		grand_len = mo(grand)
		data1 = [x0[0],x0[1]]
		data.append(data1)	
	return data	
	
def draww(data):
	fig = plt.figure()
	ax = axisartist.Subplot(fig,111)
	fig.add_axes(ax)
	ax.axis["bottom"].set_axisline_style("-|>", size=1.5)
	ax.axis["left"].set_axisline_style("->", size=1.5)
	ax.axis["top"].set_visible(False)
	ax.axis["right"].set_visible(False)
	plt.title(r'$Gradient \ method - steepest \ descent \ method$')
	datax =[]
	datay =[]
	for i in range(0,len(data)):
		datax.append(data[i][0])
		datay.append(data[i][1])
	plt.plot(datax, datay, label=r'$f(x_1,x_2)=x_1^2+2 \cdot x_2^2-2 \cdot x_1 \cdot x_2-2 \cdot x_2$')
	plt.legend()
	#plt.scatter(1, 1, marker=(5, 1), c=5, s=1000)
	plt.grid()
	plt.xlabel(r'$x_1$', fontsize=20)
	plt.ylabel(r'$x_2$', fontsize=20)
	plt.show()
	
def file1(data):
	'''问题待排查'''
	with open(r"11.text",mode='w',encoding='utf-8') as f:
		for i in range(0,len(data)):
			f.write("%d: \t" % (i+1))
			for j in [0,1]:
				f.write("%3f: \t" % (data[i][j]))
			f.write("\n")
		print("写入成功")	
				
data = main([0,0],0.0001)
file1(data)
draww(data)
