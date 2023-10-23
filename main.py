import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import  FuncAnimation
from scipy.integrate import odeint

# Constants:
P = 28
SIG = 10
BETA = 8/3

# Initial conditions for positions
S_0 = (5,5,5)

time = np.linspace(0, 10, 1_000) # Running at 10 FPS for now

# Note S is a vector with components (x,y,z)
def dSdt(S, t):
    x, y, z = S
    return (SIG*(y - x)), (x*(P - z)-y), (x*y - BETA*z)

sol = odeint(dSdt, S_0, time)

pos_x, pos_y, pos_z = sol.T


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.set(xlim= (-40, 40), ylim= (-40, 40), zlim=(-50, 50) )

line, = ax.plot([], [], [], marker= 'o', markersize= 5)
trace, = ax.plot([], [], [], lw= 2)

def animate(i):
    line.set_data([pos_x[i]], [pos_y[i]])
    line.set_3d_properties([pos_z[i]])

    trace.set_data(pos_x[:i], pos_y[:i])
    trace.set_3d_properties(pos_z[:i])

    return line, trace,

anim = FuncAnimation(fig, animate, frames=len(time), interval=20, blit=True)
anim.save('Lorentz.mp4', writer='ffmpeg', fps=60)
print('Animation has been saved')
