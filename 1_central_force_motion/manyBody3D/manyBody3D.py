#Many Body 3D

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

n=20 # no.of objects
M=10*rd.rand(n)

#Time and Coordinates

h=0.01
t=np.arange(0,20,h)
T=len(t)

x=np.zeros((T,n))
y=np.zeros((T,n))
z=np.zeros((T,n))
vx=np.zeros((T,n))
vy=np.zeros((T,n))
vz=np.zeros((T,n))

#initial conditions

x=0.001*rd.randint(-10000,10000,size=(T,n))
y=0.001*rd.randint(-10000,10000,size=(T,n))
z=0.001*rd.randint(-10000,10000,size=(T,n))
vx=0.00002*rd.randint(-10000,10000,size=(T,n))
vy=0.00002*rd.randint(-10000,10000,size=(T,n))
vz=0.000002*rd.randint(-10000,10000,size=(T,n))
	
#print(x)
#print(y)
#print(z)

filet=open('data/tdata.txt','w');
filex=open('data/xdata.txt','w');
filey=open('data/ydata.txt','w');
filez=open('data/zdata.txt','w');

for i in range (T-1):
  filet.write(str(t[i])+'\t')
  for j in range (n):
    sum1=0;
    for k in range(n):
      if (k != j) :
        sum1=sum1+M[k]*(x[i,k]-x[i,j])*((x[i,k]-x[i,j])**2+(y[i,k]-y[i,j])**2+(z[i,k]-z[i,j])**2)**(-1.5)
      else :
        sum1=sum1;
    vx[i+1,j]=vx[i,j]+h*sum1;
    x[i+1,j]=x[i,j]+h*vx[i+1,j];
    
    sum2=0
    for s in range (n):
      if (s != j) :
        sum2=sum2+M[s]*(y[i,s]-y[i,j])*((x[i,s]-x[i,j])**2+(y[i,s]-y[i,j])**2+(z[i,s]-z[i,j])**2)**(-1.5)
      else :
        sum2=sum2
    vy[i+1,j]=vy[i,j]+h*sum2
    y[i+1,j]=y[i,j]+h*vy[i+1,j]
    
    sum3=0
    for p in range (n):
      if p != j :
        sum3=sum3+M[p]*(z[i,p]-z[i,j])*((x[i,p]-x[i,j])**2+(y[i,p]-y[i,j])**2+(z[i,p]-z[i,j])**2)**(-1.5)
      else :
        sum3=sum3
    vz[i+1,j]=vz[i,j]+h*sum3
    z[i+1,j]=z[i,j]+h*vz[i+1,j]
    
    filex.write(str(x[i,j])+'\t')
    filey.write(str(y[i,j])+'\t')
    filez.write(str(z[i,j])+'\t')
  filex.write('\n')
  filey.write('\n')
  filez.write('\n')

filet.close()
filex.close()
filex.close()
filex.close()