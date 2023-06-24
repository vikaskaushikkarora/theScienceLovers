# Mobius Strip

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.tri import Triangulation

#Adding 3D Figure
fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')
ax.set_facecolor('black')

#Parameters of Mobius Strip
theta = np.linspace(0, 2 * np.pi, 30)
w = np.linspace(-0.05, 0.05, 8)
w, theta = np.meshgrid(w, theta)

phi = 0.5 * theta

r = 1 + w * np.cos(phi)

x = np.ravel(r * np.cos(theta))
y = np.ravel(r * np.sin(theta))
z = np.ravel(w * np.sin(phi))

tri = Triangulation(np.ravel(w), np.ravel(theta))


for i in range (3000):
	ax.set_axis_off()
	ax.view_init(elev=30 , azim=-35+0.2*i)
	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.plot_trisurf(x, y, z, triangles=tri.triangles,cmap='cubehelix', linewidths=0.1)
	ax.text2D(0.24,0.1,r'$ \mathcal{A}$ $\mathcal{Mobius}$ $\mathcal{Strip}$',transform=ax.transAxes,color='lightskyblue',size=40)
	plt.pause(0.1)
	ax.clear()

plt.show()

