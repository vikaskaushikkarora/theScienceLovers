# Streamline Flow of a Fluid

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2.2,0.1)
y = np.arange(0,2.2,0.1)

x,y = np.meshgrid(x, y)
u = np.cos(x)
v = np.sin(y)

fig=plt.figure()
ax = fig.add_axes([0.0005,0.26,0.998,0.527],facecolor='black')
ax.set_xticks([])

ax.axis([0.5,2.1,0,2])
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.streamplot(x,y,u,v, density = 2,color='deepskyblue',linewidth=0.5,arrowsize=0.8)

plt.show()