# Wave Equation 2D ________________________________

#Importing Libraries 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import sin,cos,exp,pi
from mpl_toolkits.mplot3d import Axes3D



#______________________________

#Variables
n=2000 # Time Steps
mx=40 # Space Divisions x
my=40 #Space Divisions y
c=1 # Speed of wave 
t=np.linspace(0,1.5,n)#Time
x=np.linspace(-1,1,mx)#Space x
y=np.linspace(-1,1,my) #Space y
dt=t[1]-t[0] #Time Division
dx=x[1]-x[0]#Space Division x
dy=y[1]-y[0]#Space Division y

a=(c*dt*dx**(-1))**2
b=(c*dt*dy**(-1))**2

#Displacement of string particle in transverse direction
z=np.zeros(((n,mx,my)))
#v0=np.zeros((mx,my)) #Initial Velocity if it is required in order to define the initial conditions



#______________________________

#Finite Difference Method
#Initial Conditions and Boundary Conditions

#Main Iteration Loop
for i in range(1,n-1):
	for j in range(1,mx-1):
		for k in range(1,my-1):
			# Define the source slits here :-
			if ( y[k] > -0.2 and y[k] < -0.1 ):
				z[i,0,k]=0.03*sin(40*t[i])
			elif ( y[k] > 0.1 and y[k] < 0.2 ):
				z[i,0,k]=0.03*sin(40*t[i])
			# Define the working of numerical solution here :-
			z[i+1,j,k]=2*(1-a-b)*z[i,j,k]+a*(z[i,j+1,k]+z[i,j-1,k])+b*(z[i,j,k+1]+z[i,j,k-1])-z[i-1,j,k]



#______________________________

#Animation
fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')

X,Y= np.meshgrid(x,y)
s=20
for i in range(int(n*s**(-1))):
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_axis_off()
	ax.set_xlim(-0.7,0.7)
	ax.set_ylim(-0.7,0.7)
	ax.set_zlim(-0.05,0.05)
	ax.set_facecolor('black')
	ax.view_init(elev=90 , azim=0)
	ax.plot_surface(X,Y,z[s*i,:,:],antialiased=False)
	ax.text2D(0.84, 0.05, "The Science Lovers", transform=ax.transAxes,size=15,ha='center',va='center',color='yellow')
	plt.pause(0.1)
	ax.clear()

plt.show()