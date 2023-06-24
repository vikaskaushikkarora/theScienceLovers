# Runge Kutta 2 order #
import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
	A=np.sin(x)*(y+1)
	return A
h=0.01
x=np.arange (0,10,h)
y=np.zeros(len(x))
y[0]=0
for i in range (0,len(x)-1):
	y[i+1]=y[i]+h*f(x[i],y[i])
plt.plot(x,y)
z=np.zeros(len(x))
def f(x,z):
	B=np.sin(x)*(z+1)
	return B
z[0]=0
for i in range (0,len(x)-1):
# The average value of f(x,y) is taken at the original point and the point reached if we only apply euler method . And this idea can be extemded for more complex functions with more variables ....
	z[i+1]=z[i]+0.5*h*(f(x[i],z[i])+f(x[i]+h,z[i]+h*f(x[i],z[i])))
plt.plot(x,z,'r')
plt.legend(['Euler','Runge Kutta: More Accurate '] , loc =1)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('Euler VS Runge Kutta')
plt.show()
