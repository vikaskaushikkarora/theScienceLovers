## Definite Integration of a function ## 
import numpy as np
xi=-2
xf=2
h=0.0001
x=np.arange(xi,xf,h) ##Put the limits of intgration here ##

def f(x) :
	y= np.exp(-x*x)
	return y

def g(x,f) :
	A=(f(x+h)-f(x))/h
	return A

def int(x,f,g) :
	z=0
	for i in range(0,len(x)-1) :
		z=z+f(x[i])*(x[i+1]-x[i])+h*h*g(x[i],f)/2
	return z
print('integration of the above function:')
print(int(x,f,g))
