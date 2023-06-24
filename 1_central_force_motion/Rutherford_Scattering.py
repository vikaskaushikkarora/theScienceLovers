# Rutherford Scatttering 2 D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

T=250 # Time Window
t=np.linspace(0,T,5000)
h=t[1]-t[0] # Step Size
n=100#number of alpha particles

# Create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568],xlim=(-5,10),ylim=(-10,10),facecolor='black')
ax.set_xticks([])
ax.set_yticks([])
ax.text(2.5,8,'Rutherford Scattering',ha='center',va='center',color='azure',size=30)
# Placing Nuclie
A=8 # number of rows of nuclie
B=4 # number of columns of nuclie
a=np.linspace(0,1,B)
b=np.linspace(-4,4,A+1)

for i in range (A+1):
	for j in range (B):
		ax.plot(a[j],b[i],'o',color='orange',markersize=7)

k=5e-5 # Strength of Electrostatic Force
def f(x,y):
	F=0
	for i in range(A+1):
		for j in range(B):
			F=F+k*(x-a[j])*((x-a[j])**2+(y-b[i])**2)**(-1.5)
	return F
def g(x,y):
	G=0
	for i in range(A):
		for j in range(B):
			G=G+k*(y-a[j])*((x-a[j])**2+(y-b[i])**2)**(-1.5)
	return G
	
x=np.zeros((T,n))
y=np.zeros((T,n))
vx=np.zeros((T,n))
vy=np.zeros((T,n))

# Initial Conditions
for j in range(n):
	y[0,j]=5-10*j*(n)**(-1)
	x[0,j]=-3
	vx[0,j]=1
	vy[0,j]=0

# Iteration for motion for alpha particles
for i in range(T-1):
	for j in range(n):
		vx[i+1,j]=vx[i,j]+h*f(x[i,j],y[i,j])
		vy[i+1,j]=vy[i,j]+h*g(x[i,j],y[i,j])
		x[i+1,j]=x[i,j]+h*vx[i+1,j]
		y[i+1,j]=y[i,j]+h*vy[i+1,j]

#Animation

P,=ax.plot([],[],'o',color='deepskyblue',markersize=3)
Q,=ax.plot([],[],'o',color='white',markersize=0.35)

def animate(i):
	s=1
	P.set_data(x[s*i],y[s*i])
	Q.set_data(x[0:s*i],y[0:s*i])
	return P,Q,

anim = FuncAnimation(fig, animate, frames = T, interval = 1, blit = True)

plt.show()