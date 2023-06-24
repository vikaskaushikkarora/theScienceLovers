#Plotting a Complex Number
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

z=1+1j

def plot(z):
	fig=plt.figure()
	ax=fig.add_subplot(111,fc='black',xlim=(-z.real*0.1,z.real*1.3),ylim=(-z.imag*0.1,z.imag*1.1))
	a = ax.plot([0,z.real],[0,z.imag],'ro-')
	b= ax.text(z.real,z.imag,z,size=10,color='white')
	plt.grid(lw=0.5,ls='-.')
	plt.tight_layout()
	return a,b

plot(z)
plt.savefig('a.png')
plt.show()
