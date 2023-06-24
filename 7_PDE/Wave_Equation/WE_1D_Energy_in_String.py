# Wave Equation 1D ( Energy in String Wave) :- ________________________________

#Importing Libraries 
import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,cos,exp,pi
from matplotlib.animation import FuncAnimation



#______________________________

#Variables
n=700 # Time Steps
m=200 # Space Divisions
c=1 # Speed of wave 
t=np.linspace(0,1.8,n)#Time
x=np.linspace(0,1,m) #Space
h=t[1]-t[0] #Time Division
k=x[1]-x[0]#Space Division
a=(h**2)*(c**2)*(k**(-2))

#Displacement of string particle in transverse direction
y=np.zeros((n,m))
v0=np.zeros(m) #Initial Velocity



#______________________________

#Finite Difference Method
#Initial Conditions and Boundary Conditions
for j in range(m):
	y[0,j]=0.5*exp(-500*(x[j]-0.3)**2)
	y[1,j]=0.5*exp(-500*(x[j]-0.3)**2)


#Main Iteration Loop
for i in range(1,n-1):
	for j in range(1,m-1):
		y[i+1,j]=2*(1-a)*y[i,j]+a*(y[i,j+1]+y[i,j-1])-y[i-1,j]


#Calculating Total Energy for each element at each instant of time 
yx=np.zeros((n-1,m-1)) #dy/dx
yt=np.zeros((n-1,m-1)) #dy/dt
for i in range(1,n):
	for j in range(1,m):
		yx[i-1,j-1]=(y[i,j]-y[i,j-1])*k**(-1)
		yt[i-1,j-1]=(y[i,j]-y[i-1,j])*h**(-1)

#Total Energy
E=(((c**2)*yx**2+yt**2)*k)-0.8
x0=x[1:m] #Erasing x[0]



#______________________________

#Animation
fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_xlim(-0.02,1.02)
ax.set_ylim(-1.3,0.7)
point,=ax.plot([],[],'yo',markersize=10)
line,=ax.plot([],[],color='deepskyblue')
energy,=ax.plot([],[],color='lightcoral')

s=5
def animate(i):
	A=line.set_data(x,y[i+1,:])
	B=point.set_data(1,0)
	C=energy.set_data(x0,E[i,:])
	return line,energy,point
	
anim = FuncAnimation(fig, animate, frames = n, interval = 10, blit = True)


plt.show()