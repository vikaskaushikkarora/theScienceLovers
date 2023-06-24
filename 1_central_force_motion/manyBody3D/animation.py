# Making animation from the given data using Multi Processing in drawing seperate images by matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import os
import multiprocessing

st=time.time()
os.system("mkdir images")

t=np.loadtxt("data/tdata.txt");
T=len(t)
x=np.loadtxt("data/xdata.txt")
y=np.loadtxt("data/ydata.txt")
z=np.loadtxt("data/zdata.txt")
m=20

s=3 #speed of animation : by reducing data plotted
pp=5 #Number of parallel processes
N = T
n=int(N/s)
#Draw Each Frame Here using Matplotlib
def makeVideo(j):
  fig = plt.figure()
  ax = Axes3D(fig)
  ax.set_aspect('auto')
  ax.set_facecolor('black')

  for i in range(int(j*n/pp),int((j+1)*n/pp)):
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_zlim(-10,10)
    ax.set_facecolor("black")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_axis_off()
    ax.view_init(elev=15 , azim=-35+0.8*i)
    ax.quiver(0,0,0,5,0,0,cmap='Reds',length=3,lw=1,normalize=False,arrow_length_ratio=0.1)
    ax.quiver(0,0,0,0,5,0,cmap='Reds',length=3,lw=1,normalize=False,arrow_length_ratio=0.1)
    ax.quiver(0,0,0,0,0,5,cmap='Reds',length=3,lw=1,normalize=False,arrow_length_ratio=0.1)
    for j in range(m):
      ax.plot(x[s*i],y[s*i],z[s*i],'ro')

    string="images/plot"+str(i)+".png"
    plt.savefig(string,dpi=100)
    print((i/n)*100,"% is complete .")
    ax.clear()

processes=[]
for j in range(pp):
  P=multiprocessing.Process(target=makeVideo,args=[j])
  P.start()
  processes.append(P)
  
for process in processes:
  process.join()

os.system("rm output.mp4")
os.system("ffmpeg -framerate 24 -i images/plot%d.png -c:v libx264 -vf format=yuv420p output.mp4")

ft=time.time()
print("Total time taken : ",ft-st)
os.system("rm -r images")
