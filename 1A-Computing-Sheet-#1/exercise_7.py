import numpy as np
import math
import matplotlib as plt

def friction(v):
    if v < 0: return 0.025
    elif v == 0: return 0
    else: return -0.025

def plot_friction_null():
    k, m, dt, f = 40, 1, 0.01, 0

    t = np.arange(0, 20, dt)
    n = len(t)

    x = np.zeros(n)
    x[0], x[1] = 0.01, 0.01 

    for i in range(2, n):
        x[i] = dt ** 2 / m * f - dt ** 2 * k / m * x[i - 1] + 2 * x[i - 1] - x[i - 2]

    omega = math.sqrt(k / m)

    plt.plot(t, x, label = "Numerical Solution")
    plt.plot(t, 0.01 * math.cos(omega * t), label = "Analytic Solution")

    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.legend()

def plot_friction_not_null():
    k, m, dt= 40, 1, 0.01

    t = np.arange(0, 20, dt)
    n = len(t)

    x = np.zeros(n)
    x[0], x[1] = 0.01, 0.01 

    for i in range(2, n):
        v = (x[i - 1] - x[i - 2])/dt
        x[i] = dt ** 2 / m * friction(v) - dt ** 2 * k / m * x[i - 1] + 2 * x[i - 1] - x[i - 2]

    omega = math.sqrt(k / m)

    plt.plot(t, x, label = "Numerical Solution")
    plt.plot(t, 0.01 * math.cos(omega * t), label = "Analytic Solution")

    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.legend()

def main():
    plot_friction_not_null()
    plot_friction_null()
