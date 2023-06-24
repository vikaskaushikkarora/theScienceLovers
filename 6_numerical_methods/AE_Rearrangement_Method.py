#Solution of Alzebraic Equation
#Rearranagment Method
import numpy as np
import matplotlib.pyplot as plt
n=5
x=np.zeros(n)
x[0]=1.7
for i in range (0,n-2):
	# A.E. is x**5-2*x**2-3=0
	#Upon rearranging it becomes :-
	x[i+1]=(2*x[i]*x[i]+3)**(0.2)
	print(x[i+1])
y=np.arange(-2,2,0.01)
plt.plot(y,y**5-2*y**2-3)
z=np.zeros(len(x))
plt.plot(x,z,'ro')
plt.grid()
plt.show(
