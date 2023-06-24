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
ax.text(3.05,-4.50,'The Science Lovers',color='white',size=10)
ax.text(0,-3,'Actually there is another quantity which is also \nconserved mostly when collision causes \nroatations : \nAngular Momentum (Oomph to rotate )',va='center',ha='center',size=20,color='azure')
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
T=1350
x1=np.zeros(T)
y1=np.zeros(T)

a=240
for i in range(a):
	x1[i]=-2+0.01*i
	y1[i]=3
	
for i in range(a,T):
	x1[i]=-2+0.01*a-0.004*(i-a)
	y1[i]=3
	

#Animation

P,=ax.plot([],[],'o',color='cyan',markersize=30)


def animate(i):
	s=5
	P.set_data(x1[s*i],y1[s*i])
	if s*i <= a  :
		Q=plt.text(1,1,'                                          ',size=20,rotation=90,wrap=False,ha='center',va='center',color='magenta',style='oblique',withdash=True,bbox=dict(boxstyle='round',fc='lightyellow',ec='red'))
	else :
		Q=plt.text(1+0.005*(s*i-a),1,'                                          ',size=20,rotation=90-0.5*(s*i-a),wrap=False,ha='center',va='center',color='magenta',style='oblique',withdash=True,bbox=dict(boxstyle='round',fc='lightyellow',ec='red'))
	return P,Q

anim = FuncAnimation(fig, animate, frames = T, interval = 1, blit = True)

plt.show()