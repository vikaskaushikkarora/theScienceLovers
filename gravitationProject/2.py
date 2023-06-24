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

def rec1(a,b,c,d,e):
		A=np.arange(a-0.5*c,a+0.5*c,0.001)
		A_=[b-0.5*d]*len(A)
		A__=[b+0.5*d]*len(A)
		B=np.arange(b-0.5*d,b+0.5*d,0.001)
		B_=[a-0.5*c]*len(B)
		B__=[a+0.5*c]*len(B)
		ax.plot(A,A_,'w',linewidth=e)
		ax.plot(A,A__,'w',linewidth=e)
		ax.plot(B_,B,'w',linewidth=e)
		ax.plot(B__,B,'w',linewidth=e)

ell(3,1.2,1.5,0.65)
rec1(5,0.55,01.8,0.22,0.5 )

A=ax.arrow(4.2,0.48,0,0.1,head_width=0.06, head_length=0.06,width=0.02, fc='green', ec='green')

#Stationary Texts in Animation

#Main text in Animation
ax.text(0.28,0.25,'Sun attracts the planets and the Earth , so they move around it .',size=20 , color='white')
ax.text(4.3,0.5,' represents the direction \n of force .',size=13 , color='white')
ax.text(2.85,0.87,'Sun',size=20 , color='Orange')


#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='skyblue',markersize=20)
#another line object : maybe plotting its path or anything else

#Time array ( omit if not required) :
t=np.arange(0,1,0.001)
dt=t[1]-t[0]
T=len(t)

#Initiallizing Function
def init():
	line.set_data([], [])
	return line,

x=np.zeros(T)
y=np.zeros(T)
for i in range (T):
	x[i]=3+1.5*np.cos(20*t[i])
	y[i]=1.2+0.65*np.sin(20*t[i])

# Repeatition Function
def animate(i):
	#setting data for line object
	line.set_data(x[i+1],y[i+1])
	#Other things in animations which vary for different frames 
	A=ax.arrow(x[i+1],y[i+1],-0.25*1.5*np.cos(20*t[i]),-0.25*0.65*np.sin(20*t[i]),head_width=0.06, head_length=0.06,width=0.02, fc='green', ec='green')
	#return the variables and objects in the function
	return A,line

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T-1, interval = 10, blit = True)

plt.show() 