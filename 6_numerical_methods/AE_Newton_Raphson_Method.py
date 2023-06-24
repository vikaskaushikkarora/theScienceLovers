#Alzebraic Equation
#Newton Raphson
import numpy as np
import matplotlib.pyplot as plt
def f(x):
	y=x**20+x**5-30*x**2+10 # Equation
	return y
def g(x,f):
	h=0.01
	z=(f(x+h)-f(x))/h
	return z

m=100 # No. of points you want to start calculating roots from
A=np.zeros(m)
for j in range (0,m):
	n=500 #Number of Iterations
	x=np.zeros(n)
	x[0]=-10+(j)*20*(m)**(-1)
	for i in range (0,len(x)-1):
		x[i+1]=x[i]-(f(x[i])/g(x[i],f))
	A[j]=x[len(x)-1]
print('Possible Roots are :')
print(A)

# Plotting Function Visually
a=np.arange(-1.5,1.5,0.01)
plt.plot(a,f(a))
plt.grid()
plt.title('Function')
plt.show()
