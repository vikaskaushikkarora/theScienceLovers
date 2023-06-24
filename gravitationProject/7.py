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


#Main text in Animation
ax.text(0.35,1.4,'If Sun applies gravitational force on Earth , \nDoes Earth also apply force on Sun ?',size=30 , color='lightskyblue')

#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)

#Sun and Earth

A1=(-1)**(np.random.randint(10))*0.3*np.random.randn(50000)
B1=(-1)**(np.random.randint(10))*0.15*np.random.randn(50000)
ax.scatter(0.7+A1,0.7+B1,color='orange',s=0.1)
ax.plot(3,0.7,'o',color='deepskyblue',markersize=30)

A=ax.arrow(1.7,0.7,0.8,0,head_width=0.1, head_length=0.2,width=0.02, fc='green', ec='green')

ax.text(2.2,0.8,'?',color='lightyellow',size=45)

# Newton's Third Law'

ax.text(3.5,0.6,'Because every action \nhas equal and \nopposite reaction ?',size=23,color='lightcyan')

plt.show() 