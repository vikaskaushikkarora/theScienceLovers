# Wave Equation 1D ( Transmission and Reflection) :- ________________________________

#Importing Libraries 
import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,cos,exp,pi
from matplotlib.animation import FuncAnimation



#______________________________

#Variables
n=1000 # Time Steps
m=200 # Space Divisions
t=np.linspace(0,1.5,n)#Time
x=np.linspace(0,1,m) #Space
x0=x[0:int(0.5*m)] # First String
x1=x[int(0.5*m):m] # Second String
h=t[1]-t[0] #Time Division
k=x[1]-x[0]#Space Division
c=np.zeros(m)# Speed of wave ,it is variable with distance bcoz the mass density is variable

#Displacement of string particle in transverse direction
y=np.zeros((n,m))
v0=np.zeros(m) #Initial Velocity , if required to define initial conditions


#______________________________

#Finite Difference Method
#Initial Conditions and Boundary Conditions
for j in range(m):
	# Define Speed of the wave for both mediums is variable due to different mass densities
	if x[j]< 0.5 :
		c[j]=3
	else :
		c[j]=1.5
	
	#define initial conditions
	y[0,j]=0.7*np.exp(-500*(x[j]-0.2)**2)
	y[1,j]=0.7*np.exp(-500*(x[j]-0.2-c[j]*h)**2)


#Main Iteration Loop
a=(h**2)*(c**2)*(k**(-2))

for i in range(1,n-1):
	for j in range(1,m-1):
		y[i+1,j]=2*(1-a[j])*y[i,j]+a[j]*(y[i,j+1]+y[i,j-1])-y[i-1,j]

# Displacements of particles on each string 
y0=np.zeros((n,int(0.5*m)))
y1=np.zeros((n,m-int(0.5*m)))
for j in range(int(0.5*m)):
	y0[:,j]=y[:,j]
for j in range(int(0.5*m),m):
	y1[:,j-int(0.5*m)]=y[:,j]


#______________________________

#Animation
fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_xlim(-0.02,1.02)
ax.set_ylim(-1.5,1.5)
line,=ax.plot([],[],color='deepskyblue')
line1,=ax.plot([],[],color='lightcoral',linewidth=4)
points,=ax.plot([],[],'o',color='yellow',markersize=10)


s=5
def animate(i):
	A=line.set_data(x0,y0[i,:])
	B=line1.set_data(x1,y1[i,:])
	C=points.set_data([-0.005,1.005],[0,0])
	return line,line1,points
	
anim = FuncAnimation(fig, animate, frames = n, interval = 10, blit = True)

plt.show()