# Complex numbers

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

j=(sp.sqrt(-1))
#You dont need actually scipy here to write the values of z and w here , because the variable type complex is already defined in python ; here if you write z=2+1j , that does not mean you are multiplying 1 and j which is squre root of -1 ; rather it is a way of defining the conplex variable such that it's real part is 2 and imaginary is 1 . But why do we define j=sp.sqrt(-1) in the first place ? Because we will need it when we defone some complex valued functions ....

z=5+3j
w = 2.5+0.2j

print('Complex Number 1 : ')
print(z)
print(type(z))
print('')
print('Complex Number 2 : ')
print(w)
print(type(w))
print('')

a=z.real
print('Real Part : ')
print(a)
print(type(a))
print('')

b=z.imag
print('Imaginary Part : ')
print(b)
print(type(b))
print('')

def modulus(w):
	return ((w.real)**2+(w.imag)**2)**(0.5)

print('Modulus of z : ')
print(modulus(z))
print('')

def conj(w):
	c =(w.real)-(w.imag)*j
	return c

print('Conjugate of z :')
print(conj(z))
print('')

#Alzbraic Operations :

s = z+w
print('Sum : ')
print(s)
print('')

sub = z-w
print('Subtraction : ')
print(sub)
print('')

mul = z*w
print('Multiplication : ')
print(mul)
print('')

div = z/w
print('Division : ')
print(div)
print('')

#Plotting : 

plt.plot([0,z.real],[0,z.imag],'bo-',linewidth=2,label='z')
plt.plot([0,w.real],[0,w.imag],'ko-',linewidth=2,label='w')
plt.plot([0,conj(z).real],[0,conj(z).imag],'bo-.',linewidth=2,label='conj(z)')
plt.plot([0,s.real],[0,s.imag],'co-',linewidth=2,label='sum')
plt.plot([0,sub.real],[0,sub.imag],'o-',color='green',linewidth=2,label='subtraction')
plt.legend(loc='upper left')
plt.text(z.real,z.imag,'z',size=20)
plt.text(conj(z).real,conj(z).imag,'conj(z)',size=20)
plt.text(sub.real,sub.imag,'z-w',size=20)
plt.text(w.real,w.imag,'w',size=20)
plt.text(s.real,s.imag,'z+w',size=20)
plt.xticks([])
plt.yticks([])
plt.show()