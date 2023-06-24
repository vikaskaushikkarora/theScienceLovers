import numpy
import matplotlib.pyplot

A=numpy.loadtxt("Data.txt");
x1=A[:,1];
x2=A[:,2];
x3=A[:,3];
y1=A[:,4];
y2=A[:,5];
y3=A[:,6];

matplotlib.pyplot.plot(x1,y1,'-r');
matplotlib.pyplot.plot(x2,y2,'-b');
matplotlib.pyplot.plot(x3,y3,'-g');

matplotlib.pyplot.savefig("graph.png",dpi=200);