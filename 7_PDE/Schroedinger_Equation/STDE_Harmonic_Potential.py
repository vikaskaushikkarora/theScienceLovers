# STDE_Harmonic_Potential ________________________________
#Libraries
import numpy as np
import cmath
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#Constants
i=cmath.sqrt(-1)
plank_constant=1
mass=1
a=i*plank_constant**(-1)
b=plank_constant**2*(2*mass)**(-1)


#Arrays
n=12000
m=100
t=np.linspace(0,0.15,n)
h=t[2]-t[1]
x=np.linspace(-1,1,m)
k=x[2]-x[1]
psi=np.zeros((n,m),dtype=np.complex)



# Boundary Conditions ( The wavefunction vanishes at boundaries )
psi[:,0]=0
psi[:,m-1]=0



#Defining Potential and Initial Condition
V=np.zeros(m) 
for j in range(m):
	psi[0,j]=np.exp(-50*(x[j])**2)*np.exp(i*10*x[j])
	V[j]=800*x[j]*x[j]



#Finite Difference Method
for i in range (n-1):
	for j in range (1,m-1):
		psi[i+1,j]=(h*a*b*k**(-2))*(psi[i,j+1]+psi[i,j-1])+(1-h*a*V[j]-2*h*a*b*k**(-2))*psi[i,j]
		


#Animation		
fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_xlim(-1,1)
ax.set_ylim(-0.1,1.1)
line,=ax.plot([],[],color='deepskyblue')


s=10
def animate(i):
	A=line.set_data(x,abs(psi[s*i,:])**2)
	return line,
	
anim = FuncAnimation(fig, animate, frames = n, interval = 10, blit = True)

plt.show()