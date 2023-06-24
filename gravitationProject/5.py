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

ax.scatter(6*np.random.rand(300,1),2*np.random.rand(300,1),s=0.3,color='white')
ax.scatter(6*np.random.rand(30,1),2*np.random.rand(30,1),s=3,color='white')
ax.scatter(6*np.random.rand(5,1),2*np.random.rand(5,1),s=5,color='white')


#Stationary figures in animation
A1=(-1)**(np.random.randint(10))*0.1*np.random.randn(10000)
B1=(-1)**(np.random.randint(10))*0.05*np.random.randn(10000)
ax.scatter(3+A1,1.2+B1,color='orange',s=0.1)



#Main text in Animation
ax.text(0.19,0.15,'Just like Sun attracts Earth , Earth also attracts Moon by Gravitation.\nAnd so do the rest of the planets . All planets have moons except \nMercury and Venus , ( more than 50 also sometimes ) .',size=20 , color='white')

ax.text(2.85,0.88,'Sun',size=20 , color='Orange')
ax.plot(5,1.8,'o',color='skyblue',markersize=20)
ax.plot(5,1.6,'o',color='white',markersize=10)
ax.text(5.23,1.77,'Earth',color='skyblue',size=20)
ax.text(5.23,1.57,'Moon',color='white',size=15)
#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='skyblue',markersize=20)
line1,= ax.plot([], [],'o',color='white',markersize=10)


#Time array ( omit if not required) :
t=np.arange(0,1,0.001)
dt=t[1]-t[0]
T=len(t)

#Initiallizing Function
def init():
	line.set_data([],[])
	line1.set_data([],[])
	return line,line1

x=np.zeros(T)
y=np.zeros(T)
x1=np.zeros(T)
y1=np.zeros(T)

for i in range (T):
	x[i]=3+1.5*np.cos(40*t[i])
	y[i]=1.2+0.65*np.sin(40*t[i])
	x1[i]=x[i]+0.15*np.cos(200*t[i])
	y1[i]=y[i]+0.07*np.sin(200*t[i])

# Repeatition Function
def animate(i):
	#setting data for line object
	line.set_data(x[i],y[i])
	line1.set_data(x1[i],y1[i])
	#Other things in animations which vary for different frames 
	
	#return the variables and objects in the function
	return line,line1

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T-1, interval = 10, blit = True)

plt.show() 