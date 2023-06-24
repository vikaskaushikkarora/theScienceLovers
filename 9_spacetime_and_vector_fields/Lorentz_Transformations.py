# Lorentz Transformation of a World - Line _______________________________

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  


#______________________________

c=1 # speed of light
beta=0.7 # beta = v/c , where we have v = speed of the moving frame S'
G=(1-beta**2)**(-0.5) # Gamma Factor


#______________________________

# S - Frame :-
t=np.arange(0,1,0.01)
N=len(t)
x=0.3+0.1*t

#S' - Frame :-
X=G*(x-beta*c*t)
T=G*(t-x*beta*c**(-1))


#______________________________

#Animation :-

fig=plt.figure()
ax = fig.add_axes([0.0005,0.251,0.998,0.47])
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-1,1)
ax.set_ylim(-0.5,1.5)

ax.text(0,1.35,'LORENTZ TRANSFORMATION',color='lightcoral',size=30,ha='center',va='center',bbox=dict(boxstyle='round',fc='grey',alpha=0.4,ec='red'))
ax.quiver(0,0,1,0,color='white',scale=3,width=0.004)
ax.quiver(0,0,0,1,color='white',scale=3,width=0.004)
ax.text(0,0.8,'t',color='white',size=20,ha='center',va='center')
ax.text(0.7,0,'x',color='white',size=20,ha='center',va='center')

point, = ax.plot([], [],'o',color='skyblue',markersize=10)  
point1, = ax.plot([], [],'o',color='coral',markersize=10)
line,=ax.plot([],[],'-',color='skyblue',linewidth=2,label='Stationary Frame')
line1,=ax.plot([],[],'-',color='coral',linewidth=2,label='Moving Frame')
ax.legend(loc=3)

def animate(i):
	point.set_data(x[i],t[i]) 
	point1.set_data(X[i],T[i])
	line.set_data(x[0:i],t[0:i])
	line1.set_data(X[0:i],T[0:i])
	return line,line1,point,point1

anim = FuncAnimation(fig, animate, frames =N, interval = 50, blit = True)

plt.show()