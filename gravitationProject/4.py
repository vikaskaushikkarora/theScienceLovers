#Temp:A1a
#centre of fig :(1.5,1)
#centre of text :(4.5,1)
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
ax.scatter(6*np.random.rand(40,1),2*np.random.rand(40,1),s=3,color='white')
ax.scatter(6*np.random.rand(5,1),2*np.random.rand(5,1),s=5,color='white')


A1=(-1)**(np.random.randint(10))*0.04*np.random.randn(10000)
B1=(-1)**(np.random.randint(10))*0.02*np.random.randn(10000)
ax.scatter(0.5+A1,1.1+B1,color='orange',s=0.1)


#Main text in Animation on right
#Headline:
ax.text(2.85,1.6,'Kepler`s Other Laws',color='mediumseagreen',size=35)
#Extra Text
ax.text(2.95,0.5,'All the planets move around the \nSun in ellipses, not in circles . And \nwhen the planet is near the Sun \nin it`s orbit , it moves pretty fast .\nBut when it is far away , it moves \nvery slowly .',size=20 , color='white')

#Logo Text :
ax.text(0.2,0.1,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='skyblue',markersize=25)
line1,=ax.plot([],[],'-.',color='lightskyblue')
#another line object : maybe plotting its path or anything else

#Time array ( omit if not required) :
t=np.arange(0,25,0.001)
dt=t[1]-t[0]
T=len(t)

K=1 #Strength of field = GM
# Write down equations of motion of the object in plane using x and y coordinates which are two second order equations , so we convert them into four first oder equations as:
def f(z):
	A=z
	return A
def g(x,y):
	B=-K*x*(x**2+y**2)**(-1.5)
	return B
def j(w):
	C=w
	return C
def k(x,y):
	D=-K*y*(x**2+y**2)**(-1.5)
	return D
	
x=np.zeros(T)
z=np.zeros(T)
y=np.zeros(T)
w=np.zeros(T)


#Initial Conditions 
x[0]=2
z[0]=-0.45
y[0]=0
w[0]=0.24

for i in range (0,T-1):
	#I have used Euler Verlet method here . I have calculated the ith coordinate of distance from the ( i+1)th coordinate of velocity components . This conserves energy ...
	z[i+1]=z[i]+dt*g(x[i],y[i])
	x[i+1]=x[i]+dt*f(z[i+1])
	w[i+1]=w[i]+dt*k(x[i],y[i])
	y[i+1]=y[i]+dt*j(w[i+1])

#Initiallizing Function
def init():
	line.set_data([], [])
	line1.set_data([],[])
	return line1,line
	
# Repeatition Function
def animate(i):
	#setting data for line object
	line.set_data(0.5+x[40*i],1.1+y[40*i])
	line1.set_data(0.5+x[0:40*i],1.1+y[0:40*i])

	return line1,line

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)
plt.show()