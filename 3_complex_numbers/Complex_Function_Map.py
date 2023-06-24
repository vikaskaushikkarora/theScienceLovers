#Complex Function Map _______________________________

import numpy as np
import cmath
import matplotlib.pyplot as plt
J=cmath.sqrt(-1)


#______________________________

def f(z):
	w=z**13
	return w

N=2000
z0=np.linspace(-4,4,N)

a_2=[-2]*N+J*z0
a_1=[-1]*N+J*z0
a=[0]*N+J*z0
a1=[1]*N+J*z0
a2=[2]*N+J*z0

b_2=z0+J*(-2)
b_1=z0+J*(-1)
b=z0
b1=z0+J*(1)
b2=z0+J*(2)



#______________________________

fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_xlim(-50,50)
ax.set_ylim(-50,50)

ax.plot(f(a_2).real,f(a_2).imag,color='coral')
ax.plot(f(a_1).real,f(a_1).imag,color='coral')
ax.plot(f(a).real,f(a).imag,color='coral')
ax.plot(f(a1).real,f(a1).imag,color='coral')
ax.plot(f(a2).real,f(a2).imag,color='coral')

ax.plot(f(b_2).real,f(b_2).imag,color='skyblue')
ax.plot(f(b_1).real,f(b_1).imag,color='skyblue')
ax.plot(f(b).real,f(b).imag,color='skyblue')
ax.plot(f(b1).real,f(b1).imag,color='skyblue')
ax.plot(f(b2).real,f(b2).imag,color='skyblue')


plt.show()