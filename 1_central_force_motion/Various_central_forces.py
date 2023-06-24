import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G=1
h=0.0001
t=np.arange(0,30,h)
T=len(t)

def f1(x,y):
	a=-G*x*(x**2+y**2)**(-1.5)
	return a
def g1(x,y):
	b=-G*y*(x**2+y**2)**(-1.5)
	return b

def f2(x,y):
	a=-G*x*(x**2+y**2)**(-1)
	return a
def g2(x,y):
	b=-G*y*(x**2+y**2)**(-1)
	return b

def f3(x,y):
	a=-G*x*(x**2+y**2)**(-2)
	return a
def g3(x,y):
	b=-G*y*(x**2+y**2)**(-2)
	return b


x1=np.zeros(T)
y1=np.zeros(T)
z1=np.zeros(T)
w1=np.zeros(T)

x2=np.zeros(T)
y2=np.zeros(T)
z2=np.zeros(T)
w2=np.zeros(T)

x3=np.zeros(T)
y3=np.zeros(T)
z3=np.zeros(T)
w3=np.zeros(T)

x1[0]=1
y1[0]=1
z1[0]=-0.6
w1[0]=0.2

x2[0]=1
y2[0]=1
z2[0]=-0.6
w2[0]=0.2

x3[0]=1
y3[0]=1
z3[0]=-0.6
w3[0]=0.2


for i in range (0,T-1):
	#I have used Euler Verlet method here . I have calculated the ith coordinate of distance from the ( i+1)th coordinate of velocity components . This conserves energy ...
	z1[i+1]=z1[i]+h*f1(x1[i],y1[i])
	x1[i+1]=x1[i]+h*z1[i+1]
	w1[i+1]=w1[i]+h*g1(x1[i],y1[i])
	y1[i+1]=y1[i]+h*w1[i+1]
	
	z2[i+1]=z2[i]+h*f2(x2[i],y2[i])
	x2[i+1]=x2[i]+h*z2[i+1]
	w2[i+1]=w2[i]+h*g2(x2[i],y2[i])
	y2[i+1]=y2[i]+h*w2[i+1]
	
	z3[i+1]=z3[i]+h*f3(x3[i],y3[i])
	x3[i+1]=x3[i]+h*z3[i+1]
	w3[i+1]=w3[i]+h*g3(x3[i],y3[i])
	y3[i+1]=y3[i]+h*w3[i+1]
	

#Animating

fig = plt.figure()   
axis = fig.add_axes([0.05,0.05,0.9,0.9])
axis.set_xlim(-2,2)
axis.set_ylim(-3,3)
axis.set_xticks([])
axis.set_yticks([])
axis.set_facecolor('black')
line, = axis.plot([], [],'o',color='skyblue')
aline, = axis.plot([], [],color='skyblue',label=r'$\frac{1}{r^2}$')
line2, = axis.plot([], [],'o',color='white') 
aline2, = axis.plot([], [],color='white',label=r'$\frac{1}{r}$') 
line3, = axis.plot([], [],'o',color='red') 
aline3, = axis.plot([], [],color='red',label=r'$\frac{1}{r^3}$') 
plt.scatter(0.06*np.random.randn(8000,1),0.06*np.random.randn(8000,1),s=0.05,color='orange')
axis.text(0.16,0.16,'Sun',size=18,color='orange',ha='center',va='center')
axis.legend(loc=5,frameon='false',facecolor='grey',fontsize=15)
#axis.text(-0.4,0.65,'Precession in Orbit of Mercury',color='lightyellow',style='oblique',size=25)
#axis.text(-0.1,0.58,' ( As predicted by General Relativity )',color='deepskyblue',style='oblique',size=13)
#axis.text(0.2,-0.53,'The Science Lovers',color='skyblue',style='oblique',size=13)

s=60
def animate(i):
	p=s*i
	q=s*(i+1)
	line.set_data(x1[p],y1[p])
	aline.set_data(x1[0:q],y1[0:q])
	line2.set_data(x2[p],y2[p])
	aline2.set_data(x2[0:q],y2[0:q])
	if i < int(0.0673*T*s**(-1)) :
		line3.set_data(x3[p],y3[p])
		aline3.set_data(x3[0:q],y3[0:q])
	else :
		line3.set_data(0,0)
		aline3.set_data(50,50)
	
	return line,aline,line2,aline2,line3,aline3

anim = FuncAnimation(fig, animate, frames = T, interval = 0.1, blit = True)

plt.show()
