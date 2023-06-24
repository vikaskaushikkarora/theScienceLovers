# Stationary States for any Potential
# By Matrix Method
# The condition that wavefunction at x[0] and x[l-1] vanish are implemented ....
# We have solved it for an empty box here
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as la
#constants :
h=1.054e-34
m=9.1e-31
e=1.6e-19
#define x-axis :
l=1500
x=np.linspace(-1e-10,1e-10,l)
#delete first and last terms for non-obvious reasons (You will know the reason only when you do it by hand by going into the details of the Matrix Method and use of finite difference to convert differential equation into alzebraic equation ...)
x=np.delete(x,[0,l-1])
dx=x[1]-x[0]
L=len(x)
#define a matrix
matrix=np.zeros((L,L))
for i in range (L-1):
	matrix[i,i]=-2
	matrix[i,i+1]=1
	matrix[i+1,i]=1
matrix[L-1,L-1]=-2
#print(x)
#print(matrix)
#Kinetic Energy Matrix
alpha=-(dx**(-2))*(h*h*(2*m)**(-1))
K=alpha*matrix
#Potential Energy Matrix
V=np.zeros((L,L))
for i in range (50):
	V[i,i]=0
for i in range (50,L-50):
	V[i,i]=-400*e
for i in range (L-50,L):
	V[i,i]=0
#Hamiltonian Matrix
H=K+V
#print(H)
#find out eignvalues and eignvectors from Hamiltonian Matrix which means stationary states of energy 
eign=la.eig(H)
eignvalues=eign[0]
eignvectors=eign[1]

#Plotting Eignfunctions Probability Density
plt.subplot(2,2,1)
plt.plot(x,eignvectors[:,0]*eignvectors[:,0],'b')
plt.legend(['1st Stationary State'],loc=1)
plt.subplot(2,2,2)
plt.plot(x,eignvectors[:,1]*eignvectors[:,1],'r')
plt.legend(['2nd Stationary State'],loc=1)
plt.subplot(2,2,3)
plt.plot(x,eignvectors[:,2]*eignvectors[:,2],'k')
plt.legend(['3rd Stationary State'],loc=1)
plt.subplot(2,2,4)
plt.plot(x,eignvectors[:,3]*eignvectors[:,3],'c')
plt.legend(['4th Stationary State'],loc=1)
plt.suptitle('The probability density corresponding \nto first four states',size=25,color='black')

print(eignvalues*(1.6e-19)**(-1))
plt.show()