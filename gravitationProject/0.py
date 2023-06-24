#Sliding Text
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig = plt.figure() 
ax = fig.add_axes([0.20,0.015,0.74,0.975])
ax.set_xlim(0,5)
ax.set_ylim(0,2)
line, = ax.plot([], [],'o',markersize=10,color='deepskyblue')
line1, = ax.plot([],[],color='skyblue')
line2, = ax.plot([], [],'o',markersize=10,color='skyblue')
line3, = ax.plot([], [],color='deepskyblue')
ax.set_xticks([])
ax.set_yticks([])
# Background Color
ax.set_facecolor('black')
# Index Text 
n1=70
n2=n1+230
n3=n2+70
N=n3

def ell (a,b,c,d):
	A=np.arange(a-c,a+c,0.0001)
	B=b+d*(c**(-1))*np.sqrt(c**2-(A-a)**2)
	B_=b-d*(c**(-1))*np.sqrt(c**2-(A-a)**2)
	plt.plot(A,B,color='orange')
	plt.plot(A,B_,color='orange')
	plt.fill_between(A,B,B_,color='orange')

ax.scatter(6*np.random.rand(300,1),2*np.random.rand(300,1),s=0.3,color='white')
ax.scatter(6*np.random.rand(50,1),2*np.random.rand(50,1),s=3,color='white')
ax.scatter(6*np.random.rand(10,1),2*np.random.rand(10,1),s=5,color='white')


ell(4,1.6,0.2,0.1)


def init():
	line.set_data([], [])
	line1.set_data([],[])
	line2.set_data([], [])
	line3.set_data([], [])
	return line,line1,line2,line3
	
x=np.zeros(N)
y=np.zeros(N)
x1=np.zeros(N)
y1=np.zeros(N)

def animate(i):
	L= 5 # Length of Index Text
	L1= 3
	if i <= n1 :
		x[i]=4+0.80*np.cos(0.1*i)
		y[i]=1.6+0.30*np.sin(0.1*i)
		line.set_data(x[i],y[i])
		line1.set_data(x[0:i],y[0:i])
		line2.set_data(10,10)
		line3.set_data(10,10)
		q=ax.text(-L+i*(3+0.5*L)*(n1**(-1)),1.25,'What is Gravitation ?',color='white',size=35)
		p=ax.text(-L1+i*(3+0.5*L1)*(n1**(-1)),0.75,'Explained as Easily as Possible',color='skyblue',size=25)
	elif ( i > n1 and i <= n2 ):
		x[i]=4+0.80*np.cos(0.1*i)
		y[i]=1.6+0.30*np.sin(0.1*i)
		line.set_data(x[i],y[i])
		line1.set_data(x[i-10:i],y[i-10:i])
		x1[i]=(i-n1)*0.02
		y1[i]=0.0127*np.exp(x1[i])
		line2.set_data(x1[i],y1[i])
		line3.set_data(x1[i-10:i],y1[i-10:i])
		q=ax.text(3-0.5*L,1.25,'What is Gravitation ?',color='skyblue',size=35)
		p=ax.text(3-0.5*L1,0.75,'Explained as Easily as Possible',color='white',size=25)
	elif ( i > n2 and i <= n3 ):
		x[i]=4+0.80*np.cos(0.1*i)
		y[i]=1.6+0.30*np.sin(0.1*i)
		line.set_data(x[i],y[i])
		line1.set_data(x[i-10:i],y[i-10:i])
		line2.set_data(10,10)
		line3.set_data(10,10)
		q=ax.text((3-0.5*L)+(i-n2)*(3+0.5*L)*(n3-n2)**(-1),1.25,'What is Gravitation ?',color='white',size=35)
		p=ax.text((3-0.5*L1)+(i-n2)*(3+0.5*L1)*(n3-n2)**(-1),0.75,'Explained as Easily as Possible',color='skyblue',size=25)
	return line, q , p ,line1,line2,line3

anim = FuncAnimation(fig, animate, init_func = init, frames = N , interval = 40, blit = True)
plt.show()