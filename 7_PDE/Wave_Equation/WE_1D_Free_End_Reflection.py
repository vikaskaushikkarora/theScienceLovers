# Wave Equation 1D ( Gaussian Moving ) :- ________________________________

#Importing Libraries 
import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,cos,exp,pi
from matplotlib.animation import FuncAnimation



#______________________________

#Variables
n=500 # Time Steps
m=200 # Space Divisions
c=1 # Speed of wave 
t=np.linspace(0,1.5,n)#Time
x=np.linspace(0,1,m) #Space
h=t[1]-t[0] #Time Division
k=x[1]-x[0]#Space Division
a=(h**2)*(c**2)*(k**(-2))

#Displacement of string particle in transverse direction
y=np.zeros((n,m))
v0=np.zeros(m) #Initial Velocity , if required to define initial conditions


#______________________________

#Finite Difference Method
#Initial Conditions
for j in range(m):
	y[0,j]=0.8*exp(-500*(x[j]-0.2)**2)-0.6*exp(-700*(x[j]-0.7)**2)
	y[1,j]=0.8*exp(-500*(x[j]-0.2-c*h)**2)-0.6*exp(-700*(x[j]-0.7-c*h)**2)


#Main Iteration Loop
for i in range(1,n-1):
	for j in range(1,m-1):
		y[i+1,j]=2*(1-a)*y[i,j]+a*(y[i,j+1]+y[i,j-1])-y[i-1,j]
	#Boundary Condition for right end
	y[i+1,m-1]=y[i+1,m-2]
		
	



#______________________________

#Animation
fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_xlim(-0.02,1.02)
ax.set_ylim(-1.5,1.5)
line,=ax.plot([],[],color='deepskyblue')
points,=ax.plot([],[],'o',color='yellow',markersize=10)


s=5
def animate(i):
	A=line.set_data(x,y[i,:])
	B=points.set_data([-0.005],[0])
	return line,points
	
anim = FuncAnimation(fig, animate, frames = n, interval = 10, blit = True)

plt.show()