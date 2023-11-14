import numpy as np
from Point_Class import Point
from Animation_Class import Animation
import timeit


x_pos = (np.pi /2 * np.random.randn(50))
y_pos = 0.5 * np.random.randn(50)


for i in range(50):
    S_0 = (x_pos[i], y_pos[i])
    Point(S_0, np.linspace(0,30, 600)).pendulum_data()

a = Animation(Point.Pendulum_objs, np.linspace(0, 30, 600))


start = timeit.default_timer()


print(Point.Pendulum_objs)
a.make_pendulum_animation()




print("The difference of time is :", timeit.default_timer() - start)
