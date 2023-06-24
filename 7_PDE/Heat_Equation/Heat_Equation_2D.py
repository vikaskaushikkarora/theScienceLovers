#Heat Equation 2D _______________________________



#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



#______________________________

#Define Time and Space Meshgrid
n=1000 #Time Steps
mx=20 #Space Steps in x
my=20 #Space Steps in y
t=np.linspace(0,1.5,n)
dt=t[2]-t[1] #Time Interval
x=np.linspace(-1,1,mx)
dx=x[2]-x[1] #Space Interval in x
y=np.linspace(-1,1,my)
dy=y[2]-y[1] #Space Interval in y
#Temperature 
T=np.zeros(((n,mx,my)))
alpha=0.3 # Conductivity
beta=dt*alpha*dx**(-2)
gamma=dt*alpha*dy**(-2)


#______________________________

#Initial Conditions :-
for j in range(0,mx):
	for k in range (0,my):
		r=(x[j]**2+y[k]**2)**(0.5)
		T[0,j,k]= 50*r**2*np.exp(-5*r)


#Finite Difference Method
#Iterations :-
for i in range (n-1):
	for j in range (1,mx-1):
		for k in range (1,my-1):
			a=T[i,j,k]
			b=T[i,j+1,k]
			c=T[i,j-1,k]
			e=T[i,j,k+1]
			f=T[i,j,k-1]
			T[i+1,j,k]=(1-2*beta-2*gamma)*a+beta*(b+c)+gamma*(e+f)
		
	# Boundary Conditions
	# (The temperature gradient at boundaries is zero i.e. heat does not flow at the ends )
	T[i+1,0,:]=T[i+1,1,:]
	T[i+1,mx-1,:]=T[i+1,mx-2,:]
	T[i+1,:,0]=T[i+1,:,1]
	T[i+1,:,my-1]=T[i+1,:,my-2]




#______________________________

#Plotting Surface and Rod	
p,q=np.meshgrid(x,y)
u=np.zeros((mx,my))
fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')
for i in range (n):
	ax.set_facecolor('black')
	ax.set_axis_off()
	ax.set_xlim(-0.8,0.8)
	ax.set_ylim(-0.8,0.8)
	ax.set_zlim(-0.3,1.2)
	A=ax.view_init(elev=30, azim=120+0.4*i)
	ax.plot_surface(p,q,T[i,:,:],cmap='cool',alpha=0.6,antialiased=False)
	ax.quiver(1,1,0,-2,0,0,color='white',arrow_length_ratio=0.025)
	ax.quiver(1,1,0,0,-2,0,color='white',arrow_length_ratio=0.025)
	ax.quiver(1,1,0,0,0,1.2,color='white',arrow_length_ratio=0.03)
	ax.text(1,1,1.3,'Temp',size=15,color='white')
	plt.pause(0.1)
	ax.clear()

plt.show()