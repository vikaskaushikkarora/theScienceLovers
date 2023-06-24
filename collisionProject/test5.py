# Collisions : Unequal Mass collisions
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
ax.text(-4.8,2.5,'When smaller object collides with a \nbigger one , it reflects back with extra \nspeed of twice of the bigger object .',color='lightyellow',size=25)


P,=ax.plot(-4,-2.7,'o',color='skyblue',markersize=25,alpha=0.7)
Q,=ax.plot(-4,-3.8,'o',color='coral',markersize=70,alpha=0.7)
ax.text(-3.5,-2.7,'1 Kg',color='white',size=13,va='center')
ax.text(-3,-3.8,'100 Kg',color='white',size=20,va='center')

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
t=np.linspace(-10,10,1600)
h=t[2]-t[1]
T=len(t)
x1=np.zeros(T)
x2=np.zeros(T)
y1=np.zeros(T)
y2=np.zeros(T)

a=270
for i in range(a):
	x1[i]=-5+0.025*i
	x2[i]=4-0.005*i
	y1[i]=0.
	y2[i]=0.
for i in range(a,T):
	x1[i]=1.7-0.035*(i-a)
	x2[i]=2.65-0.005*(i-a)
	y1[i]=0
	y2[i]=0
				
#Animation

P,=ax.plot([],[],'o',color='skyblue',markersize=25,alpha=0.7)
Q,=ax.plot([],[],'o',color='coral',markersize=70,alpha=0.7)



def animate(i):
	s=5
	P.set_data(x1[s*i],y1[s*i])
	Q.set_data(x2[s*i],y2[s*i])
	if i > 0.5*T*s**(-1) :
		R=ax.text(1.85,-3.8,'Try doing it with a \ntennis ball and a football .',color='white',size=20,va='center',ha='center',bbox=dict(boxstyle='round',fc='lightskyblue',alpha=0.8,ec='lightyellow'))
	else :
		R=ax.text(20,20,' ')
		
	if i < 280*(s)**(-1) :
		A=ax.text(x1[s*i]-0.3,y1[s*i]-1,'2 m/s',ha='center',color='white',size=20)
		B=ax.text(x2[s*i],y2[s*i]-1.2,r'1 m/s',ha='center',color='white',size=20)
	else :
		A=ax.text(x1[s*i]-0.3,y1[s*i]-1,'4 m/s',ha='center',color='white',size=20)
		B=ax.text(x2[s*i],y2[s*i]-1.2,'1 m/s',ha='center',color='white',size=20)
	
	return P,Q,A,B,R

anim = FuncAnimation(fig, animate, frames = T, interval = 1, blit = True)

plt.show()