# Two Particles in a box
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
from numpy import sin
from numpy import cos

#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568])

#Set x and y limits 
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

#make background black
ax.set_facecolor('black')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')

#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])

#Logo Text :
ax.text(0.85,-1.40,'The Science Lovers',color='white',size=10)


t=np.linspace(0,40,4000)
h=t[2]-t[1]
T=len(t)

P1,=ax.plot([],[],'o',color='cyan',markersize=50)
P2,=ax.plot([],[],'o',color='cyan',markersize=50)


def squ(a,b,l):
		A=np.arange(a-0.5*l,a+0.5*l,0.001)
		A_=[b-0.5*l]*len(A)
		A__=[b+0.5*l]*len(A)
		B=np.arange(b-0.5*l,b+0.5*l,0.001)
		B_=[a-0.5*l]*len(B)
		B__=[a+0.5*l]*len(B)
		ax.plot(A,A_,'b',linewidth=10)
		ax.plot(A,A__,'b',linewidth=10)
		ax.plot(B_,B,'b',linewidth=10)
		ax.plot(B__,B,'b',linewidth=10)

squ(0,0,3.85)





def init():
	P1.set_data([],[])
	P2.set_data([],[])
	
	
	return P1,P2

L=np.zeros(T)
x1=np.zeros(T)
y1=np.zeros(T)
vx1=np.zeros(T)
vy1=np.zeros(T)
x2=np.zeros(T)
y2=np.zeros(T)
vx2=np.zeros(T)
vy2=np.zeros(T)


x1[0]=2*(-1)**(np.random.randint(10))*np.random.rand()
y1[0]=2*(-1)**(np.random.randint(10))*np.random.rand()
vx1[0]=2*(-1)**(np.random.randint(10))*np.random.rand()
vy1[0]=2*(-1)**(np.random.randint(10))*np.random.rand()

x2[0]=2*(-1)**(np.random.randint(10))*np.random.rand()
y2[0]=2*(-1)**(np.random.randint(10))*np.random.rand()
vx2[0]=2*(-1)**(np.random.randint(10))*np.random.rand()
vy2[0]=2*(-1)**(np.random.randint(10))*np.random.rand()

for i in range(0,T-1):
	L[i]=((x2[i]-x1[i])**2+(y2[i]-y1[i])**2)**(0.5)
	
	if (L[i] < 0.4):
		vx1[i+1]=vx2[i]
	elif(x1[i] < -1.75):
		vx1[i+1]=-vx1[i]
	elif(x1[i] > 1.75):
		vx1[i+1]=-vx1[i]
	else :
		vx1[i+1]=vx1[i]
		
	if (L[i] < 0.4):
		vy1[i+1]=vy2[i]
	elif(y1[i] < -1.75):
		vy1[i+1]=-vy1[i]
	elif(y1[i] > 1.75):
		vy1[i+1]=-vy1[i]
	else :
		vy1[i+1]=vy1[i]
		
	
	x1[i+1]=x1[i]+h*vx1[i+1]
	y1[i+1]=y1[i]+h*vy1[i+1]
	
	if (L[i] < 0.4):
		vx2[i+1]=vx1[i]
	elif(x2[i] < -1.75):
		vx2[i+1]=-vx2[i]
	elif(x2[i] > 1.75):
		vx2[i+1]=-vx2[i]
	else :
		vx2[i+1]=vx2[i]
		
	if (L[i] < 0.4):
		vy2[i+1]=vy1[i]
	elif(y2[i] < -1.75):
		vy2[i+1]=-vy2[i]
	elif(y2[i] > 1.75):
		vy2[i+1]=-vy2[i]
	else :
		vy2[i+1]=vy2[i]
	
	
	x2[i+1]=x2[i]+h*vx2[i+1]
	y2[i+1]=y2[i]+h*vy2[i+1]
	
		
def animate(i):
	s=4
	P1.set_data(x1[s*i],y1[s*i])
	P2.set_data(x2[s*i],y2[s*i])
	
	return P1,P2
	

anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)

plt.show()

