# Probability Density in Hydrogen Atom for p and d orbitals _______________________________

import numpy as np
from numpy import sin,cos,exp,pi
from scipy.integrate import quad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



#______________________________

# Function to create a random number array with given distribution function f
# n = Number of Random Numbers

def random(n,lowlim,uplim,h,f):
	
	x=np.arange(lowlim,uplim,h)
	# Give the limits and interval for random numbers and uniform spacing ....
	
	m=len(x)
	
	# A=Area under the curve of distribution function 
	A,A1=quad(f,lowlim,uplim)
	
	# Break up the x axis into small intervals for which total number of random numbers within is constant ......
	frac=np.zeros(m)
	
	# a is an array which contains number of random numbers per division in x axis
	a=np.zeros(m,dtype='int')
	
	for i in range(m):
		frac[i]=(f(x[i])*h)*A**(-1)
		a[i]=int(n*frac[i])
		b=sum(a)
	
	# array containing random numbers is rd
	rd=np.zeros(b)
	l=0
	for j in range(m):
		for i in range (a[j]):
			rd[l+i]=x[j]+h*np.random.rand()
		#print rd[l+i]
		l=l+a[j]
	return rd



#______________________________

# The radial and angular distribution functions :
def radial(x):
	#n=2 , l=1
	#y=(x**2)*exp(-x)
	#n=3 , l=1
	#y=((6-x)*x*exp(-0.667*x))**2
	#n=3 , l=2
	y=((x**2)*exp(-0.667*x))**2
	return y

def angular(x):
	# l=1 , m=0
	#z=(cos(x))**2
	 #l=1 , m=+-1
	#z=(sin(x))**2
	#l=2 , m=0
	z=(3*(cos(x)**2)-1)**2
	#l=2 , m=+-1
	#z=(sin(x)*cos(x))**2
	#l=2 , m=+-2
	#z=sin(x)**4
	return z

R1=random(60000,0,13,0.1,radial)
theta=random(59500,0,pi,0.005,angular)
a=len(theta)

R=R1[0:a]
phi=2*pi*np.random.rand(a)

x=R*sin(theta)*cos(phi)
y=R*sin(theta)*sin(phi)
z=R*cos(theta)



#______________________________

# Drawing Figures 

fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')
ax.set_axis_off()
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-5,5)
ax.view_init(elev=40,azim=60)

ax.plot(x,y,z,'o',color='deepskyblue',markersize=0.3)

ax.quiver(0,0,0,1.5,0,0,color='white',arrow_length_ratio=0.05)
ax.quiver(0,0,0,0,1.5,0,color='white',arrow_length_ratio=0.05)
ax.quiver(0,0,0,0,0,5.3,color='orange',arrow_length_ratio=0.045)

plt.show()