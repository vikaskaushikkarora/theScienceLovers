#Mandelbrot Set

import numpy as np
import cmath
import matplotlib.pyplot as plt

# You can take the value 
m=200
real=[]
imaginary=[]
def modulus(z):
	M=((z.real)**2+(z.imag)**2)**0.5
	return M
def f(z):
	w=0
	for i in range (50):
		w = w**(2)+z
	if w > 2 :
		pass
	else :
		for i in range (50,1000):
			w=w**2+z
	if abs(w) < 2 :
		real.append(z.real)
		imaginary.append(z.imag)
	
a=np.zeros((m,m))
b=np.zeros((m,m))
for i in range(m):
	for j in range(m):
		a[:,j]=np.linspace(-1.5,0.5,m)
		b[i,:]=np.linspace(-1,1,m)
c=a+cmath.sqrt(-1)*b

for i in range(m):
	for j in range(m):
		f(c[i,j])	

fig=plt.figure()
ax = fig.add_axes([0.0005,0.26,0.998,0.527])
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('black')
ax.plot(real,imaginary,'o',color='deepskyblue',markersize=2)	
plt.show()