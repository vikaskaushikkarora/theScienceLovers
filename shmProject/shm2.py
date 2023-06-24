#SHM Animation(1)
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
p=np.arange(-2.8,-2.3,0.01)
P=len(p)
q=[0.7]*P
r=[-0.7]*P
a=np.arange(-0.7,0.7,0.05)
b=[-1.3]*len(a)
ax.plot(b,a,'wo',markersize=0.5)
ax.fill_between(p,q,r,color='lightyellow')

#Stationary Texts in Animation
ax.text(-2.71,0.76,'Wall',color='white',size=20)

ax.text(-1.6,0.75,'Mean Position',color='white',size=15)

ax.text(-1.45,-0.35,'Force',size=20,color='green')

ax.text(-0.5,-0.45,'If the ball moves towards right , \nthe force acts in the left \ndirection attracting ball to the \nmean position and if the ball is on \nthe left side , the force acts in the \nright direction . Thus the ball vibrates \nperiodically around the centre \nposition.',size=20 , color='aliceblue')

#Logo Text :
ax.text(1.5,-0.75,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='skyblue',markersize=30)
#another line object : maybe plotting its path or anything else
line1, =ax.plot([],[],color='deepskyblue')

#Time array ( omit if not required) :
t=np.arange(0,1,0.001)
dt=t[1]-t[0]
T=len(t)

#Initiallizing Function
def init():
	line.set_data([], [])
	line1.set_data([],[]) 
	return line , line1
	
# Repeatition Function
def animate(i):
	#setting data for line objects
	y=0
	x=-1.3+0.5*np.sin(50*t[i])
	x1=np.arange(-2.3,x,0.01)
	y1=0.05*np.sin(10*np.pi*(x1+2.3)*(x+2.3)**(-1))
	line.set_data(x,y)
	line1.set_data(x1,y1)
	#Other things in animations which vary for different frames 
	A=ax.arrow(x,-0.2,-0.5*(x+1.3),0, head_width=0.06, head_length=0.06,width=0.02, fc='green', ec='green')
	#return the variables and objects in the function
	return line1,line,A

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)
plt.show() 
