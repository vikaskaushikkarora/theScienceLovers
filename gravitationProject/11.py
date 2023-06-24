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


A1=(-1)**(np.random.randint(10))*0.5*np.random.randn(40000)
B1=(-1)**(np.random.randint(10))*0.25*np.random.randn(40000)
ax.scatter(1.4+A1,1+B1,color='orange',s=0.1)

#Stationary Texts in Animation

#Main text in Animation
ax.text(2.8,0.4,'Because Sun is quite \nheavy compared to Earth \n\nFor Sun Earth System ,this \ncentre of mass lies inside \nthe Sun !\n\nAnd we can not directly \nobserve the motion caused \nby Earth',color='lightcyan',size=25)

#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='orange',markersize=200)
line1,= ax.plot([], [],color='white')
#another line object : maybe plotting its path or anything else


#Time array ( omit if not required) :
t=np.arange(0,30,0.001)
dt=t[1]-t[0]
T=len(t)

x=np.zeros(T)
y=np.zeros(T)
for i in range (T):
	x[i]=1.4+0.16*np.cos(t[i])
	y[i]=1+0.08*np.sin(t[i])

#Initiallizing Function
def init():
	line.set_data([], [])
	line1.set_data([],[])
	return line , line1
	
# Repeatition Function
def animate(i):
	#setting data for line objects
	line.set_data(x[60*i],y[60*i])
	line1.set_data(x[0:60*i],y[0:60*i])
	#Other things in animations which vary for different frames 
	
	#return the variables and objects in the function
	return line,line1

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)

plt.show() 