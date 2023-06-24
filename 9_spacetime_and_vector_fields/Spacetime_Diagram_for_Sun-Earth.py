#import varoius modules and libraries
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')
ax.set_facecolor('black')


theta = np.linspace(-4 * np.pi, 4 * np.pi, 400)
z = np.linspace(-2, 2, 400)
x = 5* np.sin(theta)
y = 5* np.cos(theta)
x0 = 0.001* np.sin(theta)
y0 = 0.001* np.cos(theta)
X = np.arange(-7, 7, 1)
Y = np.arange(-7, 7, 1)
X, Y = np.meshgrid(X, Y)
Z=(X*Y)**(0)
for i in range (400):
	ax.set_axis_off()
	ax.set_xlim(-5,5)
	ax.set_ylim(-5,5)
	ax.set_zlim(-2.1,2.1)
	ax.text2D(0.07,0.85, 'Spacetime Diagram for 2D Universe', transform=ax.transAxes,size=25,color='yellow')
	ax.text2D(0.07,0.02, "Take the photos of 2D universe at different times . Stack \nthe photos one over other vertically and you will get the \nspacetime diagram for 2D universe . For 3D universe , it \nwill be four dimensional and that we can't intute .", transform=ax.transAxes,size=15,color='white')
	
	ax.view_init(elev=5 , azim=-35+i*0.5)
	ax.plot3D(x0[0:i],y0[0:i],z[0:i],'o',color='orange',markersize=10,label='Sun')
	ax.plot3D(x[0:i],y[0:i],z[0:i],'o',color='skyblue',label='Earth')
	ax.legend()
	ax.plot_surface(X, Y, Z*z[i] ,rstride=1)
	plt.pause(0.1)
	ax.clear()

plt.show()