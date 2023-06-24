# The distribution of particles in the left and right half of the box reaching Equllibrium with the passage of time
import numpy as np
import matplotlib.pyplot as plt
T=100000 # Time Window
t=np.linspace(0,4,T)
N=30000 #Total number of particles in the box
n=np.zeros(T) # Number of particles in left half at any time 't'
n[0]=N #Initial number of particles in left half
for i in range (1,len(t)):
	r=np.random.rand(1,1) # assigning a random probability of crossing from left to right
	if r<n[i-1]/N :
		#'(n(i-1)/N' represents the average possiblity of particle going from   left to right , if the random possiblity lies between zero to avergae possiblity , then the particle goes to right
		n[i]=n[i-1]-1
	else :
		n[i]=n[i-1]+1 #else the particle goes from right to left ( You can remove +1 if the particles from right dont come into right half or increase the possiblity of paricles going from right to left by adding 2 and so on ...)//
plt.plot(t,n/N,'k-')
#plt.plot(t,0.5+0.5*np.exp(-1.7*t),'r')
plt.plot(t,1-(n/N),'b-')
plt.legend(['Particles in left box','Particles in right box'])
plt.xlabel('Time window')
plt.ylabel('No. of particles in left half ')
plt.grid()
plt.show()
