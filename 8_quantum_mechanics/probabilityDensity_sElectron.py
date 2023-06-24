(# Probability Density of s -electron in Hydrogen Atom _______________________________


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

# The radial distribution functions :
def radial(x):
	#n=1 , l=0   ( 1 s )
	#y=exp(-2*x)
	#n=2 , l=0   ( 2 s )
	#y=((2-x)**2)*exp(-x)
	# n=3 , l=0   (3  s )
	y=((27-18*x+2*x**2)**2)*exp(-0.667*x)
	return y


R=random(150000,0,12,0.1,radial)
b=len(R)

theta=pi*np.random.rand(b)
phi=2*pi*np.random.rand(b)

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
ax.set_xlim(-7,7)
ax.set_ylim(-7,7)
ax.set_zlim(-7,7)
ax.view_init(elev=30,azim=30)

ax.plot(x,y,z,'o',color='deepskyblue',markersize=0.4)

ax.quiver(0,0,0,8,0,0,color='white',arrow_length_ratio=0.045)
ax.quiver(0,0,0,0,8,0,color='white',arrow_length_ratio=0.045)
ax.quiver(0,0,0,0,0,8,color='orange',arrow_length_ratio=0.045)


plt.show()