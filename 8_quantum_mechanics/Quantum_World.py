# Quantum World ________________________________
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
n=4000
m=50
t=np.linspace(0,0.04,n)
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
	psi[0,j]=np.exp(-300*(x[j]+0.5)**2)*np.exp(i*20*x[j])
	V[j]=0



#Finite Difference Method
for i in range (n-1):
	for j in range (1,m-1):
		psi[i+1,j]=(h*a*b*k**(-2))*(psi[i,j+1]+psi[i,j-1])+(1-h*a*V[j]-2*h*a*b*k**(-2))*psi[i,j]
		
		
		
def random(n,x,z):
	
	# A=Area under the curve of distribution function 
	A=0
	m=len(x)
	h=x[1]-x[0]
	for j in range(m):
		A=A+z[j]*h
	
	# Break up the x axis into small intervals for which total number of random numbers within is constant ......
	frac=np.zeros(m)
	
	# a is an array which contains number of random numbers per division in x axis
	a=np.zeros(m,dtype='int')
	
	for i in range(m):
		frac[i]=(z[i]*h)*A**(-1)
		a[i]=int(n*frac[i])
	b=sum(a)
	
	# array containing random numbers is rd
	rd=np.zeros(b)
	l=0
	for j in range(m):
		for i in range (a[j]):
			rd[l+i]=x[j]+h*np.random.rand()
		#print rd[l+i]
		l=l+a[j]
	return rd
		


#Animation		
fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_xlim(-1,1)
ax.set_ylim(-0.1,1.1)
line,=ax.plot([],[],color='deepskyblue')
point,=ax.plot([],[],'o',color='white',markersize=15)

s=10
def animate(i):
	rd=random(1000,x,abs(psi[s*i,:])**2)
	w=np.random.randint(0,len(rd)-1)
	number=rd[w]
	A=line.set_data(x,abs(psi[s*i,:])**2)
	B=point.set_data(number,[-0.05])
	return line,point
	
anim = FuncAnimation(fig, animate, frames = n, interval = 10, blit = True)

plt.show()