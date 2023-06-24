# Precession in the orbit of mercury
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
t=np.arange(0,150,0.01)
dt=t[1]-t[0]
T=len(t)
GMm=6*10**(-3) # Units are in astronomical units instead of meters
b=0.6*10**(-4)
#Einsteinian Equation
x=np.zeros(T)
y=np.zeros(T)
vx=np.zeros(T)
vy=np.zeros(T)
x[0]=0.39 #in AU
y[0]=0
vx[0]=0
vy[0]=np.sqrt(GMm*(0.39)**(-1))
for i in range (T-1):
	vx[i+1]=vx[i]+dt*(-GMm+b*(x[i]**2+y[i]**2)**(-1))*x[i]*(x[i]**2+y[i]**2)**(-1.5)
	x[i+1]=x[i]+dt*vx[i+1]
	vy[i+1]=vy[i]+dt*(-GMm+b*(x[i]**2+y[i]**2)**(-1))*y[i]*(x[i]**2+y[i]**2)**(-1.5)
	y[i+1]=y[i]+dt*vy[i+1]
	
#Newtonian Equations
ax=np.zeros(T)
ay=np.zeros(T)
avx=np.zeros(T)
avy=np.zeros(T)
ax[0]=0.39 #in AU
ay[0]=0
avx[0]=0
avy[0]=np.sqrt(GMm*(0.39)**(-1))
for i in range (T-1):
	avx[i+1]=avx[i]+dt*(-GMm)*ax[i]*(ax[i]**2+ay[i]**2)**(-1.5)
	ax[i+1]=ax[i]+dt*avx[i+1]
	avy[i+1]=avy[i]+dt*(-GMm)*ay[i]*(ax[i]**2+ay[i]**2)**(-1.5)
	ay[i+1]=ay[i]+dt*avy[i+1]
	
#Animating

fig = plt.figure()   
axis = fig.add_axes([0.05,0.05,0.9,0.9])
axis.set_xlim(-0.5,0.5)
axis.set_ylim(-0.55,1.5)
axis.grid(ls='-.',lw=0.75,color='w')
axis.set_xticks([])
axis.set_yticks([])
axis.set_facecolor('black')
line, = axis.plot([], [],'o',color='skyblue')
aline, = axis.plot([], [],color='skyblue',label='Predicted by Einstein')
line2, = axis.plot([], [],'o',color='white') 
aline2, = axis.plot([], [],color='white',label='Predicted by Newton') 
plt.scatter(0.02*np.random.randn(8000,1),0.02*np.random.randn(8000,1),s=0.05,color='orange')
axis.text(-0.04,-0.13,'Sun',size=18,color='orange')
axis.legend(loc=3,frameon='false',facecolor='grey')
axis.text(-0.4,0.65,'Precession in Orbit of Mercury',color='lightyellow',style='oblique',size=25)
axis.text(-0.1,0.58,' ( As predicted by General Relativity )',color='deepskyblue',style='oblique',size=13)
axis.text(0.2,-0.53,'The Science Lovers',color='skyblue',style='oblique',size=13)

def init():
	line.set_data([], []) 
	aline.set_data([], [])
	line2.set_data([], [])
	aline2.set_data([], [])
	return line,aline,line2,aline2


def animate(i):
	line.set_data(x[10*i],y[10*i])
	aline.set_data(x[0:10*(i+1)],y[0:10*(i+1)])
	line2.set_data(ax[10*i],ay[10*i])
	aline2.set_data(ax[0:10*(i+1)],ay[0:10*(i+1)])
	return line,aline,line2,aline2

anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 0.1, blit = True)

plt.show()
