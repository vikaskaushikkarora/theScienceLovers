# Phase Space And Spacetime
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib import animation
from numpy import sin
from numpy import cos

#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568],xlim=(-5,5),ylim=(-5,5),facecolor='grey')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')

ax.plot(0.1*np.random.randn(3000,1),0.1*np.random.randn(3000,1),'o',color='orange',markersize=0.2)

#if you want to remove the ticks on axies including gridlines
#ax.set_xticks([])
#ax.set_yticks([])

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


t=np.linspace(-1.5*np.pi,1.5*np.pi,1000)
h=t[2]-t[1]
T=len(t)

# define x (path) as a function of time :
	
def f(t):
	value=np.sin(t)
	return value

def g(t,f):
	value=(f(t+h)-f(t))*h**(-1)
	return value

# x coordinate of particle as a function of time :
x=f(t)

# velocity of particle as a function of time : 	
xdot=g(t,f)

#Animation

P,=ax.plot([],[],'o',color='cyan',markersize=5)
traj,=ax.plot([],[],color='lightskyblue',label='Phase Space')
Q,=ax.plot([],[],'o',color='coral',markersize=5)
traj1,=ax.plot([],[],color='lightcoral',label='Spacetime')
ax.legend()

def init():
	P.set_data([],[])
	traj.set_data([],[])
	Q.set_data([],[])
	traj1.set_data([],[])
	return traj,P,Q,traj1

def animate(i):
	s=1
	traj.set_data(x[0:s*i],xdot[0:s*i])
	P.set_data(x[s*i],xdot[s*i])
	traj1.set_data(x[0:s*i],t[0:s*i])
	Q.set_data(x[s*i],t[s*i])
	return traj,P,Q,traj1

anim = animation.FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=500)
anim.save('/sdcard/video.mp4', writer=writer)
