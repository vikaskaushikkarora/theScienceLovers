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

A1=(-1)**(np.random.randint(10))*0.1*np.random.randn(10000)
B1=(-1)**(np.random.randint(10))*0.05*np.random.randn(10000)
ax.scatter(3+A1,1+B1,color='orange',s=0.1)

ax.text(2.9,0.95,'Sun',color='orange',size=15)

ax.text(0.6,1.7,'If it is moving slow , it will be set into orbit .',color='lightgreen',size=25)
t=np.arange(0,10,0.001)
h=t[1]-t[0]
T=len(t)

K=50 #Strength of field = GM
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
#Time window and stepsize 
h=0.005 # You have to keep the stepsize as simple as possible because the differential equations are non linear and inhomogeneous and error may occur OR you could use the Euler Verlet Method too which will be a little help .
x=np.zeros(T)
z=np.zeros(T)
y=np.zeros(T)
w=np.zeros(T)

#Initial Conditions 
x[0]=-2
z[0]=1
y[0]=-0.2
w[0]=3

for i in range (0,len(t)-1):
	#I have used Euler Verlet method here . I have calculated the ith coordinate of distance from the ( i+1)th coordinate of velocity components . This conserves energy ...
	z[i+1]=z[i]+h*g(x[i],y[i])
	x[i+1]=x[i]+h*f(z[i+1])
	w[i+1]=w[i]+h*k(x[i],y[i])
	y[i+1]=y[i]+h*j(w[i+1])


#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='skyblue',markersize=20)
line1,= ax.plot([], [],color='lightskyblue',)
#Initiallizing Function
def init():
	line.set_data([], [])
	line1.set_data([],[])
	return line,line1

# Repeatition Function
def animate(i):
	#setting data for line object
	line.set_data(3+x[i],1+y[i])
	line1.set_data(3+x[0:i],1+y[0:i])
	#Other things in animations which vary for different frames 
	
	B=ax.arrow(3+x[i],1+y[i],5*(x[i+1]-x[i]),5*(y[i+1]-y[i]),head_width=0.06, head_length=0.06,width=0.02, fc='white', ec='white')
	
	#return the variables and objects in the function
	return line1,B,line

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T-1, interval = 10, blit = True)

plt.show() 