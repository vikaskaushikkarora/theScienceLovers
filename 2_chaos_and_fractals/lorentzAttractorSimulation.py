# Lorentz Attractor Simulation

#import libraries
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def lorenz(x, y, z, s=10, r=28, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.002
num_steps = 40000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)
    
    
# Simulation :-

fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')
ax.set_axis_off()
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlim(-22,22)
ax.set_ylim(-22,22)
ax.set_zlim(15,53)
ax.text2D(0.5,0.93,'The Butterfly Effect',transform=ax.transAxes,va='center',ha='center',color='lightyellow',size=35)
ax.text2D(0.85,0.05,'The Science Lovers',transform=ax.transAxes,va='center',ha='center',color='azure',size=10)


line,=ax.plot([],[],[],'o',markersize=7,color='white')
traj,=ax.plot([],[],[],'-',color='deepskyblue',linewidth=1)
def animate(i):
	s=2
	line.set_data([xs[s*i]],[ys[s*i]])
	line.set_3d_properties([zs[s*i]],'z')
	traj.set_data(xs[0:s*i],ys[0:s*i])
	traj.set_3d_properties(zs[0:s*i],'z')
	A=ax.view_init(elev=20 , azim=-130-0.05*s*i)
	#B=ax.text2D(0.4,0.9,'Text Here', transform=ax.transAxes,size=20,color='yellow')
	return line,traj,A
	
anim = FuncAnimation(fig, animate, frames = 20000, interval = 10)



plt.show()
