# Collisions : Elastic and Inelastic
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
from numpy import random as rd

#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568],xlim=(-5.5,5.5),ylim=(-5,5),facecolor='black')
ax.set_xticks([])
ax.set_yticks([])
#Logo Text :
ax.text(3.05,-4.90,'The Science Lovers',color='white',size=10)

#Creating Stars in Background
j=np.zeros(200)
k=np.zeros(200)
for i in range(100):
	j[i]=5.3*rd.rand()*(-1)**(rd.randint(1,10))
	k[i]=5*rd.rand()*(-1)**(rd.randint(1,10))
ax.scatter(j,k,s=0.3,color='white')

j_=np.zeros(20)
k_=np.zeros(20)
for i in range(20):
	j_[i]=5.3*rd.rand()*(-1)**(rd.randint(1,10))
	k_[i]=5*rd.rand()*(-1)**(rd.randint(1,10))
ax.scatter(j_,k_,s=2,color='white')

def rectangle(x_cord=0,y_cord=0,length=1,breadth=0.5,linewidth=2,linecolor='blue',facecolor=False):
	    if facecolor :
	    	c=facecolor
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
		ax.fill_between(A,A_,A__,color=c)

rectangle(4,0,2,9,1,'deepskyblue',facecolor='brown')

ax.text(-5,0,'The wall applies force on \nthe ball only horizontally \nand there is no force on \nthe ball in the vertical \ndirection . And thus the \nmomentum in vertical \ndirection is same as before .\nThus the ball is reversed in \nhorizontal and continues  \nalong vertical . ',color='azure',size=20,va='center')

ax.text(4.1,0,'Wall',color='white',size=20,va='center',ha='center')

#Dynamics of collision
t=np.linspace(-10,10,1000)
h=t[2]-t[1]
T=len(t)
x1=np.zeros(T)
y1=np.zeros(T)
y2=np.zeros(T)

a=460
for i in range(a):
	x1[i]=0.006*i
	y1[i]=4.8-0.01*i	
	
for i in range(a,T):
	x1[i]=2.8-0.006*(i-a)
	y1[i]=0.2-0.01*(i-a)
	

#Animation

P,=ax.plot([],[],'o',color='cyan',markersize=25)



def animate(i):
	s=5
	P.set_data(x1[s*i],y1[s*i])
	
	return P,

anim = FuncAnimation(fig, animate, frames = T, interval = 1, blit = True)

plt.show()