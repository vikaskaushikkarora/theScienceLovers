# Solution of Alzebraic Equation
# Binary Chopping 
import numpy as np
x=np.zeros(100)
def f(x):
	y=np.cos(x)
	return y
# a and b must be taken as f(a)*f(b) < 0
a=1
b=2
x[0]=a
x[1]=b
for i in range(1,99):
	x[i+1]=(a+b)*(0.5)
	if f(a)*f(x[i+1]) <0 :
		b=x[i+1]
	elif f(a)*f(x[i+1])==0 :
		break
	else :
		a=x[i+1]
print('The root is %0.3f'%x[99])
print(x)
