# Interacting Particles in a Box 
#Importing Libraries and Modules _______________________________
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
from numpy import sin
from numpy import cos

#Working Programme _______________________________
t_fin=5
t=np.linspace(0,t_fin,5000) #Time Window
h=t[2]-t[1] #Step Size
T=len(t) #Length of t
n=10 #number of particles
#Coordinates of space and velocity
x=np.zeros((T,n))
y=np.zeros((T,n))
vx=np.zeros((T,n))
vy=np.zeros((T,n))
n1=np.zeros(T) #Particles in left half
n2=np.zeros(T)#Particles in right half

#Initial Condotions
x[0,:]=-1.5*np.random.rand(1,n)
y[0,:]=-1.5*np.random.rand(1,n)
for j in range (n):
	vx[0,j]=3*(-1)**(np.random.randint(10))*np.random.randn()
	vy[0,j]=3*(-1)**(np.random.randint(10))*np.random.randn()

#Main Loop
for i in range (T-1):
# dummy varaibles to count n1 for time t[i]
	a=0
	b=0
	for j in range (n):
		if x[i,j] < 0:
			a=a+1
		else :
			b=b+1
		sum1=0
		sum2=0
#Particles' Interaction with each other
		for k in range(n):
			if ( k != j and abs(x[i,j]-x[i,k]) < 0.1  and abs(y[i,j]-y[i,k]) < 0.1 ) :
				sum1=sum1-10**(-2)*(x[i,k]-x[i,j])*((x[i,k]-x[i,j])**2+(y[i,k]-y[i,j])**2)**(-2.5)
				sum2=sum2-10**(-2)*(y[i,k]-y[i,j])*((x[i,k]-x[i,j])**2+(y[i,k]-y[i,j])**2)**(-2.5)
			else :
				sum1=sum1
				sum2=sum2			
#Collisions with Boundaries
		if ( x[i,j] < -1.9 ):
			vx[i+1,j]=-vx[i,j]
			vy[i+1,j]=vy[i,j]
		elif ( x[i,j] > 1.9):
			vx[i+1,j]=-vx[i,j]
			vy[i+1,j]=vy[i,j]
		elif ( y[i,j] < -1.9 ):
			vy[i+1,j]=-vy[i,j]
			vx[i+1,j]=vx[i,j]
		elif ( y[i,j] > 0.1 ):
			vy[i+1,j]=-vy[i,j]
			vx[i+1,j]=vx[i,j]
		else :
			vx[i+1,j]=vx[i,j]+h*sum1
			vy[i+1,j]=vy[i,j]+h*sum2
#Collisions with wall
		if (abs(x[i,j]) < 0.02 and y[i,j] > -1.6 ) :
			vx[i+1,j]=-vx[i,j]
#Equations of motion
		x[i+1,j]=x[i,j]+h*vx[i+1,j]
		y[i+1,j]=y[i,j]+h*vy[i+1,j]
#Callculating No. of particles on each side
	n1[i]=a
	n2[i]=b


#Animation _______________________________
#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.284])
ax1=fig.add_axes([0.0005,0.494,0.998,0.240])
fig.tight_layout()

#Set x and y limits 
ax.set_xlim(-2,2)
ax.set_ylim(-2,0.2)
ax1.set_xlim(-0.5,t_fin+0.5)
ax1.set_ylim(-0.5,n+1)

#make background black
ax.set_facecolor('black')
ax1.set_facecolor('black')

#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])
ax1.set_xticks([])

#Logo Text 
ax.text(1.05,-1.85,'The Science Lovers',color='white',size=10)

# Wall and Boundaries
def rectangle(x_cord=0,y_cord=0,length=1,breadth=0.5,linewidth=5,linecolor='blue',facecolor=False):
		A=np.arange(x_cord-0.5*length,x_cord+0.5*length,0.001)
		A_=[y_cord-0.5*breadth]*len(A)
		A__=[y_cord+0.5*breadth]*len(A)
		B=np.arange(y_cord-0.5*breadth,y_cord+0.5*breadth,0.001)
		B_=[x_cord-0.5*length]*len(B)
		B__=[x_cord+0.5*length]*len(B)
		ax.plot(A,A_,linecolor,linewidth=linewidth)
		ax.plot(A,A__,linecolor,linewidth=linewidth)
		ax.plot(B_,B,linecolor,linewidth=linewidth)
		ax.plot(B__,B,linecolor,linewidth=linewidth)
		if facecolor :
			ax.fill_between(A,A_,A__,color=facecolor)

rectangle(0,-0.73,0.04,1.7,0.1,'white',facecolor='lightyellow')
rectangle(0,-0.9,3.85,2.05,1,'white')

#FuncAnimation :-
line,=ax.plot([],[],'o',color='cyan',markersize=8)
a1,=ax1.plot([],[],color='deepskyblue',linewidth=2,label='Particles in Left')
a2,=ax1.plot([],[],color='coral',linewidth=2,label='Particles in Right')
ax1.legend(loc=1)
def init():
	line.set_data([],[])
	a1.set_data([],[])
	a2.set_data([],[])
	return line,a1,a2
	
def animate(i):
	s=10#speed of animation
	line.set_data(x[s*i],y[s*i])
	a1.set_data(t[0:s*i],n1[0:s*i])
	a2.set_data(t[0:s*i],n2[0:s*i])
	return line,a1,a2

anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)

plt.show()