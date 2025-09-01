import numpy as np
from math import *

# Constants
g = 9.8     # acceleration due to gravity (m/s^2)
L = 1       # length of pendulum (m)

# Function definitions
def f(t, u, v):
    return v

def b(t, u, v):
    return (-g / L) * sin(u)

# Runge-Kutta 4th order method to simulate pendulum and estimate time period
def RK4(t0, u0, v0, h):
    t, u, v = t0, u0, v0
    initial_angle = u0
    first_pass = True

    for t in np.arange(t, 20 + h, h):
        print(round(t, 4), '\t', round(u, 4), '\t', round(v, 4))

        # Detect full period: angle returns near start with upward motion
        if not first_pass and abs(u - initial_angle) < 0.001 and v > 0:
            print("Estimated period:", round(t, 4))
            break

        if u < initial_angle:
            first_pass = False

        # RK4 updates
        K1 = h * f(t, u, v)
        L1 = h * b(t, u, v)

        K2 = h * f(t + h / 2, u + K1 / 2, v + L1 / 2)
        L2 = h * b(t + h / 2, u + K1 / 2, v + L1 / 2)

        K3 = h * f(t + h / 2, u + K2 / 2, v + L2 / 2)
        L3 = h * b(t + h / 2, u + K2 / 2, v + L2 / 2)

        K4 = h * f(t + h, u + K3, v + L3)
        L4 = h * b(t + h, u + K3, v + L3)

        u = u + (K1 + 2 * K2 + 2 * K3 + K4) / 6
        v = v + (L1 + 2 * L2 + 2 * L3 + L4) / 6

# Initial values
RK4(t0=0, u0=1, v0=0, h=0.01)