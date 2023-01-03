import numpy as np


def intergrate(func, a, b, n):
    x = np.linspace(a, b, n)
    f = eval(func)
    h = (b - a) / n
    y = h * np.sum(f[:-1])

    return y


print(intergrate('x**2', 0, 1, 10000))




















print("matan yesh tzionim")