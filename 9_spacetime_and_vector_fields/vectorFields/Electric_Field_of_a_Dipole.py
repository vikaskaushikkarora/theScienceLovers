# Time Varying Electric Field Lines of Dipole

import numpy as np
import matplotlib.pyplot as plt

# Define a function of electric field for a system conatining charged particles

def elec_field(x, y, x_coords=[0], y_coords=[0], charges=[1]):
    Ex = np.zeros_like(x)
    Ey = np.zeros_like(x)
    for x0, y0, q in zip(x_coords, y_coords, charges):
        R = np.sqrt((x - x0)**2 + (y - y0)**2) +1
        Ex += q*(x - x0)/R**3
        Ey += q*(y - y0)/R**3
    return Ex, Ey


x = np.arange(-8,8,0.5)
y = np.arange(-8,8,0.5)
x,y = np.meshgrid(x, y)


fig=plt.figure()
ax = fig.add_axes([0.0005,0.26,0.998,0.527],facecolor='black')

for i in range (1000):
	x1=-2*np.cos(0.01*i)
	x2=2*np.cos(0.01*i)
	y1=2*np.sin(0.01*i)
	y2=-2*np.sin(0.01*i)
	Ex, Ey = elec_field(x, y,x_coords=[x1,x2], y_coords=[y1,y2],charges=[1,-1])
	Emag =np.sqrt(Ex**2 + Ey**2)
	dir_x = Ex/Emag
	dir_y = Ey/Emag
	ax.set_xlim(-8,7.5)
	ax.set_ylim(-8,7.5)
	ax.set_xticks([])
	ax.contourf(x, y,np.log10(Emag), cmap='cool')
	ax.quiver(x, y, Ex/Emag, Ey/Emag, color='black',scale=35)
	ax.plot(x1,y1,'o',color='red',markersize=10,label='Positive charge')
	ax.plot(x2,y2,'o',color='blue',markersize=10,label='Negative charge')
	ax.text(0,6.5,'Electric Field of A Dipole',color='yellow',size=30,ha='center',va='center')
	ax.text(5,-7.5,'The Science Lovers',color='azure',size=13,ha='center',va='center')
	ax.legend(loc=3)
	plt.pause(0.1)
	ax.clear()
plt.show()