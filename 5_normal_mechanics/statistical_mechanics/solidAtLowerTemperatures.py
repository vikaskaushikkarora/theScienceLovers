#Acoustic Wave
#centre of fig :(3,1)
#centre of text :(5,1)
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
#create figure and axies
fig = plt.figure() 
ax = fig.add_axes([0.0005,0.211,0.998,0.568])

#Set x and y limits 
ax.set_xlim(-40,40)
ax.set_ylim(-1.5,1.5)
#make background black
ax.set_facecolor('black')
#gridlines to keep track 
ax.grid(ls='-.',lw=0.5,color='white')
#if you want to remove the ticks on axies including gridlines
ax.set_xticks([])
ax.set_yticks([])

#line object : plotting variable point
n=5
line,=ax.plot([],[],'o',color='skyblue',markersize=n)
line1,=ax.plot([],[],'o',color='skyblue',markersize=n)
line2,=ax.plot([],[],'o',color='skyblue',markersize=n)
line3,=ax.plot([],[],'o',color='skyblue',markersize=n)
line4,=ax.plot([],[],'o',color='skyblue',markersize=n)
line5,=ax.plot([],[],'o',color='skyblue',markersize=n)
line6,=ax.plot([],[],'o',color='skyblue',markersize=n)
line7,=ax.plot([],[],'o',color='skyblue',markersize=n)
line8,=ax.plot([],[],'o',color='skyblue',markersize=n)
line9,=ax.plot([],[],'o',color='skyblue',markersize=n)
line10,=ax.plot([],[],'o',color='skyblue',markersize=n)
line11,=ax.plot([],[],'o',color='skyblue',markersize=n)
line12,=ax.plot([],[],'o',color='skyblue',markersize=n)
line13,=ax.plot([],[],'o',color='skyblue',markersize=n)
line14,=ax.plot([],[],'o',color='skyblue',markersize=n)
line15,=ax.plot([],[],'o',color='skyblue',markersize=n)
line16,=ax.plot([],[],'o',color='skyblue',markersize=n)
line17,=ax.plot([],[],'o',color='skyblue',markersize=n)
line18,=ax.plot([],[],'o',color='skyblue',markersize=n)
line18,=ax.plot([],[],'o',color='skyblue',markersize=n)
line19,=ax.plot([],[],'o',color='skyblue',markersize=n)
line20,=ax.plot([],[],'o',color='skyblue',markersize=n)
line21,=ax.plot([],[],'o',color='skyblue',markersize=n)
line22,=ax.plot([],[],'o',color='skyblue',markersize=n)
line23,=ax.plot([],[],'o',color='skyblue',markersize=n)
line24,=ax.plot([],[],'o',color='skyblue',markersize=n)
line25,=ax.plot([],[],'o',color='skyblue',markersize=n)
line26,=ax.plot([],[],'o',color='skyblue',markersize=n)
line27,=ax.plot([],[],'o',color='skyblue',markersize=n)
line28,=ax.plot([],[],'o',color='skyblue',markersize=n)
line29,=ax.plot([],[],'o',color='skyblue',markersize=n)
line30,=ax.plot([],[],'o',color='skyblue',markersize=n)
line31,=ax.plot([],[],'o',color='skyblue',markersize=n)
line32,=ax.plot([],[],'o',color='skyblue',markersize=n)
line33,=ax.plot([],[],'o',color='skyblue',markersize=n)
line34,=ax.plot([],[],'o',color='skyblue',markersize=n)
line35,=ax.plot([],[],'o',color='skyblue',markersize=n)
line36,=ax.plot([],[],'o',color='skyblue',markersize=n)
line37,=ax.plot([],[],'o',color='skyblue',markersize=n)
line38,=ax.plot([],[],'o',color='skyblue',markersize=n)
line39,=ax.plot([],[],'o',color='skyblue',markersize=n)


def init():
	line.set_data([],[])
	line1.set_data([],[])
	line2.set_data([],[])
	line3.set_data([],[])
	line4.set_data([],[])
	line5.set_data([],[])
	line6.set_data([],[])
	line7.set_data([],[])
	line8.set_data([],[])
	line9.set_data([],[])
	line10.set_data([],[])
	line11.set_data([],[])
	line12.set_data([],[])
	line13.set_data([],[])
	line14.set_data([],[])
	line15.set_data([],[])
	line16.set_data([],[])
	line17.set_data([],[])
	line18.set_data([],[])
	line19.set_data([],[])
	line20.set_data([],[])
	line21.set_data([],[])
	line22.set_data([],[])
	line23.set_data([],[])
	line24.set_data([],[])
	line25.set_data([],[])
	line26.set_data([],[])
	line27.set_data([],[])
	line28.set_data([],[])
	line29.set_data([],[])
	line30.set_data([],[])
	line31.set_data([],[])
	line32.set_data([],[])
	line33.set_data([],[])
	line34.set_data([],[])
	line35.set_data([],[])
	line36.set_data([],[])
	line37.set_data([],[])
	line38.set_data([],[])
	
	return line,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line28,line29,line30,line31,line32,line33,line34,line35,line36,line37,line38
		
		
t=np.arange(0,5,0.01)
		
		
		
def animate(i):
	w=0.7
	k=3.5
	x1=0.1
	x2=0.2
	x3=0.3
	x4=0.4
	x5=0.5
	x6=0.6
	x7=0.7
	x8=0.8
	x9=0.9
	x10=1.0
	x11=1.1
	x12=1.2
	x13=1.3
	x14=1.4
	x15=1.5
	x16=1.6
	x17=1.7
	x18=1.8
	x19=1.9
	x20=-0.1
	x21=-0.2
	x22=-0.3
	x23=-0.4
	x24=-0.5
	x25=-0.6
	x26=-0.7
	x27=-0.8
	x28=-0.9
	x29=-1.0
	x30=-1.1
	x31=-1.2
	x32=-1.3
	x33=-1.4
	x34=-1.5
	x35=-1.6
	x36=-1.7
	x37=-1.8
	x38=-1.9
	
	
	def f(x):
		z=x+0.01*(np.random.rand())*(np.sin((np.random.rand())))
		return z	
	
	b=np.arange(-1,1,0.1)
	a=f(0)*len(b)
	a1=f(x1)*len(b)
	a2=f(x2)*len(b)
	a3=f(x3)*len(b)
	a4=f(x4)*len(b)
	a5=f(x5)*len(b)
	a6=f(x6)*len(b)
	a7=f(x7)*len(b)
	a8=f(x8)*len(b)
	a9=f(x9)*len(b)
	a10=f(x10)*len(b)
	a11=f(x11)*len(b)
	a12=f(x12)*len(b)
	a13=f(x13)*len(b)
	a14=f(x14)*len(b)
	a15=f(x15)*len(b)
	a16=f(x16)*len(b)
	a17=f(x17)*len(b)
	a18=f(x18)*len(b)
	a19=f(x19)*len(b)
	a20=f(x20)*len(b)
	a21=f(x21)*len(b)
	a22=f(x22)*len(b)
	a23=f(x23)*len(b)
	a24=f(x24)*len(b)
	a25=f(x25)*len(b)
	a26=f(x26)*len(b)
	a27=f(x27)*len(b)
	a28=f(x28)*len(b)
	a29=f(x29)*len(b)
	a30=f(x30)*len(b)
	a31=f(x31)*len(b)
	a32=f(x32)*len(b)
	a33=f(x33)*len(b)
	a34=f(x34)*len(b)
	a35=f(x35)*len(b)
	a36=f(x36)*len(b)
	a37=f(x37)*len(b)
	a38=f(x38)*len(b)
	
	
	
	line.set_data(a,b)
	line1.set_data(a1,b)
	line2.set_data(a2,b)
	line3.set_data(a3,b)
	line4.set_data(a4,b)
	line5.set_data(a5,b)
	line6.set_data(a6,b)
	line7.set_data(a7,b)
	line8.set_data(a8,b)
	line9.set_data(a9,b)
	line10.set_data(a10,b)
	line11.set_data(a11,b)
	line12.set_data(a12,b)
	line13.set_data(a13,b)
	line14.set_data(a14,b)
	line15.set_data(a15,b)
	line16.set_data(a16,b)
	line17.set_data(a17,b)
	line18.set_data(a18,b)
	line19.set_data(a19,b)
	line20.set_data(a20,b)
	line21.set_data(a21,b)
	line22.set_data(a22,b)
	line23.set_data(a23,b)
	line24.set_data(a24,b)
	line25.set_data(a25,b)
	line26.set_data(a26,b)
	line27.set_data(a27,b)
	line28.set_data(a28,b)
	line29.set_data(a29,b)
	line30.set_data(a30,b)
	line31.set_data(a31,b)
	line32.set_data(a32,b)
	line33.set_data(a33,b)
	line34.set_data(a34,b)
	line35.set_data(a35,b)
	line36.set_data(a36,b)
	line37.set_data(a37,b)
	line38.set_data(a38,b)
	return line,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line28,line29,line30,line31,line32,line33,line34,line35,line36,line37,line38

ax.text(-29,1.05,'Solid at Lower Temperatures ',color='seagreen',size=28)

#Logo Text :
ax.text(22,-1.4,'The Science Lovers',color='white',size=10)

anim = FuncAnimation(fig, animate, init_func = init, frames = 500, interval = 1, blit = True)



plt.show() 
