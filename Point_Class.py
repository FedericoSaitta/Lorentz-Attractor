# This is to create a point object that will follow a path according to different sets of ODEs
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import  FuncAnimation
from scipy.integrate import odeint
import random as ran


class Point:
    time = np.linspace(0, 10, 2_500)

    Lorentz_objs = []


    def __init__(self, S_0): # Note S_0 needs to always be a tuple with 3 components
        self.x = []
        self.y = []
        self.z = []

        self.S_0 = S_0

    def lorentz_data(self):
        Point.Lorentz_objs.append(self)

        sol = odeint(Point.dSdt, self.S_0, Point.time)
        self.x, self.y, self.z = sol.T


    def dSdt(S, t):
        P = 28
        SIG = 10
        BETA = 8 / 3
        x, y, z = S

        return (SIG * (y - x)), (x * (P - z) - y), (x * y - BETA * z)

    @staticmethod
    def make_animation():
        plt.style.use('dark_background')

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')


        ax.set(xlim=(-25, 25), ylim=(-25, 25), zlim=(0, 50))
        plt.axis('off')
        fig.patch.set_alpha(1)


        line, = ax.plot([], [], [], marker='o', markersize=5)
        trace, = ax.plot([], [], [], lw=1)

        colours = ['red', 'black', 'orange']

        all_lines = []
        all_traces = []
        for index in range(len(Point.Lorentz_objs)):
            col = ran.random(), ran.random(), ran.random()
            col = col
            line, = ax.plot([], [], [], marker='o', markersize=3, c=col)
            trace, = ax.plot([], [], [], lw=0.5, c=col)
            all_lines.append(line)
            all_traces.append(trace)




        def animate(i):
            ax.view_init(elev=0., azim= (i/10))
            for index, line in enumerate(all_lines):
                obj = Point.Lorentz_objs[index]
                line.set_data([obj.x[i]], [obj.y[i]])
                line.set_3d_properties([obj.z[i]])

            remain = i - 30

            for index, trace in enumerate(all_traces):
                obj = Point.Lorentz_objs[index]
                if remain > 0:

                    trace.set_data(obj.x[remain:i], obj.y[remain:i])
                    trace.set_3d_properties(obj.z[remain:i])
                else:
                    trace.set_data(obj.x[0:i], obj.y[0:i])
                    trace.set_3d_properties(obj.z[0:i])

            return (obj for obj in all_traces + all_lines)


        anim = FuncAnimation(fig, animate, frames=len(Point.time), interval=20, blit= True)

        anim.save('testing.mp4', writer='ffmpeg', fps=40,  savefig_kwargs={'facecolor':'black'})
        print('Animation has been saved')



    def pendulum_data(self):
        pass
