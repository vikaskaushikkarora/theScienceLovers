#Chaos in Double Pendulum 
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg
t_stop = 20  # how many seconds to simulate


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0, t_stop, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)

th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1


# Other initial conditions woth slight variration from the first 

ath1 = 120.05
aw1 = 0.0
ath2 = -10.05
aw2 = 0.0

astate = np.radians([ath1, aw1, ath2, aw2])

ay = integrate.odeint(derivs, astate, t)

ax1 = L1*sin(ay[:, 0])
ay1 = -L1*cos(ay[:, 0])

ax2 = L2*sin(ay[:, 2]) + ax1
ay2 = -L2*cos(ay[:, 2]) + ay1


# Other initial conditions woth slight variration from the first 

bth1 = 119.95
bw1 = 0.0
bth2 = -9.95
bw2 = 0.0

bstate = np.radians([bth1, bw1, bth2, bw2])

by = integrate.odeint(derivs, bstate, t)

bx1 = L1*sin(by[:, 0])
by1 = -L1*cos(by[:, 0])

bx2 = L2*sin(by[:, 2]) + bx1
by2 = -L2*cos(by[:, 2]) + by1


#Plotting

fig = plt.figure()
ax = fig.add_axes([0.005,0.005,0.99,0.99])
ax.set_aspect('equal')
ax.grid(color='white',ls='-.',lw=1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-2,2)
ax.set_ylim(-2.8,2.8)

line1, = ax.plot([],[],'o-',color='deepskyblue',)
line2,=ax.plot([],[],'yo-')
line3,=ax.plot([],[],'go-')
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.1, '', transform=ax.transAxes,color='white')
ax.text(-1.2,1.5,r'Double Pendulum',size=25,style='oblique',color='white')
ax.text(-0.8,-2.45,'The initial conditions are very slightly different but \n over the course of time , they take very different \n trajectories : This is chaos ... ',color='white')
facecolor=ax.set_facecolor('black')
plt.rcParams['axes.facecolor'] = 'black'



def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    athisx=[0,ax1[i],ax2[i]]
    athisy=[0,ay1[i],ay2[i]]
    bthisx=[0,bx1[i],bx2[i]]
    bthisy=[0,by1[i],by2[i]]
    line1.set_data(thisx, thisy)
    line2.set_data(athisx,athisy)
    line3.set_data(bthisx,bthisy)
    time_text.set_text(time_template % (i*dt))
    return line1,line2,line3,time_text


anim = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=False)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=5000)
anim.save('/sdcard/video.mp4', writer=writer)
