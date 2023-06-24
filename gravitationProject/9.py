# Three Body Problems
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
G=1 # Strength of field
# Masses of three bodie
m1=1
m2=1
t=np.arange(0,16,0.001)
h=t[1]-t[0]
T=len(t)
x1=np.zeros(len(t))# X coordinate 1
y1=np.zeros(len(t))#Y coordinate 1
z1=np.zeros(len(t)) # X coordinate of velocity of mass 1
w1=np.zeros(len(t))# Y ccordinate of velocity of mass 2
x2=np.zeros(len(t))# And similarily these
y2=np.zeros(len(t))
z2=np.zeros(len(t))
w2=np.zeros(len(t))

x1[0]=0
y1[0]=0
z1[0]=0
w1[0]=3**(-0.5)
x2[0]=1.5
y2[0]=0
z2[0]=0
w2[0]=-3**(-0.5)

# Equations of motions of three objects 
def a(z1):
	A=z1
	return A
def b(x1,y1,x2,y2):
	B=G*m2*(x2-x1)*((x1-x2)**2+(y1-y2)**2)**(-1.5)
	return B
def c(w1):
	C=w1
	return C
def d(x1,y1,x2,y2):
	D=G*m2*(y2-y1)*((x1-x2)**2+(y1-y2)**2)**(-1.5)
	return D
def e(z2):
	E=z2
	return E
def f(x1,y1,x2,y2):
	F=G*m1*(x1-x2)*((x1-x2)**2+(y1-y2)**2)**(-1.5)
	return F
def j(w2):
	J=w2
	return J
def k(x1,y1,x2,y2):
	K=G*m1*(y1-y2)*((x1-x2)**2+(y1-y2)**2)**(-1.5)
	return K

#Iterations : We have used Euler Verlet Method to conserve Energy

for i in range (0,T-1):
	z1[i+1]=z1[i]+h*b(x1[i],y1[i],x2[i],y2[i])
	x1[i+1]=x1[i]+h*a(z1[i+1])
	w1[i+1]=w1[i]+h*d(x1[i],y1[i],x2[i],y2[i])
	y1[i+1]=y1[i]+h*c(w1[i+1])
	z2[i+1]=z2[i]+h*f(x1[i],y1[i],x2[i],y2[i])
	x2[i+1]=x2[i]+h*e(z2[i+1])
	w2[i+1]=w2[i]+h*k(x1[i],y1[i],x2[i],y2[i])
	y2[i+1]=y2[i]+h*j(w2[i+1])



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
ax.text(2.7,0.5,'Earth also applies a force on Sun \nbut it`s effects are too small to be \nvisible .\n\nWhen two objects are gravitationally \nbound , they go around a common \npoint which is centre of mass .\n\nFor objects of equal masses , \nthis is the central point .',size=21 , color='lightcyan')

ax.text(1.5,1,'Centre of \n   mass .',size=10 , color='lightcyan')

#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='lightskyblue',markersize=35)
line1,= ax.plot([], [],'o',color='lightskyblue',markersize=35)
traj,= ax.plot([], [],color='skyblue')
traj1,= ax.plot([], [],color='skyblue')


#Initiallizing Function
def init():
	line.set_data([], [])
	line1.set_data([],[])
	traj.set_data([], [])
	traj1.set_data([],[])
	
	return line , line1,traj,traj1
	
# Repeatition Function
def animate(i):
	#setting data for line objects
	line.set_data(1+x1[40*i],1+y1[40*i])
	line1.set_data(1+x2[40*i],1+y2[40*i])
	traj.set_data(1+x1[0:40*i],1+y1[0:40*i])
	traj1.set_data(1+x2[0:40*i],1+y2[0:40*i])
	#Other things in animations which vary for different frames 
	
	#return the variables and objects in the function
	return line,line1,traj,traj1

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True,repeat=True)
plt.show()