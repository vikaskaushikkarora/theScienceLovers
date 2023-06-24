#SHM Animation (0)
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
fig = plt.figure() 
ax = fig.add_axes([0.1,0.05,0.85,0.85])
ax.set_xlim(-3,3)
ax.set_ylim(-1,1)
p=np.arange(0,0.5,0.01)
P=len(p)
q=[0.5]*P
r=[-0.5]*P
ax.fill_between(p,q,r,color='lightyellow')
line,= ax.plot([], [],'o',color='skyblue',markersize=30)
line1, =ax.plot([],[],color='deepskyblue')
ax.set_facecolor('black')
ax.grid(ls='-.',lw=0.5,color='white')
ax.text(0.07,0.56,'Wall',color='white',size=23)
ax.text(-2,0.35,'SIMPLE',color='lightcyan',size=30)
ax.text(-2,0.15,'HARMONIC',color='lightcyan',size=30)
ax.text(-2,-0.05,'MOTION',color='lightcyan',size=30)
ax.text(-2,-0.45,'( Explaination and Animation )',color='lavenderblush',size=15)
ax.text(1.5,-0.75,'The Science Lovers',color='white',size=10)
ax.set_xticks([])
ax.set_yticks([])
t=np.arange(0,1,0.001)
dt=t[1]-t[0]
T=len(t)
def init():
	line.set_data([], [])
	line1.set_data([],[]) 
	return line , line1
def animate(i):
	y=0
	x=1.5+0.5*np.sin(50*t[i])
	x1=np.arange(0.5,x,0.01)
	y1=0.05*np.sin(10*np.pi*(x1-0.5)*(x-0.5)**(-1))
	line.set_data(x,y)
	line1.set_data(x1,y1)
	text=ax.text(x-0.115,y+0.15,'Ball',color='white',size=20)
	return line1,line,text


anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)

plt.show() 
