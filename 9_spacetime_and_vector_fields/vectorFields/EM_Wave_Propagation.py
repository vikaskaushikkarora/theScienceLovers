# E M Wave Propagation

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Create 3D Meshgrid
x = np.linspace(-3,3,50)
y = np.linspace(-3,3,1)
z = np.arange(-1,0,1)
x,y,z=np.meshgrid(x,y,z)


#Animation
fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')

for i in range(2000):
	ax.set_facecolor('black')
	ax.set_axis_off()
	ax.set_xlim(-1,4)
	ax.set_ylim(-3,3)
	ax.set_zlim(-2,0)
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])
	ax.view_init(elev=20 , azim=-120)
	
	#Define Vector Field
	k=2
	omega=0.1
	u = 0
	v = 0
	w= 0.8*np.sin(k*x-omega*i)
	
	#Draw Vector Field
	ax.quiver(x,y,z,u,v,w,color='deepskyblue',length=1,lw=1,normalize=False,arrow_length_ratio=0.1)
	ax.quiver(x,y,z,u,2.4*w,v,color='yellow',length=1,lw=1,arrow_length_ratio=0.05)
	
	#Draw Axies 
	ax.quiver(-3.1,-3,-1,6.7,0,0,color='red',arrow_length_ratio=0.025)
	ax.quiver(-3.1,-3,-1,0,-2,0,color='lightyellow',arrow_length_ratio=0.06)
	ax.quiver(-3.1,-3,-1,0,0,1,color='skyblue',arrow_length_ratio=0.2)
	
	#Add 3D Text
	ax.text(-3.1,-3,0.15,r'$\vecE$', color='deepskyblue',size=20)
	ax.text(-3.3,-5.83,-1,r'$\vecB$', color='yellow',size=20)
	
	#Add 2D Text
	ax.text2D(0.52,0.83,"An Electromagnetic Wave", transform=ax.transAxes,size=30,color='white',ha='center',va='center')
	ax.text2D(0.52,0.75,"( Plane Polarized )", transform=ax.transAxes,size=20,color='lightyellow',ha='center',va='center')
	ax.text2D(0.85,0.12,"The Science Lovers", transform=ax.transAxes,size=15,color='lightyellow',ha='center',va='center')
	
	plt.pause(0.1)
	ax.clear()

plt.show()