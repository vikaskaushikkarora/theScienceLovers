# Visualling Quantum Wave Function ( Barrier - Potential ) ________________________________
#Libraries
import numpy as np
import cmath
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Constants
from numpy import sin, cos , exp , pi , linspace
j=cmath.sqrt(-1)
J=j
plank_constant=1
mass=1
a=j*plank_constant**(-1)
b=plank_constant**2*(2*mass)**(-1)

#Arrays
n=5000
m=150
t=np.linspace(0,0.013,n)
h=t[2]-t[1]
T=len(t)
x=np.linspace(-1,1,m)
k=x[2]-x[1]
psi=np.zeros((n,m),dtype=np.complex)



#______________________________

# Boundary Conditions ( The wavefunction vanishes at boundaries )
psi[:,0]=0
psi[:,m-1]=0


#Defining Potential and Initial Condition
V=np.zeros(m) 
for j in range(int(0.4*m)):
	psi[0,j]=exp(-600*(x[j]-0.3)**2)*exp(-J*50*x[j])
	V[j]=0
for j in range(int(0.4*m),int(0.4*m)+50):
	psi[0,j]=exp(-600*(x[j]-0.3)**2)*exp(-J*50*x[j])
	V[j]=300
for j in range(int(0.4*m)+50,m):
	psi[0,j]=exp(-600*(x[j]-0.3)**2)*exp(-J*50*x[j])
	V[j]=0


#Finite Difference Method
for i in range (n-1):
	for j in range (1,m-1):
		psi[i+1,j]=(h*a*b*k**(-2))*(psi[i,j+1]+psi[i,j-1])+(1-h*a*V[j]-2*h*a*b*k**(-2))*psi[i,j]

		

#______________________________

#Creating a function to plot random number within a bound interval according to the given distribution		
def random(n,x,z):
	
	# A=Area under the curve of distribution function 
	A=0
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

		
		
#_____________________________		
#Animation
fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')
ax.view_init(elev=20 , azim=70)
s=15
for i in range (int(T*s**(-1))):
	ax.set_facecolor('black')
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])
	ax.set_axis_off()
	ax.view_init(elev=20 , azim=80+0.005*s*i)
	
	ax.set_xlim(-0.85,0.75)
	ax.set_ylim(-0.8,0.8)
	ax.set_zlim(-0.5,1.3)
	ax.quiver(-1.1,0,0,1.5,0,0,color='white',length=1.5,arrow_length_ratio=0.04)
	ax.quiver(-1.1,0,0,0,1,0,color='white',length=1.2,arrow_length_ratio=0.1)
	ax.quiver(-1.1,0,0,0,0,1,color='white',length=0.8,arrow_length_ratio=0.1)
	
	#Text
	ax.text(1.25,0,-0.03,'x',color='lightyellow',size=15)
	ax.text(-0.9,1.6,0,r'$Real(\psi)$',color='lightyellow',size=15)
	ax.text(-0.9,0,0.92,r'$Img(\psi)$',color='lightyellow',size=15)
	ax.text2D(0.7,0.03, "The Science Lovers", transform=ax.transAxes,size=15,color='azure')
	
	#Plotting Wavefunction
	ax.plot(x,psi[s*i,:].real,psi[s*i,:].imag,color='deepskyblue',label='Wavefunction')
	
	#Plotting the variable point 
	rd=random(1000,x,abs(psi[s*i,:])**2)
	w=np.random.randint(0,len(rd)-1)
	number=rd[w]
	plt.plot([number],[0],[-0],'o',color='lightcoral',markersize=10)
	
	#Plotting Probability Density
	phi=np.linspace(0,2*pi,50)
	X,Phi=np.meshgrid(x,phi)
	def f(d):
		return abs(psi[s*i,:])		
	Y=f(X)*cos(Phi)
	Z=f(X)*sin(Phi)
	ax.plot_surface(X,Y,Z,color='skyblue',alpha=0.6)
	
	#Plotting Potential
	ax.plot(x,[0]*m,0.0015*V,color='coral',label='Potential')
	ax.legend()
	
	plt.pause(0.1)
	ax.clear()

plt.show()