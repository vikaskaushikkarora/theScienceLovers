# Basic Equation of Chaos
import numpy as np
import matplotlib.pyplot as plt 
n=2

b=np.zeros(1000)

for i in range(120):
	b[i]=i*(40)**(-1)
for i in range(120,300):
	b[i]=3+(i-120)*(90)**(-1)
for i in range(300,1000):
	b[i]=3.5+(i-300)*(1500)*(-1)

for j in range (0,1000):
	x=np.zeros(int((b[j]+1)*n))
	x[0]=np.random.rand()
	for i in range (0,len(x)-1):
		x[i+1]=b[j]*x[i]*(1-x[i])
		plt.plot(b[j],x[len(x)-1],'k.')

plt.annotate('This is the most basic equation of chaos \n and you can see the chaos after x=3 ', xy=(0.2,0.9), xytext=(0.2,0.9),size=13,color='green')
plt.title(' Graph for Chaotic Equation : a(n+1)=x*a(n)*(1-a(n))',colo='blue')
plt.xlabel('x')
plt.ylabel('a(1000)')
plt.show()
