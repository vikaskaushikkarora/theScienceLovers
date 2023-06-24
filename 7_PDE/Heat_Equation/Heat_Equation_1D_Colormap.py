#Heat Diffusion in Rod _______________________________


#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 



#Define Time and Space Meshgrid
n=7000 #Time Steps
m=120 #Space Steps
t=np.linspace(0,3,n)
h=t[2]-t[1] #Time Interval
x=np.linspace(-1,1,m)
k=x[2]-x[1] #Space Interval
T=np.zeros((n,m)) #Temp.
a=0.3 # Conductivity
b=h*a*k**(-2)



#______________________________
#Initial Conditions :-
for j in range(0,m):
	T[0,j]=-1+2.8*np.exp(-20*(x[j]+0.25)**2)-3*np.exp(-15*(x[j]-0.5)**2)


#Finite Difference Method
#Iterations :-
for i in range (n-1):
	for j in range (1,m-1):
		T[i+1,j]=(1-2*b)*T[i,j]+b*(T[i,j+1]+T[i,j-1]) 
		
	# Boundary Conditions
	# (The temperature gradient at boundaries is zero i.e. heat does not flow at the ends )
	T[i+1,0]=T[i+1,1]
	T[i+1,m-1]=T[i+1,m-2]



#______________________________
#Animation
fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])

#Colormap
u=np.zeros((n,m))
for i in range(n):
	u[i,:]=T[i,:]
for i in range(n):
	u[i,0]=u[0,0]
	u[i,m-1]=u[0,m-1]


for i in range(3500):
	ax.set_facecolor('black')
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_xlim(-1.2,1.2)
	ax.set_ylim(-6,5)
	#Making sure that initial condition remain visible for sometime
	if i < 10 :
		ax.plot(x,T[0,:],color='deepskyblue')
		ax.scatter(x,[-5]*m,c=u[0,:],cmap='plasma',s=150)
	else :
		ax.plot(x,T[4*(i-10),:],color='deepskyblue')
		ax.scatter(x,[-5]*m,c=u[4*(i-10),:],cmap='plasma',s=150)
	#Fixing endpoints' color and Making scatter of points look like a rod
	ax.scatter(1,-5,s=400,c='black')
	ax.scatter(-1,-5,s=400,c='black')
	#Labelling and Axes
	ax.quiver(-1.05,-4.5,0,20,scale=23,width=0.002,headwidth=10,color='white')
	ax.text(-1,3,'Temp.',size=12,color='white')
	ax.text(0.5,2.05,'As you can see that the \ncurve smoothes out over \ntime . And this is the general behaviour of diffusion equations .',color='azure',size=20,ha='center',wrap=True)
	ax.text(0.9,-4.6,'Rod',size=15,color='white')
	plt.pause(0.1)
	ax.clear()
	
plt.show()

