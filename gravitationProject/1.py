#Temp:O
#centre of fig :(3,1.1)
#centre of text :(3,1,0.4)
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.20,0.015,0.74,0.975])

#Set x and y limits 
ax.set_xlim(0,6)
ax.set_ylim(0,2)
#make background black
ax.set_facecolor('black')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')
#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])

#Stationary figures in animation
ax.scatter(6*np.random.rand(300,1),2*np.random.rand(300,1),s=0.3,color='white')
ax.scatter(6*np.random.rand(50,1),2*np.random.rand(50,1),s=3,color='white')
ax.scatter(6*np.random.rand(10,1),2*np.random.rand(10,1),s=5,color='white')

#Stationary Texts in Animation

#Main text in Animation
ax.text(0.4,0.4,'Gravitation is the force every object exerts on another object in \nthe universe .And hence they tend to be close to each other .',size=20 , color='lightcyan')

#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='orange',markersize=75)
line1,= ax.plot([], [],'o',color='lightskyblue',markersize=35)
#another line object : maybe plotting its path or anything else


#Time array ( omit if not required) :
t=np.arange(0,1,0.001)
dt=t[1]-t[0]
T=len(t)

# 1D Gravitational Programme

x1=np.zeros(T)
vx1=np.zeros(T)
x2=np.zeros(T)
vx2=np.zeros(T)
m1=5
m2=1
x1[0]=1.5
vx1[0]=0
x2[0]=3.7
vx2[0]=19

for i in range (T-1):
	vx1[i+1]=vx1[i]+dt*200*(m2*(x2[i]-x1[i])**(-2))
	x1[i+1]=x1[i]+dt*vx1[i+1]
	vx2[i+1]=vx2[i]-dt*200*(m1*(x2[i]-x1[i])**(-2))
	x2[i+1]=x2[i]+dt*vx2[i+1]
	
#Initiallizing Function
def init():
	line.set_data([], [])
	line1.set_data([],[])
	return line , line1
	
# Repeatition Function
def animate(i):
	#setting data for line objects
	line.set_data(x1[i],1.3)
	line1.set_data(x2[i],1.3)
	#Other things in animations which vary for different frames 
	
	#return the variables and objects in the function
	return line,line1

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)

plt.show() 