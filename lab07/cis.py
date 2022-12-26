import numpy as np
import matplotlib.pyplot as plt


def cis(r):
    x = np.linspace(0, 1, 10000)
    theta = r * (np.cos(2 * np.pi * x) + (1j * (np.sin(2 * np.pi * x))))

    fig, ax = plt.subplots()
    ax.plot(theta, theta.real)
    ax.plot(theta, theta.imag)
    ax.legend(['real', 'imag'])
    fig.show()
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, np.ones(theta.shape) * r)
    fig.show()

if __name__ == '__main__':
    cis(5)
