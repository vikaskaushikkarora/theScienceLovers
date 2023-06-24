# Electric Field Lines of Dipole

import numpy as np
import matplotlib.pyplot as plt

# Define a function of electric field for a system conatining charged particles

def elec_field(x, y, x_coords=[0], y_coords=[0], charges=[1]):
    Ex = np.zeros_like(x)
    Ey = np.zeros_like(x)
    for x0, y0, q in zip(x_coords, y_coords, charges):
        R = np.sqrt((x - x0)**2 + (y - y0)**2) +1e-4
        Ex += q*(x - x0)/R**3
        Ey += q*(y - y0)/R**3
    return Ex, Ey


x = np.arange(-8,8,0.1)
y = np.arange(-8,8,0.1)
x,y = np.meshgrid(x, y)

Ex, Ey = elec_field(x, y, x_coords=[-1,1], y_coords=[0,0],charges=[1,-1])
Emag =np.sqrt(Ex**2 + Ey**2)
dir_x = Ex/Emag
dir_y = Ey/Emag

#Creating Figure
fig=plt.figure()
ax = fig.add_axes([0.0005,0.26,0.998,0.527],facecolor='black')
ax.set_xticks([])

ax.contourf(x, y,np.log10(Emag), cmap='cool')
ax.streamplot(x, y, Ex/Emag, Ey/Emag, color='black',density=1,linewidth=0.5,arrowsize=0.8)
plt.show()