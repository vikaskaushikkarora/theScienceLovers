#SHM animation (2)
#import libraries
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.20,0.05,0.67,0.9])
#Set x and y limits 
ax.set_xlim(-3,3)
ax.set_ylim(-1,1)
#make background black
ax.set_facecolor('black')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')
#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])

#Stationary figures in animation
ax.arrow(2.6,-0.5,0,1,head_width=0.04, head_length=0.04,width=0.01, fc='skyblue', ec='green')
ax.arrow(-2.4,-0.7,1.5,0,head_width=0.04, head_length=0.04,width=0.005, fc='skyblue', ec='green')
#Stationary Texts in Animation
ax.text(-2.3,-0.85,'Time',size=15,color='lightyellow')
ax.text(1.8,0.65,'Displacememt',size=15,color='lightyellow')
#Logo Text :
ax.text(2,-0.9,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='deepskyblue',markersize=30)
#another line object : maybe plotting its path or anything else
line1, =ax.plot([],[],'o',color='white',markersize=2)
line2, =ax.plot([],[],color='white')

#Time array ( omit if not required) :
t=np.arange(0,1,0.001)
dt=t[1]-t[0]
T=len(t)

#Initiallizing Function
def init():
	line.set_data([], [])
	line1.set_data([],[]) 
	line2.set_data([],[]) 
	return line , line1
	
# Repeatition Function
def animate(i):
	#setting data for line objects
	x=-2.7
	y=0.50*np.sin(50*t[i])
	x1=np.arange(-2.7,-2.4,0.05)
	y1=[y]*len(x1)
	x2=np.arange(-2.4,2.35,0.01)
	y2=0.5*np.sin(50*t[i]-5*(x2+2.4))
	line.set_data(x,y)
	line1.set_data(x1,y1)
	line2.set_data(x2,y2)
	#Other things in animations which vary for different frames 
	A=ax.arrow(-2.7,0,0,y-0.01 ,head_width=0.04, head_length=0.04,width=0.02, fc='skyblue', ec='skyblue')
	#return the variables and objects in the function
	return line1,line,line2,A

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)
plt.show() 
