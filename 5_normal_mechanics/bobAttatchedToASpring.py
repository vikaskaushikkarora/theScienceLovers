import time
import os
import multiprocessing
import numpy as np
import matplotlib.pyplot as plt

L0=1
k=10
m=1
a=k/m
g=10

t=np.linspace(0,15,15000)
h=t[1]-t[0]
N=len(t)
x=np.zeros(N)
y=np.zeros(N)
vx=np.zeros(N)
vy=np.zeros(N)

x[0]=0
y[0]=1.1
vx[0]=0.5
vy[0]=0

def fx(x,y):
    r=np.sqrt(x**2+y**2)
    el=r-L0
    return -k*el*x*(r**(-1))

def fy(x,y):
    r=np.sqrt(x**2+y**2)
    el=r-L0
    return g-k*el*y*(r**(-1))

for i in range(N-1):
    x[i+1]=x[i]+h*vx[i]
    y[i+1]=y[i]+h*vy[i]
    vx[i+1]=vx[i]+h*fx(x[i],y[i])
    vy[i+1]=vy[i]+h*fy(x[i],y[i])

#==================================================================

def makeFrame(j,n,pp,s):
  fig=plt.figure()
  ax=fig.add_axes([0,0,1,1])
  for i in range(int(j*n/pp),int((j+1)*n/pp)):
     
    ax.set_xlim(-1.2,1.2)
    ax.set_ylim(-3.5,1.2)
    ax.set_facecolor("black")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.plot([0,x[s*i]],[0,-y[s*i]],'-y')
    ax.plot(x[s*i],-y[s*i],'ro',markersize=15)
    
    string="/sdcard/1_work/images/plot"+str(i)+".png"
    plt.savefig(string,dpi=150)
    print((i/n)*100,"% is complete .")
    ax.clear()

def makeVideo():
    N=len(t)
    s=50 #speed of animation : by reducing data plotted
    pp=20 #Number of parallel processes
    n=int(N/s)
    st=time.time()
    os.system("mkdir /sdcard/1_work/images")
    processes=[]
    for j in range(pp):
        P=multiprocessing.Process(target=makeFrame,args=[j,n,pp,s])
        P.start()
        processes.append(P)  
    
    for process in processes:
        process.join()
        
    os.system("rm /sdcard/1_work/output.mp4")
    os.system("ffmpeg -framerate 24 -i /sdcard/1_work/images/plot%d.png -c:v libx264 -vf format=yuv420p /sdcard/1_work/output.mp4")
        
    ft=time.time()
    print("Total time taken for video making : ",ft-st)
    os.system("rm -r /sdcard/1_work/images")

makeVideo()
