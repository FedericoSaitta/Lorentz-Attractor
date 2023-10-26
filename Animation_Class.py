# Class to make animation from data, not only for Lorentz systems
# Class to animate data points pass onto it

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Point_Class import Point
import random as rnd

class Animation:
    def __init__(self, p_objs, time_array, save_anim = True):
        # If save_anim is made False then it will be shown via plt.show()

        self.p_objs = p_objs # List of Point objects to animate
        self.time_array = time_array



    def make_animation(self):
        plt.style.use('dark_background')

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        ax.set(xlim=(-35, 35), ylim=(-35, 35), zlim=(-10, 60))
        plt.axis('off')
        fig.patch.set_alpha(1)

        all_lines = []
        all_traces = []
        for index in range(len(self.p_objs)):
            col = rnd.random(), rnd.random(), rnd.random()
            col = col
            line, = ax.plot([], [], [], marker='o', markersize=1.5, c=col)
            trace, = ax.plot([], [], [], lw=0.4, c=col)
            all_lines.append(line)
            all_traces.append(trace)

        def animate(i):

            for index, line in enumerate(all_lines):
                obj = self.p_objs[index]
                line.set_data([obj.x[i]], [obj.y[i]])
                line.set_3d_properties([obj.z[i]])

            remain = i - 30

            for index, trace in enumerate(all_traces):
                obj = self.p_objs[index]
                if remain > 0:

                    trace.set_data(obj.x[remain:i], obj.y[remain:i])
                    trace.set_3d_properties(obj.z[remain:i])
                else:
                    trace.set_data(obj.x[0:i], obj.y[0:i])
                    trace.set_3d_properties(obj.z[0:i])

            return (obj for obj in all_traces + all_lines)

        anim = FuncAnimation(fig, animate, frames=len(Point.time), interval=20, blit=True)

        anim.save('test_class.mp4', writer='ffmpeg', fps=20, savefig_kwargs={'facecolor': 'black'})
        print('Animation has been saved')


