# Projectile Motion ( Ball in a Pit) _______________________________

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#______________________________


t=np.arange(0,30,0.005) #time
T=len(t)
h=t[1]-t[0] #stepsize
#coordinates for position and velocity
x=np.zeros(T) 
y=np.zeros(T)
vx=np.zeros(T)
vy=np.zeros(T)
#initial conditions
vx[0]=1.7
vy[0]=0
x[0]=0
y[0]=5

#______________________________


#Kinematics of Motion
for i in range(T-1):
	if ( x[i] > 4 and x[i] < 4.1 and y[i] < 3 and vx[i]> 0 ): #collision on surface
		vx[i+1]=-0.8*vx[i]
	elif ( x[i] <1 and x[i] > 0.9 and y[i] < 3 and vx[i] < 0): #collision on surface
		vx[i+1]=-0.8*vx[i]
	elif (y[i] < 0.03 and vy[i] < 0.03 and vy[i] > -0.03 ): #friction while moving on the lowest surface 
		vx[i+1]=vx[i]*np.exp(-0.3*h)
	else:
		vx[i+1]=vx[i]
		
	if ( x[i] < 1 and y[i] < 3 and y[i] > 2.9 and vy[i] < 0 ): #collision on the surface
		vy[i+1]=-0.7*vy[i]
	elif ( x[i] > 4 and y[i] < 3 and y[i] >2.9 and vy[i] <0 ): #collision on the surface
		vy[i+1]=-0.7*vy[i]
	elif ( x[i] < 4 and x[i] > 1 and y[i] < 0 and vy[i] < 0 ): #collision on the surface
		vy[i+1]=-0.8*vy[i]
	else:
		vy[i+1]=vy[i]-2*h #effect of gravity
	
	#Equation of motion
	x[i+1]=x[i]+vx[i]*h
	y[i+1]=y[i]+vy[i]*h
	
#______________________________


#Animation
fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_xlim(-0.2,5.2)
ax.set_ylim(-0.7,5.5)
ax.plot([0,0.9],[2.9,2.9],'-',color='lightyellow')
ax.plot([0.9,0.9],[2.9,-0.1],'-',color='lightyellow')
ax.plot([0.9,4.1],[-0.1,-0.1],'-',color='yellow',linewidth=3)
ax.plot([4.1,4.1],[2.9,-0.1],'-',color='lightyellow')
ax.plot([4.1,5],[2.9,2.9],'-',color='lightyellow')
ax.text(4.4,-0.6,'The Science Lovers',color='white',size=13,ha='center')


line,=ax.plot([],[],'o',color='deepskyblue',markersize=15)
	
s=1
def animate(i):
	A=line.set_data(x[s*i],y[s*i])
	return line,
	
anim = FuncAnimation(fig, animate, frames = T, interval = 50, blit = True)

plt.show()