# A Vector Field with Postive Curl

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-5,5.5,0.5)
y=np.arange(-5,5.5,0.5)
x,y=np.meshgrid(x,y)

u = -y*(x**2+y**2)**(-0.5)
v = x*(x**2+y**2)**(-0.5)

color_array = np.sqrt((x/2)**2 + (y/2)**2)

fig=plt.figure()
ax = fig.add_axes([0.0005,0.26,0.998,0.527],facecolor='black')
ax.set_xticks([])

ax.quiver(x,y,u,v,color_array,color='deepskyblue',scale=40)

plt.show()