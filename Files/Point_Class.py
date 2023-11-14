# This is to create a point object that will follow a path according to different sets of ODEs
import numpy as np
from scipy.integrate import odeint
import random as ran

# Tried many different types of spacing models and in the end a simple quadratic or x^n where 1 < n <= 2 works
# by far the best, more complicated models often only yield better results when tweaking other parameters too


class Point:
    '''    a = np.linspace(0, 1, 750)
    b = np.linspace(1, np.sqrt(3), 500)
    c = np.linspace(np.sqrt(3), np.sqrt(5), 250)
    time = np.hstack((a, b, c))

    time = time ** 2'''
    time = np.linspace(0, 30, 600)

    Lorentz_objs, Pendulum_objs = [], []


    def __init__(self, S_0, time): # Z component is initialized but may not be used
        self.x, self.y, self.z = [], [], []

        self.S_0 = S_0 # Starting conditions vector
        self.time = time

    def lorentz_data(self):
        Point.Lorentz_objs.append(self)

        sol = odeint(Point.__dSdt_Lorentz__, self.S_0, Point.time)
        self.x, self.y, self.z = sol.T


    def pendulum_data(self): # Note this is for a 2D pendulum
        Point.Pendulum_objs.append(self)

        sol = odeint(Point.__dSdt_Pendulum__, self.S_0, Point.time)
        self.x, self.y = sol.T



    """
    These are all the ODE equations that go into odeint, maybe make your own one day
    """
    @staticmethod
    def __dSdt_Lorentz__(S_0, t):
        P = 28
        SIG = 10
        BETA = 8 / 3
        x, y, z = S_0

        return (SIG * (y - x)), (x * (P - z) - y), (x * y - BETA * z)

    @staticmethod
    def __dSdt_Pendulum__(S_0, t):
        theta, omega = S_0

        return omega, -np.sin(theta)

