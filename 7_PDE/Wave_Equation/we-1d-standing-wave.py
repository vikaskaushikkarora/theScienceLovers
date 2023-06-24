# Wave Equation 1D ( Standing Wave ) :- ________________________________

#Importing Libraries 
import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,cos,exp,pi
from matplotlib import animation 


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
v0=np.zeros(m) #Initial Velocity



#______________________________

#Finite Difference Method
#Initial Conditions and Boundary Conditions
for j in range(m):
	y[0,j]=sin(2*pi*x[j])
	y[1,j]=y[0,j]


#Main Iteration Loop
for i in range(1,n-1):
	for j in range(1,m-1):
		y[i+1,j]=2*(1-a)*y[i,j]+a*(y[i,j+1]+y[i,j-1])-y[i-1,j]



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
	B=points.set_data([-0.005,1.005],[0,0])
	return line,points
	
anim = animation.FuncAnimation(fig, animate, frames = n, interval = 10, blit = True)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
anim.save('im.mp4', writer=writer)
