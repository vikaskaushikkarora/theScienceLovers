#Many Body 2D

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
from matplotlib.animation import FuncAnimation

n=20 # no.of objects
M=5*rd.rand(n)

#Time and Coordinates

h=0.05
t=np.arange(0,20,h)
T=len(t)

x=np.zeros((T,n))
y=np.zeros((T,n))
vx=np.zeros((T,n))
vy=np.zeros((T,n))

#initial conditions
for j in range(n):
	x[0,j]=8*((-1)**rd.randint(10))*rd.randn()
	y[0,j]=8*((-1)**rd.randint(10))*rd.randn()
	vx[0,j]=2*((-1)**rd.randint(10))*rd.rand()
	vy[0,j]=2*((-1)**rd.randint(10))*rd.rand()
	
#print (x)
#print(y)

for i in range (T-1):
	for j in range (n):
		sum1=0
		for k in range(n):
			if k != j :
				sum1=sum1+M[k]*(x[i,k]-x[i,j])*((x[i,k]-x[i,j])**2+(y[i,k]-y[i,j])**2)**(-1.5)
			else :
				sum1=sum1
		vx[i+1,j]=vx[i,j]+h*sum1
		x[i+1,j]=x[i,j]+h*vx[i+1,j]
		sum2=0
		for s in range (n):
			if s != j :
				sum2=sum2+M[s]*(y[i,s]-y[i,j])*((x[i,s]-x[i,j])**2+(y[i,s]-y[i,j])**2)**(-1.5)
			else :
				sum2=sum2
		vy[i+1,j]=vy[i,j]+h*sum2
		y[i+1,j]=y[i,j]+h*vy[i+1,j]
				
#print('new super array')
#print(x)
#Animation :
	
#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568])

#Set x and y limits 
ax.set_xlim(-20,20)
ax.set_ylim(-20,20)

#make background black
ax.set_facecolor('black')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')

#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])

#Logo Text :
ax.text(12,-19.90,'The Science Lovers',color='white',size=10)

line,=ax.plot([],[],'o',color='cyan',markersize=10)

def init():
	line.set_data([],[])
	return line,
	
def animate(i):
	s=3#speed of animation
	line.set_data(x[s*i],y[s*i])
	return line,
	

anim = FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 100, blit = True)

plt.show()