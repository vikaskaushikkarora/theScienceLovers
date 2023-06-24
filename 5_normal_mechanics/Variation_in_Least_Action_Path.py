# Calculus of Variations
#Variation in Least Action Path
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider , Button , Cursor
import numpy as np
from numpy import sin , cos , exp , pi

#Creating Simple plot
fig=plt.figure()
ax = fig.add_axes([0.05,0.3,0.9,0.6])
ax.set_ylim(-1,0.5)
ax.grid('False')
ax.set_facecolor('black')
t = np.arange(0.0,2*pi, 0.001)
T=-0.5+0.01*t**2
ax.plot(t,T,color='coral',label=r'Least Action Path i.e. $y_0$')

epsilon=0.1
A=1
B=1
C=1
D=1
E=1

s = T+ epsilon*(A*sin(t)+B*sin(2*t)+C*sin(3*t)+D*sin(4*t)+E*sin(5*t))

l, = ax.plot(t, s, lw=2,label='Path with Variation i.e. y')
ax.set_xticks([])
ax.set_yticks([])
ax.legend(loc=4)

ax.text(np.pi,0.3,r'y = $y_0$ + $\epsilon \eta(x)$',size=18,color='white',ha='center',va='center')

ax.text(np.pi,0.15,r'$\eta(x)$ = A sin(t) + B sin(2t) + C sin(3t) + D sin(4t) + E sin(5t)',size=20,color='white',wrap=True,ha='center',va='center')

ax.text(np.pi,0.4,'VARIATION IN LEAST ACTION PATH',color='yellow',size=20,ha='center',va='center')

#Slider1
ax1=fig.add_axes([0.12,0.015,0.5,0.03])
s1=Slider(ax1,r'A',-3,3,1,valstep=0.1,valfmt='%1.3f',closedmin=False,closedmax=True,color='coral')

#Slider2
ax2=fig.add_axes([0.12,0.06
,0.5,0.03])
s2=Slider(ax2,r'B',-3,3,1,valstep=0.1,valfmt='%1.3f',closedmin=False,closedmax=True,color='coral')

#Slider3
ax3=fig.add_axes([0.12,0.105
,0.5,0.03])
s3=Slider(ax3,r'C',-3,3,1,valstep=0.1,valfmt='%1.3f',closedmin=False,closedmax=True,color='coral')

#Slider4
ax4=fig.add_axes([0.12,0.150
,0.5,0.03])
s4=Slider(ax4,r'D',-3,3,1,valstep=0.1,valfmt='%1.3f',closedmin=False,closedmax=True,color='coral')

#Slider5
ax5=fig.add_axes([0.12,0.195
,0.5,0.03])
s5=Slider(ax5,r'E',-3,3,1,valstep=0.1,valfmt='%1.3f',closedmin=False,closedmax=True,color='coral')

#Slider6
ax6=fig.add_axes([0.12,0.240,0.5,0.03])
s6=Slider(ax6,'$\epsilon$',-0.25,0.25,0.05,valstep=0.01,valfmt='%1.2f',closedmin=False,closedmax=True)

#Changing Values for Sliders
def update(self):
	A = s1.val
	B = s2.val
	C = s3.val
	D = s4.val
	E = s5.val
	epsilon = s6.val
	l.set_ydata(T + epsilon*(A*sin(t)+B*sin(2*t)+C*sin(3*t)+D*sin(4*t)+E*sin(5*t)))
	plt.draw()
s2.on_changed(update)
s1.on_changed(update)
s3.on_changed(update)
s4.on_changed(update)
s5.on_changed(update)
s6.on_changed(update)

#Button1
btn1=fig.add_axes([0.8,0.015,0.1,0.025])
button1=Button(btn1,'Zero',color='lightskyblue',hovercolor='coral')
def reset(event):
	s1.set_val(0)
button1.on_clicked(reset)

#Button2
btn2=fig.add_axes([0.8,0.06,0.1,0.025])
button2=Button(btn2,'Zero',color='lightskyblue',hovercolor='coral')
def reset(event):
	s2.set_val(0)
button2.on_clicked(reset)

#Button3
btn3=fig.add_axes([0.8,0.105,0.1,0.025])
button3=Button(btn3,'Zero',color='lightskyblue',hovercolor='coral')
def reset(event):
	s3.set_val(0)
button3.on_clicked(reset)

#Button4
btn4=fig.add_axes([0.8,0.150,0.1,0.025])
button4=Button(btn4,'Zero',color='lightskyblue',hovercolor='coral')
def reset(event):
	s4.set_val(0)
button4.on_clicked(reset)

#Button5
btn5=fig.add_axes([0.8,0.195,0.1,0.025])
button5=Button(btn5,'Zero',color='lightskyblue',hovercolor='coral')
def reset(event):
	s5.set_val(0)
button5.on_clicked(reset)


plt.show()