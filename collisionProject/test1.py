# Collisions : Momentum and Kinetic Energy
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
from numpy import random as rd

#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568],xlim=(-5.3,5.3),ylim=(-5,5),facecolor='black')
ax.set_xticks([])
ax.set_yticks([])
#Logo Text :
ax.text(3.05,-4.90,'The Science Lovers',color='white',size=10)
ax.text(-4,-4,r'Momentum = $m.\vec v$',color='deepskyblue',size=20)
ax.arrow(0.1,-3.9,0.4,0,color='lightyellow',width=0.05,head_width=0.15,head_length=0.15)
ax.text(-4,-4.7,r'Kinetic Energy = $\frac{1}{2}mv^2$',color='deepskyblue',size=20)


ax.text(-4.5,0.3,'Momentum is the oomph \nof the object to move in a \nspecific direction .\nKinetic Energy is the energy \nassociated with the motion \nof the object.',color='azure',size=25)

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


#Dynamics of collision
t=np.linspace(-10,10,1800)
h=t[2]-t[1]
T=len(t)
x1=np.zeros(T)
y1=np.zeros(T)


for i in range(T):
	y1[i]=4-20*np.sin(0.0004*i)**2
	x1[i]=-4.5+9*np.sin(0.002*i*np.exp(-0.00001*i))
	

#Animation

P,=ax.plot([],[],'o',color='cyan',markersize=25)

def animate(i):
	s=5
	P.set_data(x1[s*i],y1[s*i])
	A=ax.arrow(x1[s*i],y1[s*i],40*(x1[s*i]-x1[s*i-1]),40*(y1[s*i]-y1[s*i-1]),width=0.05,head_width=0.15,head_length=0.15,color='lightyellow')
	return P,A

anim = FuncAnimation(fig, animate, frames = T, interval = 1, blit = True)

plt.show()