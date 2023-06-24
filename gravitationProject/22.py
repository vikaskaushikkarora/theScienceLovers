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
ax.scatter(3+A1,1.2+B1,color='orange',s=0.1)

def ell (a,b,c,d):
	A=np.arange(a-c,a+c,0.0001)
	B=b+d*(c**(-1))*np.sqrt(c**2-(A-a)**2)
	B_=b-d*(c**(-1))*np.sqrt(c**2-(A-a)**2)
	plt.plot(A,B,'w')
	plt.plot(A,B_,'w')



ell(3,1.2,1.5,0.65)


#Stationary Texts in Animation

#Main text in Animation
ax.text(0.28,0.25,'Sun attracts the planets and the Earth , so they move around it .',size=20 , color='white')
ax.text(4.3,0.5,' represents the direction \n of force .',size=13 , color='white')
ax.text(2.85,0.87,'Sun',size=20 , color='Orange')


#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='skyblue',markersize=30)

line1,= ax.plot([], [],'o',color='white',markersize=20)

line2,= ax.plot([], [],'o',color='white',markersize=20)

line3,= ax.plot([], [],'o',color='white',markersize=20)

#another line object : maybe plotting its path or anything else

#Time array ( omit if not required) :
t=np.arange(0,1,0.001)
dt=t[1]-t[0]
T=len(t)

#Initiallizing Function
def init():
	line.set_data([], [])
	line1.set_data([],[])
	line2.set_data([],[])
	line3.set_data([],[])
	return line,line1,line2,line3

x=np.zeros(T)
y=np.zeros(T)
for i in range (T):
	x[i]=3+1.5*np.cos(20*t[i])
	y[i]=1.2+0.65*np.sin(20*t[i])
	x1[i]=3+1.5*np.cos(20*t[i]+np.pi*(0.333))
	y1[i]=1.2+0.65*np.sin(20*t[i]+np.pi*(0.333))
	x2[i]=3+1.5*np.cos(20*t[i]-np.pi*(0.333))
	y2[i]=1.2+0.65*np.sin(20*t[i]-np.pi*(0.333))
	x3[i]=3+1.5*np.cos(20*t[i]+np.pi)
	y3[i]=1.2+0.65*np.sin(20*t[i]+np.pi)
	
	
	
# Repeatition Function
def animate(i):
	#setting data for line object
	line.set_data(x[i+1],y[i+1])
	line1.set_data(x1[i+1],y1[i+1])
	line2.set_data(x2[i+1],y2[i+1])
	line3.set_data(x3[i+1],y3[i+1])
	
	
	return line,line1,line2,line3

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T-1, interval = 10, blit = True)

plt.show() 