# Collisions : Equal Mass Collision
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
ax.text(-4.5,2,'Equal masses when collide \nelastically , just exchange the \nvelocities .',color='lightyellow',size=30)

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


#Dynamics of the two bodies
t=np.linspace(-10,10,1100)
h=t[2]-t[1]
T=len(t)
x1=np.zeros(T)
x2=np.zeros(T)
y1=np.zeros(T)
y2=np.zeros(T)

a=280
for i in range(a):
	x1[i]=-5+0.02*i
	x2[i]=4-0.01*i
	y1[i]=0.
	y2[i]=0.
for i in range(a,T):
	x1[i]=0.8-0.01*(i-a)
	x2[i]=1.2+0.02*(i-a)
	y1[i]=0
	y2[i]=0
				
#Animation

P,=ax.plot([],[],'o',color='skyblue',markersize=25)
Q,=ax.plot([],[],'o',color='coral',markersize=25)



def animate(i):
	s=5
	P.set_data(x1[s*i],y1[s*i])
	Q.set_data(x2[s*i],y2[s*i])
	if i < 280*(s)**(-1) :
		A=ax.text(x1[s*i]-0.3,y1[s*i]-1,'2 m/s',ha='center',color='white',size=20)
		B=ax.text(x2[s*i]+0.3,y2[s*i]-1,r'1 m/s',ha='center',color='white',size=20)
	else :
		A=ax.text(x1[s*i]-0.3,y1[s*i]-1,'1 m/s',ha='center',color='white',size=20)
		B=ax.text(x2[s*i]+0.3,y2[s*i]-1,'2 m/s',ha='center',color='white',size=20)
	
	return P,Q,A,B

anim = FuncAnimation(fig, animate, frames = T, interval = 1, blit = True)

plt.show()