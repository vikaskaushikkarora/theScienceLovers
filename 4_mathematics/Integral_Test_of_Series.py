# The Integral Test of Series##
import numpy as np
import matplotlib.pyplot as plt
N=100
sum=0
n=2 ## input real value of reimann zeta function
a=np.zeros(N)
for i in range(0,N-1):
	a[i]=(i+1)**(-n) #recursion relation
	sum = sum + a[i]
print(sum)
x=np.arange(1,20)
b=np.zeros(len(x))
for j in range (0,len(x)-1) :
	b[j]=a[j]
plt.plot(x,b,'ko-')
plt.fill_between(x,b)
plt.title("The sum of the series upto the %d terms is : %0.3f"%(N,sum))
plt.grid()
plt.show()
