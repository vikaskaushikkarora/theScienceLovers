## Indefinite Integration of a function ## 
import numpy as np
import matplotlib.pyplot as plt
xi=-10
xf= 10
N=5000
x=np.linspace(xi,xf,N) ##Put the limits of x axis here ##
def f(x) :
	y= np.exp(-x**2)
	return y
z=np.zeros(N)
def int(x,f) :
	z[0]=0
	for i in range(1,N-1) :
		z[i+1]=z[i]+f(x[i])*(x[i+1]-x[i])
A = int(x,f)
w =np.zeros(N) ## To make integrated function zero at x=0 by adding arbitrary constant 
w= z - z[N/2]
plt.plot(x,f(x))
plt.plot(x,w,'r')
plt.fill_between(x,f(x))
plt.title('Integration of a random function')
plt.legend(['function','integrated function'])
plt.grid()
plt.show()
