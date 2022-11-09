import numpy as np
from matplotlib import pyplot as plt


def innerProd(v1, v2):
    if np.shape(v1) != np.shape(v2):
        print("Dimension Error")
        return
    else:
        v1 = np.array(v1)
        v2 = np.array(v2).conjugate()

        product = 0
        for n in range(len(v1)):
            product += v1[n] * v2[n]
    return product


Ts = 1 / 44100
x = np.arange(0, 1 - Ts, Ts)
y1 = np.cos(2 * np.pi * 1 * x)
plt.plot(x, y1)
y2 = np.sin(2 * np.pi * 1 * x)
plt.plot(x, y1, 'b', x, y2, 'r')
plt.show()

fs = 44100
Ts = 1 / fs
x = np.arange(0, 1 - Ts, Ts)
u = np.cos(2 * np.pi * x)
v = np.sin(2 * np.pi * x)
print("option 1 : ", innerProd(u, v))
print("option 2 : ", sum(u * v))