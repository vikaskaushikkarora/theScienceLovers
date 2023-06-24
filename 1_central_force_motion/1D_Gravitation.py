# 1 D Gravitational Problem #

import numpy as np
import matplotlib.pyplot as plt

# initial conditions 
y0=1
z0=0
K=1   ## strength of field

x = np.arange(0,1,0.01)
y = np.zeros(len(x))
z = np.zeros(len(x))

def f(x,y,z) : 
	A=z
	return A

def g(x,y,z) :
	B=-K/(y**2)
	return B

def odeEuler(x,f,g,y0,z0):
    y[0] = y0
    z[0]= z0
    for n in range(0,len(x)-1):
        y[n+1] = y[n] + f(x[n],y[n],z[n])*(x[n+1] -x[n])
        z[n+1]= z[n] + g(x[n],y[n],z[n])*(x[n+1]-x[n])
    return y
    return z

#Solutions 
p = odeEuler(x,f,g,y0,z0)
plt.plot(x,y,'k-')
plt.plot(x,-z,'r-')
plt.xlabel('time')
plt.legend(['distance from centre','Speed of the object'])
plt.title('Object under Gravitation in 1D')
plt.grid()
plt.show()
