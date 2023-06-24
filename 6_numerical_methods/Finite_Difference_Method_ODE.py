#Finite Difference Method
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,15,0.001)
h=x[2]-x[1]
#It basically has three ways : Forward diff. , backward diff. and central diff., however we use forward difference here to solve a general ode : y"(x)+f(x,y)*y'(x)+g(x,y)=0
#(dy/dx )[i]=(y[i+1]-y[i])/h
#(d/dx(dy/dx))[i]=(y[i+2]-2*y[i+1]+y[i])/h
def f(x,y):
	A=0
	return A
def g(x,y):
	B=y
	return B
y=np.zeros(len(x))
#Initial Conditions must be given in this form not as derivatives 
y[0]=0
y[1]=0.01
for i in range (0,len(x)-2):
	# We have converted ODE in Alzebraic Equation which can be iterated 
	y[i+2]=((h*f(x[i],y[i]))-1)*y[i]+(2-h*f(x[i],y[i]))*y[i+1]-h*h*g(x[i],y[i])
plt.plot(x,y)
plt.grid()
plt.show()
