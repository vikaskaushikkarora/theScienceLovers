import numpy as np
import matplotlib.pyplot as plt

def f(n):
	sum=0
	for i in reversed(range(1,n)):
		sum=(sum+i+1)**(-1)
	sum=sum+1
	return sum
	
x=np.arange(1,10,1)
m=len(x)
y=np.zeros(m)
for i in range(m):
	y[i]=f(x[i])
	print y[i]
	
plt.plot(x,y,'ro-')
plt.grid()
plt.show()