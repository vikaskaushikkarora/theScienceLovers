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
	
ax.text(1.5,-4.7,'The Science Lovers',color='white',size=15)
ax.text(0,2.5,'Thus when some objects are colliding and no outer factors are intervening the process , following things are conserved :',wrap=True,va='center',ha='center',size=20,color='deepskyblue')
ax.text(-5,-1,'Total Linear Momentum : Always \n\nTotal Energy : Always \n\nTotal Angular Momentum : Always \n\nKinetic Energy : Only for Elastic Collisions  ',wrap=False,va='center',size=22,color='seagreen')

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
	j_[i]=5.5*rd.rand()*(-1)**(rd.randint(1,10))
	k_[i]=5*rd.rand()*(-1)**(rd.randint(1,10))
ax.scatter(j_,k_,s=2,color='white')


plt.show()