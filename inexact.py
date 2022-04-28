import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from math import *

def function(x):
	str_fx = "(x-1)*(x-3)"
	fx = str_fx.replace("x","%(x)f")
	return eval(fx % {"x":x})

def dift(x):
	m = sp.symbols('m')
	str_fx= (m-1)*(m-3)
	fxx = sp.diff(str_fx)
	return float(fxx.evalf(subs = {m:x}))

def plot1(a,b,user):
	plt.figure(1)
	x = [a+ele*0.05 for ele in range(0,int((b-a)/0.05))]
	y = [function(m) for m in x ]
	y2 =[user for m in x]
	plt.plot(x,y)
	plt.plot(x,y2)
	plt.show()
	return 0
	
def step(user):
	m1 = 0.4
	m2 = 0.6
	a = 0
	print(dift(0))
	b = (user - function(a))/(m1*dift(0))
	k = 0
	t = b
	print(t)
	flag = True
	
	if function(t) <= user:
		flag = False
		plt.plot(t, function(t), 'g*')
		
	while flag:
		k = k+1
		t = (b+a)/2
		if function(t) > function(0)+m1*dift(0)*t:
			b = t
		elif function(t) < function(0)+m1*dift(0)*t:
			a = t
		else:
			flag = Flase
			print(str(t))
			plt.plot(t, function(t), 'r*')
	print(k)
			
			

step(-0.5)
plot1(0,5,-0.5)
