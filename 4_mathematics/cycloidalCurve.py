#  Cycloidal Curve 
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
from numpy import sin
from numpy import cos

#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568])

#Set x and y limits 
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

#make background black
ax.set_facecolor('grey')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')

#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])

#Logo Text :
ax.text(3.05,-4.90,'The Science Lovers',color='white',size=10)


P,=ax.plot([],[],'o',color='cyan',markersize=5)
traj,=ax.plot([],[],color='lightskyblue')


t=np.linspace(0,10,1000)
h=t[2]-t[1]
T=len(t)

v=5
R=0.75
w=v*R**(-1)
a=np.zeros(T)
a0=-4.8
b=-1.5
x=np.zeros(T)
y=np.zeros(T)
for i in range (T):
	a[i]=a0+v*t[i]
	x[i]=a0+v*t[i]-R*np.sin(w*t[i])
	y[i]=b+R*np.cos(w*t[i])


def init():
	P.set_data([],[])
	traj.set_data([],[])
	return traj,P

def animate(i):

	traj.set_data(x[0:i],y[0:i])
	P.set_data(x[i],y[i])
	
	return traj,P

anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)

plt.show()

