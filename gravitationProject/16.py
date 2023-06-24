#Temp:O
#centre of fig :(3,1)
#centre of text :(5,1)
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


ax.text(2.9,0.95,'Sun',color='orange',size=15)

ax.text(0.6,1.5,'If object does not have any prependicular motion \nand escape velocity, it will bump into Sun .',color='seagreen',size=25)
#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='orange',markersize=0.2)
#Initiallizing Function
def init():
	line.set_data([], [])
	return line,

# Repeatition Function
def animate(i):
	A1=(-1)**(np.random.randint(10))*(0.1+i*0.0005)*np.random.randn(10000+i*500)
	B1=(-1)**(np.random.randint(10))*(0.05+i*0.00025)*np.random.randn(10000+i*500)
	line.set_data(3+A1,1+B1)
		
	return line,

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 10, blit = True)

plt.show() 