#3 D Vector field

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-3,4,1)
y = np.arange(-3,4, 1)
z = np.arange(-3,4, 1.5)

x,y,z=np.meshgrid(x,y,z)

u = x*(x**2+y**2+z**2)**(-0.5)
v = y*(x**2+y**2+z**2)**(-0.5)
w= z*(x**2+y**2+z**2)**(-0.5)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')

for i in range(200):
	ax.set_facecolor('black')
	ax.set_axis_off()
	ax.set_xlim(-3,3)
	ax.set_ylim(-3,3)
	ax.set_zlim(-5,5)
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])
	ax.view_init(elev=20 , azim=-35-0.8*i)
	ax.quiver(x,y,z,u,v,w,cmap='Reds',length=1,lw=1,normalize=False)
	plt.pause(0.1)
	ax.clear()
plt.show()