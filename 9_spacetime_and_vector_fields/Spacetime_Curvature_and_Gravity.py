# Spacetime Curvature and Gravitation

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Meshgrid
x = np.arange(-3,3, 0.02)
y = np.arange(-3,3, 0.02)
x,y = np.meshgrid(x,y)

#Radius of Orbit of Earth
#Initially the depth in spacetime is defined
R=np.sqrt((-2)*np.log(4*14**(-1)))

#Create Figure
fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')

#Animation
for i in range (1000):
	ax.set_axis_off()
	ax.set_facecolor('black')
	ax.set_xlim(-1.5,1.5)
	ax.set_ylim(-1.5,1.5)
	ax.set_zlim(-1.2,1)
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])
	#Coordinates of movement for Earth
	x1=R*np.cos(0.02*i)
	y1=R*np.sin(0.02*i)
	#Curvature Surface for 2-D Spacetime
	z = -1.4*np.exp(-0.5*(x**2+y**2))-0.2*np.exp(-15*((x-x1)**2+(y-y1)**2))
	#View Angles
	ax.view_init(elev=40-13*np.sin(0.01*i), azim=-0.08*i)
	#Texts
	ax.text2D(0.7,0.05, 'The Science Lovers', transform=ax.transAxes,size=15,color='yellow')
	#Plotting Sun and Earth
	ax.plot([x1],[y1],[-0.4],'o',color='deepskyblue',markersize=15)
	ax.plot([0],[0],[-0.6],'o',color='orange',markersize=80)
	#Plotting Spacetime
	ax.plot_wireframe(x,y,z,color='azure')
	plt.pause(0.1)
	ax.clear()

plt.show()