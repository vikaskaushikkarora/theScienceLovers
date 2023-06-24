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


#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)


line,= ax.plot([], [],'o',color='orange',markersize=1)

#another line object : maybe plotting its path or anything else


#Time array ( omit if not required) :

n1=15
n2=n1+80
n3=n2+15
N=n3
#Initiallizing Function
def init():
	line.set_data([], [])
	return line,
	
# Repeatition Function
def animate(i):
	if i <= n1 :
		line.set_data(10,1.3)
		P=ax.text(0.8,0.5,'Because if it does \nWhy does not the Sun \nseem to move at all ?',color='lightskyblue',size=50+50*n1**(-1)*(i-n1))
	if ( i > n1 and i <= n2 ):
		line.set_data(10,13)
		P=P=ax.text(0.8,0.5,'Because if it does \nWhy does not the Sun \nseem to move at all ?',color='lightskyblue',size=50)
	if ( i > n2 and i <= n3 ):
		line.set_data(10,13)
		P=ax.text(0.8,0.5,'Because if it does \nWhy does not the Sun \nseem to move at all ?',color='lightskyblue',size=50*(n3-n2)**(-1)*(n3-i))
			

	return line,P

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = N, interval = 10, blit = True)


plt.show() 