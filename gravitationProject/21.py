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
ax.set_xlim(0,9)
ax.set_ylim(0,3)
#make background black
ax.set_facecolor('black')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')
#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])

#Stationary figures in animation


ax.scatter(9*np.random.rand(300,1),3*np.random.rand(300,1),s=0.3,color='white')
ax.scatter(9*np.random.rand(50,1),3*np.random.rand(50,1),s=3,color='white')
ax.scatter(9*np.random.rand(10,1),3*np.random.rand(10,1),s=5,color='white')

ax.text(0.4,0.9,' ',color='lightcyan',size=30)
h=0.001 # step-size
G=1 # Strength of field
# Masses of three bodie
m1=15
m2=1
m3=0.2
t=np.arange(0,5,h)
T=len(t)
x1=np.zeros(len(t))# X coordinate 1
y1=np.zeros(len(t))#Y coordinate 1
z1=np.zeros(len(t)) # X coordinate of velocity of mass 1
w1=np.zeros(len(t))# Y ccordinate of velocity of mass 2
x2=np.zeros(len(t))# And similarily these
y2=np.zeros(len(t))
z2=np.zeros(len(t))
w2=np.zeros(len(t))
x3=np.zeros(len(t))
y3=np.zeros(len(t))
z3=np.zeros(len(t))
w3=np.zeros(len(t))
#Initial Conditions
x1[0]=0
y1[0]=0
z1[0]=0
w1[0]=0
x2[0]=1
y2[0]=0
z2[0]=-01
w2[0]=3.5
x3[0]=2
y3[0]=0
z3[0]=-8
w3[0]=1.7
# Equations of motions of three objects 
def a(z1):
	A=z1
	return A
def b(x1,y1,x2,y2,x3,y3):
	B=G*m2*(x2-x1)*((x1-x2)**2+(y1-y2)**2)**(-1.5)+G*m3*(x3-x1)*((x1-x3)**2+(y1-y3)**2)**(-1.5)
	return B
def c(w1):
	C=w1
	return C
def d(x1,y1,x2,y2,x3,y3):
	D=G*m2*(y2-y1)*((x1-x2)**2+(y1-y2)**2)**(-1.5)+G*m3*(y3-y1)*((x1-x3)**2+(y1-y3)**2)**(-1.5)
	return D
def e(z2):
	E=z2
	return E
def f(x1,y1,x2,y2,x3,y3):
	F=G*m1*(x1-x2)*((x1-x2)**2+(y1-y2)**2)**(-1.5)+G*m3*(x3-x2)*((x2-x3)**2+(y2-y3)**2)**(-1.5)
	return F
def j(w2):
	J=w2
	return J
def k(x1,y1,x2,y2,x3,y3):
	K=G*m1*(y1-y2)*((x1-x2)**2+(y1-y2)**2)**(-1.5)+G*m3*(y3-y2)*((x2-x3)**2+(y2-y3)**2)**(-1.5)
	return K
def l(z3):
	L=z3
	return L
def p(x1,y1,x2,y2,x3,y3):
	P=G*m1*(x1-x3)*((x1-x3)**2+(y1-y3)**2)**(-1.5)+G*m2*(x2-x3)*((x2-x3)**2+(y2-y3)**2)**(-1.5)
	return P
def q(w3):
	Q=w3
	return Q
def r(x1,y1,x2,y2,x3,y3):
	R=G*m1*(y1-y3)*((x1-x3)**2+(y1-y3)**2)**(-1.5)+G*m2*(y2-y3)*((x2-x3)**2+(y2-y3)**2)**(-1.5)
	return R
#Iterations : We have used Euler Verlet Method to conserve Energy
for i in range (0,len(t)-1):
	z1[i+1]=z1[i]+h*b(x1[i],y1[i],x2[i],y2[i],x3[i],y3[i])
	x1[i+1]=x1[i]+h*a(z1[i+1])
	w1[i+1]=w1[i]+h*d(x1[i],y1[i],x2[i],y2[i],x3[i],y3[i])
	y1[i+1]=y1[i]+h*c(w1[i+1])
	z2[i+1]=z2[i]+h*f(x1[i],y1[i],x2[i],y2[i],x3[i],y3[i])
	x2[i+1]=x2[i]+h*e(z2[i+1])
	w2[i+1]=w2[i]+h*k(x1[i],y1[i],x2[i],y2[i],x3[i],y3[i])
	y2[i+1]=y2[i]+h*j(w2[i+1])
	z3[i+1]=z3[i]+h*p(x1[i],y1[i],x2[i],y2[i],x3[i],y3[i])
	x3[i+1]=x3[i]+h*l(z3[i+1])
	w3[i+1]=w3[i]+h*r(x1[i],y1[i],x2[i],y2[i],x3[i],y3[i])
	y3[i+1]=y3[i]+h*q(w3[i+1])
#Plots

line,= ax.plot(7,2.7,'o',color='yellow',markersize=50)
bh,=ax.plot(7,2.7,'o',color='black',markersize=45)
line1,= ax.plot(7,2.2,'*',color='white',markersize=30)
line2,= ax.plot(7,1.9,'*',color='skyblue',markersize=20)
ax.text(7.5,2.65,'Blackhole',color='Yellow',size=20)
ax.text(7.6,2.15,'Bigger Star',color='white',size=15)
ax.text(7.6,1.85,'Smaller Star',color='skyblue',size=15)

line,= ax.plot([], [],'o',color='yellow',markersize=50)
bh,=ax.plot([],[],'o',color='black',markersize=45)
line1,= ax.plot([], [],'*',color='white',markersize=25)
line2,= ax.plot([], [],'*',color='skyblue',markersize=20)


ax.text(4.6,0.7,'When one of the objects out of \nthe three bodies involved in \ngravitation is not very massive , \nit is practically thrown out of \nthe system',color='white',size=20)


ax.text(7.5,0.2,'The Science Lovers',color='white',size=10)


def init():
	line.set_data([], [])
	line1.set_data([],[])
	line2.set_data([],[])
	bh.set_data([],[])
	return line,line1,line2,bh
def animate(i):
	#setting data for line object
	line.set_data(2.5+x1[5*i],0.5+y1[5*i])
	bh.set_data(2.49+x1[5*i],0.5+y1[5*i])
	line1.set_data(2.5+x2[5*i],0.5+y2[5*i])
	line2.set_data(2.5+x3[5*i],0.5+y3[5*i])
	
	#Other things in animations which vary for different frames 
	#return the variables and objects in the function
	return line,line1,line2,bh

#Draw Animation using FuncAnimation command
anim = FuncAnimation(fig, animate, init_func = init, frames = T-1, interval = 10, blit = True)
plt.show()