import numpy as np
import matplotlib.pyplot as plt

def f(n):
	s=1
	for i in reversed(range(1,n+1)):
		s=(s*i)**(i**(-1))
	return s

x=np.arange(1,50)
m=len(x)
y=np.zeros(m)
for i in range(m):
	y[i]=f(x[i])
	print y[i]

plt.plot(x,y,'ro-')
plt.grid()
plt.show()