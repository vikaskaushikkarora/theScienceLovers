# Visuallize  Complex Functions as Vectors ________________________________
import numpy as np
import matplotlib.pyplot as plt
import cmath
from numpy import sin , cos , exp , pi 
J=cmath.sqrt(-1)


#______________________________

def f(z):
	w=z**2
	return w

N=30
z=np.zeros((N,N),dtype=np.complex)

for i in range(N):
	for j in range(N):
		z[i,j]=(-5+i*10*N**(-1))+J*(-5+j*10*N**(-1))

Z=f(z)


#______________________________

fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

x=z.real
y=z.imag
u=Z.real
v=Z.imag
ax.quiver(x,y,u,v,color='deepskyblue')

plt.show()