# Derivative of a Function #
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,4,0.1)
def f(x) :
	y=x**2
	return y 
def g(x,f) :
	h=0.1
	z= (f(x+h)-f(x))/h
	return z
plt.plot(x,f(x),'ko-')
plt.plot(x,g(x,f),'r.-')
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Derivative of a function")
plt.legend(['Function','Derivative'])
plt.show()
