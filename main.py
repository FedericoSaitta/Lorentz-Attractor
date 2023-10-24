import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import  FuncAnimation
from scipy.integrate import odeint
from Point_Class import Point
import timeit
import random




obj_list = []

x_pos = 50 * np.random.randn(50) - 25
y_pos = 50 * np.random.randn(50) - 25
z_pos = 50 * np.random.randn(50)

for i in range(50):
    Point((x_pos[i], y_pos[i], z_pos[i])).lorentz_data()



'''x = Point((5,5,5))
s = Point((5.1,5.1,5.1))
z = Point((5.05,5.05,5.05))

x.lorentz_data()
s.lorentz_data()
z.lorentz_data()'''

start = timeit.default_timer()

Point.make_animation()

print("The difference of time is :", timeit.default_timer() - start)
