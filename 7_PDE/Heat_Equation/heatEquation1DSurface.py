#Heat Equation _______________________________



#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation 



#Define Time and Space Meshgrid
n=2000 #Time Steps
m=70 #Space Steps
t=np.linspace(0,2.5,n)
h=t[2]-t[1] #Time Interval
x=np.linspace(-1,1,m)
k=x[2]-x[1] #Space Interval
T=np.zeros((n,m)) #Temp.
a=0.3 # Conductivity
b=h*a*k**(-2)



#Initial Conditions :-
for j in range(0,m):
	T[0,j]= 1+x[j]



#Finite Difference Method
#Iterations :-
for i in range (n-1):
	for j in range (1,m-1):
		T[i+1,j]=(1-2*b)*T[i,j]+b*(T[i,j+1]+T[i,j-1]) 
		
	# Boundary Conditions
	# (The temperature gradient at boundaries is zero i.e. heat does not flow at the ends )
	T[i+1,0]=T[i+1,1]
	T[i+1,m-1]=T[i+1,m-2]



#Plotting Surface and Rod	
fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal','box')
ax.set_facecolor('black')
ax.set_axis_off()
ax.set_xlim(-1.1,1.1)
ax.set_ylim(-0.1,2.1)
ax.set_zlim(-0.1,1.9)
A=ax.view_init(elev=20 , azim=150)
ax.plot(x,[0]*m,[-0.3]*m,linewidth=3,color='deepskyblue')
p,q=np.meshgrid(x,t)
ax.plot_surface(p,q,T,cmap='hot')



#Axies And Labelling :-
ax.quiver(1,0,-0.3,0,0,2.6,arrow_length_ratio=0.03,color='azure')
ax.quiver(1,0,-0.3,0,2.5,0,arrow_length_ratio=0.03,color='azure')
ax.text(0.9,0,2.1,'Temperature',color='azure',size=15)
ax.text(0.8,2.5,-0.3,'Time',color='azure',size=15)
ax.text(-1.1,0,-0.3,'Rod',color='deepskyblue',size=15)
ax.text2D(0.8,0.03,'The Science Lovers',transform=ax.transAxes,color='azure',size=10)



#Animation
line,=ax.plot([],[],[],linewidth=2,color='white')

s=10 #Speed of the Animation
def animate(i):
	line.set_data(x,[t[s*i]]*m)
	line.set_3d_properties(T[s*i,:],'z')
	A=ax.view_init(elev=20 , azim=150-0.08*s*i)
	return line,A
	
anim = animation.FuncAnimation(fig, animate, frames = 2000, interval = 10)

plt.show()