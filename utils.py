import numpy as np
import matplotlib.pyplot as plt
import time


# N = x-axis resolution
# a0,an,bn -> string
def fourierSynthesis(a0, an, bn, function, m, N):
    xAxis = np.linspace(-np.pi, np.pi, N)  # create an x Axis from [-pi , pi] with N steps
    f = eval(function)
    plt.figure(1)
    plt.plot(xAxis, f, 'r')
    y = np.zeros(xAxis.size)
    eps = 1e-14

    Sm = np.zeros(xAxis.size, ) + a0 / 2  # my end sum

    for n in range(1, m):
        a_n = eval(an)
        b_n = eval(bn)
        Sm += a_n * np.cos(n * xAxis)
        Sm += b_n * np.sin(n * xAxis)
        plt.figure(1)
        plt.pause(1)
        plt.plot(xAxis, Sm)
        plt.grid(axis='both')
        stitle = 'Fourier series part sum, n = ' + str(n)
        plt.title(stitle)
        plt.figure(1)
        plt.plot(xAxis, f, 'r')
        plt.show()

    y = Sm
    return y


# f(x) = x
a0 = 0
an = "0"
bn = "(2*(-1)**(n+1))/n"
f = 'x'
y = fourierSynthesis(a0, an, bn, f, 50, 10000)
