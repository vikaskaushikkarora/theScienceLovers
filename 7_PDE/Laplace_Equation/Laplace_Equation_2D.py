# Laplace Equation 2D ________________________________

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#______________________________


N=20 # no. of divisions along x and y axies
x=np.linspace(-0.05,0.05,N)
y=np.linspace(-0.05,0.05,N)
V=np.zeros((N,N)) #Potential in 2D -: Matrix 

# Boundary Conditions of Potential 
V[:,0]=0
V[:,N-1]=0
V[0,:]=1
V[N-1,:]=1


#______________________________

# Converting differential equation into alzebraic linear equations :- A*Z = B

n=N-2
M=n**2

A=np.zeros((M,M))
A[M-1,M-1]=4

for i in range (1,M):
	A[i-1,i-1]=4
	if i%n != 0 :
		A[i-1,i]=-1
		
for i in range (M-n):
	A[i,i+n]=-1
	
#Making matrix A symmetric
for j in range (M):
	for i in range (j+1,M):
		A[i,j]=A[j,i]

#print A

B=np.zeros(M)

B[0]=V[1,0]+V[0,1]
B[n-1]=V[0,N-2]+V[1,N-1]
B[n]=V[2,0]

for i in range (1,n-1):
	B[i]=V[0,i+1]

for i in range (n,M-n):
	if (i+1)%n == 0 :
		B[i]=V[(i+1)/n,N-1]
		B[i+1]=V[((i+1)/n)+1,0]

B[M-n]=V[N-2,0]+V[N-1,1]
B[M-1]=V[N-1,N-2]+V[N-2,N-1]

for i in range (M-n+1,M-1):
	B[i]=V[N-1,(i%n)+1]

#print B

Z = np.linalg.solve(A,B)

for i in range (1,N-1):
	for j in range (1,N-1):
		V[i,j] = Z[n*(i-1)+j-1]


#______________________________
#Plotting

fig = plt.figure()
ax = Axes3D(fig)
ax.set_axis_off()
ax.set_aspect('equal','box')
ax.set_facecolor('black')
X,Y=np.meshgrid(x,y)
ax.plot_surface(X,Y,V,antialiased=True)
plt.show() 