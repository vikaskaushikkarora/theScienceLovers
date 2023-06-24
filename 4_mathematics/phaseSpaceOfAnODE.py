# Phase Space And Spacetime
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
from numpy import sin
from numpy import cos
from numpy import random as rd

#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568])

#Set x and y limits 
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

#make background black
ax.set_facecolor('black')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')

#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])

#Logo Text :
ax.text(3.05,-4.90,'The Science Lovers',color='white',size=10)

ax.tick_params(
    axis='y',    
    which='both',   
    left=False,  
    right=False ,labelleft=False)
    #Remove x_ticks
ax.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)
n=100
x=np.linspace(0,10,4000)
h=x[2]-x[1]
L=len(x)
w=1
y=np.zeros((L,n))
z=np.zeros((L,n))
for j in range (n):
	y[0,j]=5*(-1)**(rd.randint(10))*rd.randn()
	z[0,j]=5*(-1)**(rd.randint(10))*rd.rand()
	
	for i in range (L-1):
		z[i+1,j]=z[i,j]-(w*w*y[i,j])*h
		y[i+1,j]=y[i,j]+z[i+1,j]*h


#Animation

traj,=ax.plot([],[],'o',color='lightskyblue',markersize=0.1)


def init():
	traj.set_data([],[])
	return traj,

def animate(i):
	s=5
	traj.set_data(y[0:int(s*i**(1.5))],z[0:int(s*i**(1.5))])
	
	return traj,

anim = FuncAnimation(fig, animate, init_func = init, frames = L, interval = 1, blit = True)

plt.show()