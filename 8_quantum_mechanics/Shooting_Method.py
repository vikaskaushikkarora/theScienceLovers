# Shooting Method to solve Time Independent Schroedinger Equation ________________________________

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,cos,exp,pi


L=1e-10  #meters , Well-Length
n=1000 #Space Divisions
charge=1.6e-19  #Coloumbs
m=9.1e-31 #kg , Mass
h=1.0557e-34 #Plank Cosntant
x=np.linspace(-L,L,n) #Space
dx=x[2]-x[1] # Space Step

#Wavefunction
y=np.zeros(n)
y[0]=0
y[1]=0.1

#Potential
v=np.zeros(n)
for i in range(1,n-1):
	if abs(x[i])< L/2 :
		v[i]=-400*charge


#______________________________

#Initiating Loop to find out bound energy solutions

E=-380 #eV ,Inital Energy of electron from which on you want to find bound states

y[n-1]=100000
while abs(y[n-1])>100 and E<0 :
	Ep=E*charge
	for i in range(1,n-1):
		k=((2*m*(Ep-v[i]))*dx**2)*h**(-2)
		y[i+1]=((2-k)*y[i])-y[i-1]
	E=E+0.01



#______________________________

#Plotting 
fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xlim(-1.1*L,1.1*L)
ax.set_xticks([])
ax.set_yticks([])
ax.plot(x,y,color='deepskyblue')
ax.text(0.80, 0.95, "Energy is %0.1f eV"%E, transform=ax.transAxes,size=15,ha='center',va='center',color='yellow')

plt.show()
