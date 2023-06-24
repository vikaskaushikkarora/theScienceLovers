# Visuallize  Complex Functions as Colormaps ________________________________
import numpy as np
import matplotlib.pyplot as plt
import cmath
from mpl_toolkits.mplot3d import Axes3D
from numpy import sin , cos , exp , pi , arctan , log
J=cmath.sqrt(-1)


#______________________________

def f(z):
	w=0.5*z**2
	return w

N=30
z=np.zeros((N,N),dtype=np.complex)

for i in range(N):
	for j in range(N):
		x=1.3
		z[i,j]=(-x+i*2*x*N**(-1))+J*(-x+j*2*x*N**(-1))

Z=f(z)

X =np.zeros(N*N)
Y =np.zeros(N*N)
A =np.zeros(N*N)
B =np.zeros(N*N)

for i in range (N*N):
	X[i]=z.real[i/N,i%N]
	Y[i]=z.imag[i/N,i%N]
	A[i]=(Z.real[i/N,i%N]**2+Z.imag[i/N,i%N]**2)**0.5
	B[i]=arctan(Z.imag[i/N,i%N]*(Z.real[i/N,i%N])**(-1))


#______________________________

fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')
ax.set_facecolor('black')
ax.set_axis_off()
p=ax.scatter(X,Y,A,c=B,s=10)

ax.quiver(-2,0,0,4,0,0,color='white',arrow_length_ratio=0.04)
ax.quiver(0,-2,0,0,4,0,color='white',arrow_length_ratio=0.04)
ax.text(2,0,0,'Real',color='lightcoral',size=13)
ax.text(0,2,0,'Imag',color='deepskyblue',size=13)
plt.savefig('a.png')
plt.show()
