# Gradient of a Scaler Field
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-4,4,0.2)
y = np.arange(-4,4,0.2)

x,y = np.meshgrid(x, y)
#Scaler Field
z=np.sin(x)*np.cos(y)
dy , dx= np.gradient(z)

fig=plt.figure()
ax = fig.add_axes([0.0005,0.26,0.998,0.527],facecolor='black')
ax.set_xticks([])

ax.quiver(x,y,dx,dy,color='deepskyblue',scale=4)
ax.contourf(x, y,z,alpha=0.4)
plt.show()