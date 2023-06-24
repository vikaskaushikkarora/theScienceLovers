﻿# Euler Verlet 2 ODE 
#Helps in Energy Conservation 
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6*np.pi,0.01)
y = np.zeros(len(x))
z = np.zeros(len(x))

##define f(x,y,z) as in the differential equation   dy/dx= f(x,y,z)##

def f(x,y,z) : 
	A=z
	return A
	
# define g(x,y,z) as in the differential equation dz/dx = g(x,y,z)

def g(x,y,z) :
	B=-5*y
	return B

# Initial Conditions 	
y0=1
z0=0

def odeEuler(x,f,g,y0,z0):
    y[0] = y0
    z[0]= z0
    for n in range(0,len(x)-1):
        y[n+1] = y[n] + f(x[n],y[n],z[n])*(x[n+1] -x[n])
        z[n+1]= z[n] + g(x[n],y[n],z[n])*(x[n+1]-x[n])
    return y
    return z
P = odeEuler(x,f,g,y0,z0)
plt.plot(x,y,'k-')

def odeEulerVerlet(x,f,g,y0,z0):
    y[0] = y0
    z[0]= z0
    for n in range(0,len(x)-1):
    	z[n+1]= z[n] + g(x[n],y[n],z[n])*(x[n+1]-x[n])
        y[n+1] = y[n] + f(x[n],y[n],z[n+1])*(x[n+1] -x[n])
        # Calculate y[n] from z[n+1] instead of z[n]
    return y
    return z
P = odeEulerVerlet(x,f,g,y0,z0)
plt.plot(x,y,'r-')

plt.title("Solution of SHM equation")
plt.grid()
plt.legend(['Euler Method','Euler Verlet Method'])
plt.show()
