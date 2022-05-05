from math import *
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist


x1,x2,t = symbols('x1,x2,t')
def function():
	fx = pow(x1,2)+2*pow(x2,2)-2*x1*x2-2*x2
	return fx
	
def dif(data):
	f = function()
	grand1 = [diff(f,x1),diff(f,x2)]
	grand2 = [] 
	p = grand1[0].subs(x1,data[0]).subs(x2,data[1])
	q = grand1[1].subs(x1,data[0]).subs(x2,data[1])
	grand2.apppend([p,q])
	return grand2
	
def mo(grand):
	x_len = math.sqrt(pow(grand[0],2)+pow(grand[1],2))
	return x_len

def minn(f):
	t_min = diff(f)
	t_min = solve(t_diff)
	return t_min

def main(x0,theta):
	data = list()
	grand = dif(x0)
	data1 = [x0[0],x0[1],grand]
	data.append(data1)
	grand_len = mo(grand)
	while grand_len > theta:
		p = -np.array(grand)
		x = x0 + t*p
		t_f = function(x).subs(x1,x[0]).subs(x2,x[1])
		t_min = minn(t_f)
		
		x0 = x0 +t_min*p
		grand = dif(x0)
		grand_len = mo(grand)
		data1 = [x0[0],x0[1],grand]
		data.append(data1)	
	return data	
def file1(data):	
	with open(r"11.text",mode='w',encoding='utf-8') as f:
		for i in range(0,len(data)):
			f.write("%d: \t" % (i+1))
			for j in range(0,3):
				f.write('f(%.3f)=%.7f\t' % (data[i][j],
					function(data[i][j])))
			f.write("\n")
		print("写入成功")	
		
data = main([0,0],0.00001)
file(data)




