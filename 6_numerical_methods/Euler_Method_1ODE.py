#Euler Method :- 1st order ODE #
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,5,50)
y0 = -1
y = np.zeros(len(x))
##define f(y,t) as in the differential equation   dy/dx= f(y,x) ##
def f(y,x) : 
	z=x*np.cos(x)*np.sin(y)
	return z
def odeEuler(f,y0,x):
    '''Approximate the solution of y'=f(y,x) by Euler's method.

    Parameters
    ----------
    f : function
        Right-hand side of the differential equation y'=f(x,y), y(x_0)=y_0
    y0 : number
        Initial value y(x0)=y0 wher t0 is the entry at index 0 in the array x
    x :  array
        1D NumPy array of t values where we approximate y values. Time step
        at each iteration is given by x[n+1] - x[n].

    Returns
    -------
    y : 1D NumPy array
        Approximation y[n] of the solution y(x_n) computed by Euler's method.
    '''
    y[0] = y0
    for n in range(0,len(x)-1):
        y[n+1] = y[n] + f(y[n],x[n])*(x[n+1] -x[n])
    return y

y = odeEuler(f,y0,x)
plt.plot(x,y,'r.-')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('Euler Method Solution')
plt.title("Solution")
plt.grid()
plt.show()
