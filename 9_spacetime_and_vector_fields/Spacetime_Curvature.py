# Spacetime Curvature

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Meshgrid
x = np.arange(-3,3, 0.002)
y = np.arange(-3,3, 0.002)
x,y = np.meshgrid(x,y)

#Defining Function for spacetime
z = -0.5*np.exp(-20*((x)**2+(y+2)**2))-1.5*np.exp(-15*((x)**2+(y)**2))-50*np.exp(-100*((x)**2+(y-2)**2))
	
#Figure Properties
fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')
ax.set_axis_off()
ax.set_facecolor('black')
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)
ax.set_zlim(-1.2,1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.view_init(elev=15,azim=50)

#Texts
ax.text2D(0.07,0.05, 'The Science Lovers', transform=ax.transAxes,size=15,color='yellow')
ax.text2D(0.07,0.9, "CURVATURE IN SPACETIME", transform=ax.transAxes,size=25,color='white')

#Plotting Sun , Earth and Blackhole
ax.plot([0],[0],[-1.2],'o',color='orange',markersize=15,label='Sun')
ax.plot([0],[-2],[-0.4],'o',color='deepskyblue',markersize=10,label='Earth')
ax.plot([0],[2],[-1.5],'o',color='black',markersize=10,label='Blackhole')
ax.legend(loc=1)

#Plotting Spacetime
ax.plot_surface(x,y,z,antialiased=False,alpha=0.5)

plt.show()