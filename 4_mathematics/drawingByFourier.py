# Drawing figures by Fourier Transforms
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
from numpy import sin
from numpy import cos
#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568])

#Set x and y limits 
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)
#make background black
ax.set_facecolor('black')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')
#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])

ax.text(-1.35,1.2,'A Fantastic Application of ',color='skyblue',size=30)
ax.text(0.2,0.9,'Fourier Series ',color='skyblue',size=30)

#Logo Text :
ax.text(0.85,-1.40,'The Science Lovers',color='white',size=10)

#line object : plotting variable point
ax.plot(0,0,'o',color='blue',markersize=5)
P ,=ax.plot([],[],'o',color='skyblue',markersize=4)
P1,=ax.plot([],[],'o',color='white',markersize=4)
P2,=ax.plot([],[],'o',color='white',markersize=4)
P3,=ax.plot([],[],'o',color='white',markersize=4)
P4,=ax.plot([],[],'o',color='white',markersize=4)
P5,=ax.plot([],[],'o',color='white',markersize=4)
line,=ax.plot([],[],color='white',linewidth=3)
line1,=ax.plot([],[],color='skyblue',linewidth=3)
line2,=ax.plot([],[],color='skyblue',linewidth=3)
line3,=ax.plot([],[],color='skyblue',linewidth=3)
line4,=ax.plot([],[],color='skyblue',linewidth=3)
line5,=ax.plot([],[],color='skyblue',linewidth=3)
traj,=ax.plot([],[],color='deepskyblue',linewidth=2)
A,=ax.plot([],[],color='seagreen',linewidth=1)
B,=ax.plot([],[],color='seagreen',linewidth=1)
A1,=ax.plot([],[],color='azure',linewidth=1)
B1,=ax.plot([],[],color='azure',linewidth=1)
A2,=ax.plot([],[],color='white',linewidth=1)
B2,=ax.plot([],[],color='white',linewidth=1)
A3,=ax.plot([],[],color='white',linewidth=1)
B3,=ax.plot([],[],color='white',linewidth=1)
A4,=ax.plot([],[],color='white',linewidth=1)
B4,=ax.plot([],[],color='white',linewidth=1)



def init():
	P.set_data([],[])
	P1.set_data([],[])
	P2.set_data([],[])
	P3.set_data([],[])
	P4.set_data([],[])
	P5.set_data([],[])
	line.set_data([],[])
	line1.set_data([],[])
	line2.set_data([],[])
	line3.set_data([],[])
	line4.set_data([],[])
	line5.set_data([],[])
	traj.set_data([],[])
	A.set_data([],[])
	B.set_data([],[])
	A1.set_data([],[])
	B1.set_data([],[])
	A2.set_data([],[])
	B2.set_data([],[])
	A3.set_data([],[])
	B3.set_data([],[])
	A4.set_data([],[])
	B4.set_data([],[])
	
	
	
	return line,line1,line2,line3,line4,line5,P,P1,P2,P3,P4,P5,traj,A,B,A1,B1,A2,B2,A3,B3,A4,B4
	

x=np.arange(0,2*np.pi,0.001)
h=x[2]-x[1]
L=len(x)

#Real Part of given complex function of time
def fr(x):
	z=(cos(x))*(1-sin(x))*np.exp(sin(x))
	return z
#Imaginary Part of given complex function of time 
def fi(x):
	z=(sin(x))*(1-sin(x))*np.exp(sin(x))
	return z
#first function defined to calculate fourier coefficients 
def fr1(x,fr,fi):
	z=(cos(x))*fr(x)+fi(x)*(sin(x))
	return z
#And so are the others
def fi1(x,fr,fi):
	z=fi(x)*cos(x)-fr(x)*sin(x)
	return z

def fr2(x,fr,fi):
	z=cos(2*x)*fr(x)+fi(x)*sin(2*x)
	return z

def fi2(x,fr,fi):
	z=fi(x)*cos(2*x)-fr(x)*sin(2*x)
	return z
	
def fr3(x,fr,fi):
	z=cos(3*x)*fr(x)+fi(x)*sin(3*x)
	return z

def fi3(x,fr,fi):
	z=fi(x)*cos(3*x)-fr(x)*sin(3*x)
	return z

def fr4(x,fr,fi):
	z=cos(4*x)*fr(x)+fi(x)*sin(4*x)
	return z

def fi4(x,fr,fi):
	z=fi(x)*cos(4*x)-fr(x)*sin(4*x)
	return z

def fr5(x,fr,fi):
	z=cos(5*x)*fr(x)+fi(x)*sin(5*x)
	return z

def fi5(x,fr,fi):
	z=fi(x)*cos(5*x)-fr(x)*sin(5*x)
	return z

# Integration of Functions 

def g(x,f) :
	C=(f(x+h)-f(x))/h
	return C

def int(x,f,g) :
	z=0
	for i in range(0,L) :
		z=z+f(x[i])*h+0.5*g(x[i],f)*h**2
	return z


def g1(x,f) :
	C=(f(x+h,fr,fi)-f(x,fr,fi))/h
	return C

def int1(x,f,g) :
	z=0
	for i in range(0,L) :
		z=z+f(x[i],fr,fi)*h+0.5*g1(x[i],f)*h**2
	return z

#Fourier coefficients

cr=((2*np.pi)**(-1))*int(x,fr,g)
ci=((2*np.pi)**(-1))*int(x,fi,g)
cr1=((2*np.pi)**(-1))*int1(x,fr1,g1)
ci1=((2*np.pi)**(-1))*int1(x,fi1,g1)
cr2=((2*np.pi)**(-1))*int1(x,fr2,g1)
ci2=((2*np.pi)**(-1))*int1(x,fi2,g1)
cr3=((2*np.pi)**(-1))*int1(x,fr3,g1)
ci3=((2*np.pi)**(-1))*int1(x,fi3,g1)
cr4=((2*np.pi)**(-1))*int1(x,fr4,g1)
ci4=((2*np.pi)**(-1))*int1(x,fi4,g1)
cr5=((2*np.pi)**(-1))*int1(x,fr5,g1)
ci5=((2*np.pi)**(-1))*int1(x,fi5,g1)


# Radii of epicircles

R=np.sqrt(cr**2+ci**2)
R1=np.sqrt(cr1**2+ci1**2)
R2=np.sqrt(cr2**2+ci2**2)
R3=np.sqrt(cr3**2+ci3**2)
R4=np.sqrt(cr4**2+ci4**2)
R5=np.sqrt(cr5**2+ci5**2)



n=0.01 # smoothness of curve parameter , how much small time interval you want to take


#Animating epicycles

t=np.arange(0,13,n)
T=len(t)
a=np.zeros(T)
b=np.zeros(T)
a1=np.zeros(T)
b1=np.zeros(T)
a2=np.zeros(T)
b2=np.zeros(T)
a3=np.zeros(T)
b3=np.zeros(T)
a4=np.zeros(T)
b4=np.zeros(T)
a5=np.zeros(T)
b5=np.zeros(T)


for i in range (T):
	
	a[i]=cr
	b[i]=ci
	a1[i]=a[i]+cr1*cos(n*i)+ci1*sin(n*i)
	b1[i]=b[i]+cr1*sin(n*i)+ci1*cos(n*i)
	a2[i]=a1[i]+cr2*cos(2*n*i)+ci2*sin(2*n*i)
	b2[i]=b1[i]+cr2*sin(2*n*i)+ci2*cos(2*n*i)
	a3[i]=a2[i]+cr3*cos(3*n*i)+ci3*sin(3*n*i)
	b3[i]=b2[i]+cr3*sin(3*n*i)+ci3*cos(3*n*i)
	a4[i]=a3[i]+cr4*cos(4*n*i)+ci4*sin(4*n*i)
	b4[i]=b3[i]+cr4*sin(4*n*i)+ci4*cos(4*n*i)
	a5[i]=a4[i]+cr5*cos(5*n*i)+ci5*sin(5*n*i)
	b5[i]=b4[i]+cr5*sin(5*n*i)+ci5*cos(5*n*i)
	
	
	


def animate(i):
	s=2# speed of animation 
	P.set_data(a[s*i],b[s*i])
	P1.set_data(a1[s*i],b1[s*i])
	P2.set_data(a2[s*i],b2[s*i])
	P3.set_data(a3[s*i],b3[s*i])
	P4.set_data(a4[s*i],b4[s*i])
	P5.set_data(a5[s*i],b5[s*i])
	x=[0,a[s*i]]
	y=[0,b[s*i]]
	x1=[a[s*i],a1[s*i]]
	y1=[b[s*i],b1[s*i]]
	x2=[a1[s*i],a2[s*i]]
	y2=[b1[s*i],b2[s*i]]
	x3=[a2[s*i],a3[s*i]]
	y3=[b2[s*i],b3[s*i]]
	x4=[a3[s*i],a4[s*i]]
	y4=[b3[s*i],b4[s*i]]
	x5=[a4[s*i],a5[s*i]]
	y5=[b4[s*i],b5[s*i]]
	line.set_data(x,y)
	line1.set_data(x1,y1)
	line2.set_data(x2,y2)
	line3.set_data(x3,y3)
	line4.set_data(x4,y4)
	line5.set_data(x5,y5)
	traj.set_data(a5[0:s*i],b5[0:s*i])
	
	
	#Drawing epicircles
	
	alpha=np.linspace(0-R,0+R,500)
	beta=np.sqrt(R**2-(alpha)**2)
	beta_= 0-np.sqrt(R**2-(alpha)**2)
	A.set_data(alpha,beta)
	B.set_data(alpha,beta_)
	
	alpha1=np.linspace(a[s*i]-R1,a[s*i]+R1,2000)
	beta1=b[s*i]+np.sqrt(R1**2-(alpha1-a[s*i])**2)
	beta1_= b[s*i]-np.sqrt(R1**2-(alpha1-a[s*i])**2)
	A1.set_data(alpha1,beta1)
	B1.set_data(alpha1,beta1_)
	
	alpha2=np.linspace(a1[s*i]-R2,a1[s*i]+R2,2000)
	beta2=b1[s*i]+np.sqrt(R2**2-(alpha2-a1[s*i])**2)
	beta2_= b1[s*i]-np.sqrt(R2**2-(alpha2-a1[s*i])**2)
	A2.set_data(alpha2,beta2)
	B2.set_data(alpha2,beta2_)
	
	alpha3=np.linspace(a2[s*i]-R3,a2[s*i]+R3,2000)
	beta3=b2[s*i]+np.sqrt(R3**2-(alpha3-a2[s*i])**2)
	beta3_= b2[s*i]-np.sqrt(R3**2-(alpha3-a2[s*i])**2)
	A3.set_data(alpha3,beta3)
	B3.set_data(alpha3,beta3_)
	
	alpha4=np.linspace(a3[s*i]-R4,a3[s*i]+R4,2000)
	beta4=b3[s*i]+np.sqrt(R4**2-(alpha4-a3[s*i])**2)
	beta4_= b3[s*i]-np.sqrt(R4**2-(alpha4-a3[s*i])**2)
	A4.set_data(alpha4,beta4)
	B4.set_data(alpha4,beta4_)
		
	
	return line,line1,line2,line3,line4,line5,P,P1,P2,P3,P4,P5,traj,A,B,A1,B1,A2,B2,A3,B3,A4,B4

anim = FuncAnimation(fig, animate, init_func = init, frames = T, interval = 10, blit = True)

plt.show()

