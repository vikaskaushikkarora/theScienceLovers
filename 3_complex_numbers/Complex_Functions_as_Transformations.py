# Visuallizing Complex Function as Transformations _______________________________

import numpy as np
import cmath
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
J=cmath.sqrt(-1)
from numpy import sin , cos , exp , pi


#______________________________

def f(z):
	w=z**3
	return w

N=1000
z0=np.linspace(-4,4,N)

a_3=[-3]*N+J*z0
a_2=[-2]*N+J*z0
a_1=[-1]*N+J*z0
a=[0]*N+J*z0
a1=[1]*N+J*z0
a2=[2]*N+J*z0
a3=[3]*N+J*z0

b_3=z0+J*(-3)
b_2=z0+J*(-2)
b_1=z0+J*(-1)
b=z0
b1=z0+J*(1)
b2=z0+J*(2)
b3=z0+J*(3)


#______________________________

fig=plt.figure()
ax = fig.add_axes([0.0005,0.211,0.998,0.568])
ax.set_facecolor('black')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_xticks([])
ax.set_yticks([])
T=1000


line_3,=ax.plot([],[],color='coral')
line_2,=ax.plot([],[],color='coral')
line_1,=ax.plot([],[],color='coral')
line,=ax.plot([],[],color='coral')
line1,=ax.plot([],[],color='coral')
line2,=ax.plot([],[],color='coral')
line3,=ax.plot([],[],color='coral')

iline_3,=ax.plot([],[],color='deepskyblue')
iline_2,=ax.plot([],[],color='deepskyblue')
iline_1,=ax.plot([],[],color='deepskyblue')
iline,=ax.plot([],[],color='deepskyblue')
iline1,=ax.plot([],[],color='deepskyblue')
iline2,=ax.plot([],[],color='deepskyblue')
iline3,=ax.plot([],[],color='deepskyblue')


def animate(i):
	
	s=i*T**(-1)
	def g(z,f):
		G=z*(1+exp(20*(s-0.5)))**(-1)+f(z)*(1-(1+exp(30*(s-0.25)))**(-1))
		return G
	
	line_3.set_data(g(a_3,f).real,g(a_3,f).imag)
	line_2.set_data(g(a_2,f).real,g(a_2,f).imag)
	line_1.set_data(g(a_1,f).real,g(a_1,f).imag)
	line.set_data(g(a,f).real,g(a,f).imag)
	line1.set_data(g(a1,f).real,g(a1,f).imag)
	line2.set_data(g(a2,f).real,g(a2,f).imag)
	line3.set_data(g(a3,f).real,g(a3,f).imag)
	
	iline_3.set_data(g(b_3,f).real,g(b_3,f).imag)
	iline_2.set_data(g(b_2,f).real,g(b_2,f).imag)
	iline_1.set_data(g(b_1,f).real,g(b_1,f).imag)
	iline.set_data(g(b,f).real,g(b,f).imag)
	iline1.set_data(g(b1,f).real,g(b1,f).imag)
	iline2.set_data(g(b2,f).real,g(b2,f).imag)
	iline3.set_data(g(b3,f).real,g(b3,f).imag)
	
	A=ax.set_xlim(-5-0.01*i,5+0.01*i)
	B=ax.set_ylim(-5-0.01*i,5+0.01*i)
	C=ax.text(2+0.4*0.01*i,-4.6-0.85*0.01*i,r'f(z) = $z^{3}$',color='white',size=30)
	
	return line_3,line_2,line_1,line,line1,line2,line3,iline_3,iline_2,iline_1,iline,iline1,iline2,iline3,C

anim = FuncAnimation(fig, animate, frames = T, interval = 10, blit = True)

plt.show()
