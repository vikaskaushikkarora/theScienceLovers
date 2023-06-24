# Wave Equation 1D (Sinosuidal Waveform) :- ________________________________

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
t=np.linspace(0,1,n)#Time
x=np.linspace(0,1,m) #Space
h=t[1]-t[0] #Time Division
k=x[1]-x[0]#Space Division
a=(h**2)*(c**2)*(k**(-2))

#Displacement of string particle in transverse direction
y=np.zeros((n,m))


#______________________________

#Finite Difference Method
#Initial Conditions and Boundary Conditions at right end
for j in range(1,m):
	y[0,j]=0
	y[1,j]=0

#Main Iteration Loop
w=40
for i in range(1,n-1):
	y[i,0]=0.5*sin(w*t[i]) # Boundary Conditions at left end
	for j in range(1,m-1):
		y[i+1,j]=2*(1-a)*y[i,j]+a*(y[i,j+1]+y[i,j-1])-y[i-1,j]



#______________________________

#Animation
fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_xlim(-0.1,1.02)
ax.set_ylim(-1.5,1.5)
line,=ax.plot([],[],color='deepskyblue')
point,=ax.plot([],[],'o',color='yellow',markersize=10)
rod,=ax.plot([],[],color='white')


s=5
def animate(i):
	A=line.set_data(x,y[i,:])
	B=point.set_data([1.005],[0])
	C=rod.set_data([-0.08,0],[y[i,0],y[i,0]])
	return line,point,rod
	
anim = FuncAnimation(fig, animate, frames = n, interval = 10, blit = True)

plt.show()