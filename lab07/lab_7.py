#!/usr/bin/env python3

import matplotlib

matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional


def polar(z: complex) -> Tuple[float, float]:
    # Returns r and theta
    # Your code here:
    re = z.real
    im = z.imag
    r = np.sqrt(re ** 2 + im ** 2)
    theta = np.arctan(re / im)
    return r, theta


def get_roots(z: complex, n: int) -> np.ndarray:
    # Returns an array of n complex numbers, representing the n roots of z
    roots = np.zeros((n,), dtype=np.complex64)
    ### Your code here

    r, theta = polar(z)
    for k in range(0, n):
        roots[k] = r ** (1 / n) * (np.cos((theta + 2 * np.pi * k) / n) + 1j * (np.sin((theta + 2 * np.pi * k) / n)))
    ###
    return roots


def plot_roots(z: complex, n: int):
    # Plot the n roots of the complex number z
    # Your code here

    roots = get_roots(z, n)
    x = np.zeros((roots.shape[0] + 1))
    y = np.zeros((roots.shape[0] + 1))

    for i in range(len(x) - 1):
        x[i] = roots[i].real
        y[i] = roots[i].imag

    x[len(x)-1] = x[0]
    y[len(y)-1] = y[0]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    fig.savefig('fig3.png')


def run(z: complex, n: int, figure: Optional[str]):
    plt.close()
    plot_roots(z, n)
    if figure is None:
        plt.show()
    else:
        plt.savefig(figure)


if __name__ == '__main__':
    run(z=5 + 7j,
        n=12,
        figure='fig.png')


