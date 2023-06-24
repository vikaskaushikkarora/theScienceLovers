#Graviation 2D#
import numpy as np
import matplotlib.pyplot as plt
K=1 #Strength of field = GM
# Write down equations of motion of the object in plane using x and y coordinates which are two second order equations , so we convert them into four first oder equations as:
def f(z):
	A=z
	return A
def g(x,y):
	B=-K*x*(x**2+y**2)**(-1.5)
	return B
def j(w):
	C=w
	return C
def k(x,y):
	D=-K*y*(x**2+y**2)**(-1.5)
	return D
#Time window and stepsize 
h=0.001 # You have to keep the stepsize as simple as possible because the differential equations are non linear and inhomogeneous and error may occur OR you could use the Euler Verlet Method too which will be a little help .
t=np.arange(0,15,h)
x=np.zeros(len(t))
z=np.zeros(len(t))
y=np.zeros(len(t))
w=np.zeros(len(t))

#Initial Conditions 
x[0]=1
z[0]=0
y[0]=0
w[0]=0.4

for i in range (0,len(t)-1):
	#I have used Euler Verlet method here . I have calculated the ith coordinate of distance from the ( i+1)th coordinate of velocity components . This conserves energy ...
	z[i+1]=z[i]+h*g(x[i],y[i])
	x[i+1]=x[i]+h*f(z[i+1])
	w[i+1]=w[i]+h*k(x[i],y[i])
	y[i+1]=y[i]+h*j(w[i+1])
plt.plot(x,y,'r')
plt.grid()
plt.show()
