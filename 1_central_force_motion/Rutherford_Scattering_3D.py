#Rutherford Scattering 3D

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


T=950 # Time Window
t=np.linspace(0,11,T)
h=t[1]-t[0] # Step Size

#alpha particles
n=10#number of alpha particles along y
m=10#number of alpha particles along z
alpha_initymin=-1.5
alpha_initymax=1.5
alpha_initzmin=-1.5
alpha_initzmax=1.5

#Nuclie
nuc_miny=-1.5
nuc_maxy=1.5
nuc_minz=-1.5
nuc_maxz=1.5
nuc_numy=6
nuc_numz=6
A=np.linspace(nuc_miny,nuc_maxy,nuc_numy)
B=np.linspace(nuc_minz,nuc_maxz,nuc_numz)

K=1e-2# Strength of Electrostatic Force
def f(x,y,z):
	F=0
	G=0
	L=0
	for i in range(2):
		for j in range(nuc_numy):
			for k in range(nuc_numz):
				F=F+K*(x-i*0.8)*((x-i*0.8)**2+(y-A[j])**2+(z-B[k])**2)**(-1.5)
				G=G+K*(y-A[j])*((x-i*0.8)**2+(y-A[j])**2+(z-B[k])**2)**(-1.5)
				L=L+K*(z-B[k])*((x-i*0.8)**2+(y-A[j])**2+(z-B[k])**2)**(-1.5)
	return [F,G,L]


#State Matrices
x=np.zeros(((T,n,m)))
y=np.zeros(((T,n,m)))
vx=np.zeros(((T,n,m)))
vy=np.zeros(((T,n,m)))
z=np.zeros(((T,n,m)))
vz=np.zeros(((T,n,m)))

# Initial Conditions
for j in range(n):
	for k in range (m):
		x[0,j,k]=-2
		y[0,j,k]=alpha_initymin+j*(alpha_initymax-alpha_initymin)*(n-1)**(-1)
		z[0,j,k]=alpha_initzmin+k*(alpha_initzmax-alpha_initzmin)*(m-1)**(-1)
		vx[0,j,k]=1
		vy[0,j,k]=0
		vz[0,j,k]=0
		

# Iteration for motion for alpha particles
for i in range(T-1):
	for j in range(n):
		for k in range(m):
			p,q,r=f(x[i,j,k],y[i,j,k,],z[i,j,k])
			vx[i+1,j,k]=vx[i,j,k]+h*p
			vy[i+1,j,k]=vy[i,j,k]+h*q
			vz[i+1,j,k]=vz[i,j,k]+h*r
			x[i+1,j,k]=x[i,j,k]+h*vx[i+1,j,k]
			y[i+1,j,k]=y[i,j,k]+h*vy[i+1,j,k]
			z[i+1,j,k]=z[i,j,k]+h*vz[i+1,j,k]

fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')
ax.set_axis_off()
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.set_zlim(-3,3)
ax.set_facecolor('black')
ax.view_init(elev=20 , azim=-70)

a=np.zeros((nuc_numy,nuc_numz))
b=np.zeros((nuc_numy,nuc_numz))
for j in range (nuc_numy):
	a[j,:]=np.linspace(nuc_miny,nuc_maxy,nuc_numy)
	for k in range (nuc_numz):
		b[:,k]=np.linspace(nuc_minz,nuc_maxz,nuc_numz)

a.shape=(nuc_numy*nuc_numz,)
b.shape=(nuc_numy*nuc_numz,)
line,=ax.plot([0]*nuc_numy*nuc_numz,a,b,'o',color='orange',markersize=15)
line1,=ax.plot([0.8]*nuc_numy*nuc_numz,a,b,'o',color='orange',markersize=15,label='Gold Nuclei')

point,=ax.plot([],[],[],'o',color='white',label=r'$\alpha$ - particle')
traj,=ax.plot([],[],[],'o',color='deepskyblue',markersize=0.5,label='Trajectory')
ax.text2D(0.4,0.92,'Rutherford Scattering 3D',ha='center',va='center' ,transform=ax.transAxes,size=25,color='lightyellow')
ax.legend(loc='upper right')
ax.text2D(0.85,0.05,'The Science Lovers',ha='center',va='center' ,transform=ax.transAxes,size=13,color='azure')
ax.legend(loc='upper right')
Xtraj=np.zeros((T,n*m))
Ytraj=np.zeros((T,n*m))
Ztraj=np.zeros((T,n*m))
def animate(i):
	X=x[i,:,:]
	Y=y[i,:,:]
	Z=z[i,:,:]
	X.shape=(n*m,)
	Y.shape=(n*m,)
	Z.shape=(n*m,)
	Xtraj.shape=(T,n*m)
	Ytraj.shape=(T,n*m)
	Ztraj.shape=(T,n*m)
	Xtraj[i,:]=X
	Ytraj[i,:]=Y
	Ztraj[i,:]=Z
	Xtraj.shape=(T*n*m,)
	Ytraj.shape=(T*n*m,)
	Ztraj.shape=(T*n*m,)
	print(Xtraj)
	traj.set_data(Xtraj,Ytraj)
	traj.set_3d_properties(Ztraj,'z')
	point.set_data(X,Y)
	point.set_3d_properties(Z,'z')
	A=ax.view_init(elev=20 , azim=-70-0.5*i)
	return traj,point,A
	
anim = FuncAnimation(fig, animate, frames = T, interval = 20)

plt.show()