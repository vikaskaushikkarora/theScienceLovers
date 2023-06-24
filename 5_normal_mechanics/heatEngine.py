# A Heat Engine
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568])

#Set x and y limits 
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
#make background black
ax.set_facecolor('grey')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')
#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])


ax.text(0.6,1.5,'Wheel',color='lightskyblue',size=20)
ax.text(0.12,0.10,'Piston',color='lightskyblue',size=20)
ax.text(-0.28,-1.87,'Cylinder',color='white',size=20)

def cir (a,b,R):
	A=np.zeros(10000)
	for j in range (4000):
		A[j]=a-R+2.5*10**(-5)*j
	for j in range (4000,6000):
		A[j]=a-0.9*R+9*10**(-4)*R*(j-4000)
	for j in range (6000,10000):
		A[j]=a+0.9*R+2.5*10**(-4)*R*(j-6000)
	B=b+np.sqrt(R**2-(A-a)**2)
	B_=b-np.sqrt(R**2-(A-a)**2)
	plt.plot(A,B,'w')
	plt.plot(A,B_,'w')
	plt.fill_between(A,B,B_,color='cyan')

cir (0,1,0.7)


#line object : plotting variable point

line,=ax.plot([],[],'o',color='red',markersize=25)
line1,=ax.plot([],[],'o',color='blue',markersize=7)
line2,=ax.plot([],[],color='seagreen',linewidth=5)
line3,=ax.plot([],[],color='blue',linewidth=5)

def init():
	line.set_data([],[])
	line1.set_data([],[])
	line2.set_data([],[])
	line3.set_data([],[])
	return line,line1,line2,line3
		
def animate(i):
	a=0
	b=-1
	c=1
	f=0.7
	L=1.3
	
	a1=0.3*np.cos(0.1*i)
	b1=1+0.3*np.sin(0.1*i)
	d=b1-(L**2-a1**2)**(0.5)
	
	
	line.set_data(a1,b1)
	line1.set_data(0.45*np.cos(0.1*i+np.pi*0.33),1+0.45*np.sin(0.1*i+np.pi*(0.33)))
	if ( np.sin(0.1*i+np.pi*(0.5)) > 0 ) :
		A=np.arange(a-0.5*c,a+0.5*c,0.001)
		A_=[b-(f)]*len(A)
		A__=[d]*len(A)
		X=ax.fill_between(A,A_,A__,color='lightyellow')
	else :	
		A=np.arange(a-0.5*c,a+0.5*c,0.001)
		A_=[b-(f)]*len(A)
		A__=[d]*len(A)
		X=ax.fill_between(A,A_,A__,color='chocolate')
	
	x=np.linspace(0,a1,500)
	y=(b1-d)*(a1)**(-1)*x+d
	line2.set_data(x,y)
	
	
	z=np.linspace(-0.5*c,0.5*c,500)
	w=[d]*len(z)
	line3.set_data(z,w)
	
	
	if ( np.sin(0.1*i+np.pi*(0.5)) > 0 ) :
		alpha=np.linspace(-1.2,-0.5,500)
		beta=[-0.8]*len(alpha)
		beta_=[-1.4]*len(alpha)
		A= ax.text(-1.1,-1.23,'Hot \nSource',color='white',size=20)
		P = plt.fill_between(alpha,beta,beta_,color='lightcoral')
		B=ax.text(-0.31,-1.15,'Expanding',color='black',size=15)
	else :
		A = ax.text(0.63,-1.23,'Cold \n  Sink',color='white',size=20)
		alpha=np.linspace(0.5,1.2,500)
		beta=[-0.8]*len(alpha)
		beta_=[-1.4]*len(alpha)
		P = plt.fill_between(alpha,beta,beta_,color='lightskyblue')
		B=ax.text(-0.31,-1.15,'Contracting',color='white',size=15)
	
	
	
	
	return X,line1,line2,line3,line,B,P,A



#Logo Text :
ax.text(1.25,-1.95,'The Science Lovers',color='white',size=10)

anim = FuncAnimation(fig, animate, init_func = init, frames = 500, interval = 30, blit = True)



plt.show() 
