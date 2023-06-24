#Temp:O
#centre of fig :(3,1)
#centre of text :(5,1)
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.20,0.015,0.74,0.975])

#Set x and y limits 
ax.set_xlim(0,6)
ax.set_ylim(0,2)
#make background black
ax.set_facecolor('black')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')
#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])

#Stationary figures in animation

ax.scatter(6*np.random.rand(300,1),2*np.random.rand(300,1),s=0.3,color='white')
ax.scatter(6*np.random.rand(40,1),2*np.random.rand(40,1),s=3,color='white')
ax.scatter(6*np.random.rand(5,1),2*np.random.rand(5,1),s=5,color='white')


A1=(-1)**(np.random.randint(10))*0.06*np.random.randn(10000)
B1=(-1)**(np.random.randint(10))*0.03*np.random.randn(10000)
ax.scatter(3+A1,1.2+B1,color='orange',s=0.1)

def ell (a,b,c,d):
	A=np.arange(a-c,a+c,0.0001)
	B=b+d*(c**(-1))*np.sqrt(c**2-(A-a)**2)
	B_=b-d*(c**(-1))*np.sqrt(c**2-(A-a)**2)
	plt.plot(A,B,'w')
	plt.plot(A,B_,'w')
	

def ell1 (a,b,c,d):
	A=np.arange(a-c,a+c,0.0001)
	B=b+d*(c**(-1))*np.sqrt(c**2-(A-a)**2)
	B_=b-d*(c**(-1))*np.sqrt(c**2-(A-a)**2)
	plt.plot(A,B,'lightcoral')
	plt.plot(A,B_,'lightcoral')

ell(3,1.2,1,0.45)
ell1(3,1.2,1.52,0.68)


#Main text in Animation
ax.text(0.28,0.15,'Mars and Other planets also move around the Sun . But the planet at a \nlarger distance takes more time to go around the Sun than the nearer one \nAnd this is Keplers Third Law .',size=18 , color='skyblue')

ax.text(2.85,0.87,'Sun',size=20 , color='Orange')


#Logo Text :
ax.text(5,0.1,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
line,= ax.plot([], [],'o',color='skyblue',markersize=20)
line1,= ax.plot([], [],'o',color='lightcoral',markersize=11)

def cir (a,b,R):
	A=np.zeros(10000)
	for j in range (4000):
		A[j]=a-R+2.5*10**(-5)*j
	for j in range (4000,6000):
		A[j]=a-0.9*R+9*10**(-4)*R*(j-4000)
	for j in range (6000,10000):
		A[j]=a+0.9*R+2.5*10**(-4)*R*(j-6000)
	B=b+0.8*np.sqrt(R**2-(A-a)**2)
	B_=b-0.8*np.sqrt(R**2-(A-a)**2)
	plt.plot(A,B,color='skyblue')
	plt.plot(A,B_,color='skyblue')
	plt.fill_between(A,B,B_,color='skyblue')
	
def cir1(a,b,R):
	A=np.zeros(10000)
	for j in range (4000):
		A[j]=a-R+2.5*10**(-5)*j
	for j in range (4000,6000):
		A[j]=a-0.9*R+9*10**(-4)*R*(j-4000)
	for j in range (6000,10000):
		A[j]=a+0.9*R+2.5*10**(-4)*R*(j-6000)
	B=b+0.8*np.sqrt(R**2-(A-a)**2)
	B_=b-0.8*np.sqrt(R**2-(A-a)**2)
	plt.plot(A,B,color='lightcoral')
	plt.plot(A,B_,color='lightcoral')
	plt.fill_between(A,B,B_,color='lightcoral')
	
cir(4.8,1.7,0.07)
cir1(4.8,1.5,0.07)
ax.text(5,1.67,'Earth',color='skyblue',size=20)
ax.text(5,1.47,'Mars',color='lightcoral',size=20)

#another line object : maybe plotting its path or anything else

#Time array ( omit if not required) :
t=np.arange(0,1,0.001)
dt=t[1]-t[0]
T=len(t)

#Initiallizing Function
def init():
	line.set_data([], [])
	line1.set_data([],[])
	return line,line1

x=np.zeros(T)
y=np.zeros(T)
x1=np.zeros(T)
y1=np.zeros(T)
for i in range (T):
	x[i]=3+1*np.cos(40*t[i])
	y[i]=1.2+0.45*np.sin(40*t[i])
	x1[i]=3+1.52*np.cos(2*10.69*t[i])
	y1[i]=1.2+0.68*np.sin(2*10.69*t[i])
# Repeatition Function
def animate(i):
	#setting data for line object
	line.set_data(x[i+1],y[i+1])
	line1.set_data(x1[i+1],y1[i+1])

	#Other things in animations which vary for different frames 
	#return the variables and objects in the function
	return line,line1

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T-1, interval = 10, blit = True)

plt.show() 