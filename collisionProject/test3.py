# Collisions : Elastic and Inelastic
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
ax.text(-4.8,3,'In non-elastic collisions , the \nkinetic energy is lost in form of \nheat and sound energy. ',color='lightyellow',size=28)
ax.text(-0.2,-0.5,'Perfectly Elastic Collision',color='lightskyblue',size=20)
ax.text(-0.7,-4,'Perfectly Inelastic Collision',color='lightskyblue',size=20)

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
t=np.linspace(-10,10,1700)
h=t[2]-t[1]
T=len(t)
x1=np.zeros(T)
x2=np.zeros(T)
y1=np.zeros(T)
y2=np.zeros(T)
xa1=np.zeros(T)
xa2=np.zeros(T)
ya1=np.zeros(T)
ya2=np.zeros(T)


a=480
for i in range(a):
	x1[i]=-5+0.01*i
	x2[i]=0.2
	y1[i]=1
	y2[i]=1
	xa1[i]=-5+0.01*i
	xa2[i]=0.2
	ya1[i]=-2.5
	ya2[i]=-2.5
	
	
for i in range(a,T):
	x1[i]=-0.2
	x2[i]=0.2+0.01*(i-a)
	y1[i]=1
	y2[i]=1
	xa1[i]=-0.2+0.005*(i-a)
	xa2[i]=0.3+0.005*(i-a)
	ya1[i]=-2.5
	ya2[i]=-2.5
	

#Animation

P,=ax.plot([],[],'o',color='cyan',markersize=25)
Q,=ax.plot([],[],'o',color='coral',markersize=25)
R,=ax.plot([],[],'o',color='cyan',markersize=25)
S,=ax.plot([],[],'o',color='coral',markersize=25)


def animate(i):
	s=10
	P.set_data(x1[s*i],y1[s*i])
	Q.set_data(x2[s*i],y2[s*i])
	R.set_data(xa1[s*i],ya1[s*i])
	S.set_data(xa2[s*i],ya2[s*i])
	if ( i > ( a*(s)**(-1)) and i < (a*s**(-1) + 20) ):
		A=ax.text(-0.3,-2.1,'BOOM !',color='orange',size=20)
	else:
		A=ax.text(10,10,' ')
	
	return P,Q,R,S,A

anim = FuncAnimation(fig, animate, frames = T, interval = 1, blit = True)

plt.show()