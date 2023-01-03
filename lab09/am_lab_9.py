#!/usr/bin/env python3

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
import scipy
import math


def rectangular_rule_integration(func, left, right, n_rects):
    x = np.linspace(left, right, n_rects)
    h = (right - left) / n_rects
    y = h * np.sum(func(x)[:-1])

    return y


def fourier_series(ax, func, order, x_resolution):
    """
    ax - subplot to draw on
    func - Function pointer to estimate
    order - Order of the partial sum
    x_resolution - Number of samples on axis x
    
    Returns the fourier series coefficients
    """
    # Create two numpy vectors of length order, they will keep the fourier coefficients
    a_n = np.zeros(order)
    b_n = np.zeros(order)

    # Sample x and calculate f(x)
    x = np.linspace(-np.pi, np.pi, x_resolution)
    fx = func(x)

    # Fill a_0
    a0_func = lambda xs: func(xs)
    a_n[0] = (1 / np.pi) * (scipy.integrate.quad(a0_func, -np.pi, np.pi)[0])

    # Fill a_n and b_n for 1 <= n < order
    an_func = lambda xs: func(xs) * np.cos(xs * n)
    bn_func = lambda xs: func(xs) * np.sin(xs * n)
    for n in range(1, order):
        a_n[n] = (1 / np.pi) * (scipy.integrate.quad(an_func, -np.pi, np.pi)[0])
        b_n[n] = (1 / np.pi) * (scipy.integrate.quad(bn_func, -np.pi, np.pi)[0])

    # Approximate f(x) using the coefficients
    approx = np.zeros(x_resolution)
    for n in range(1, order):
        approx += a_n[n] * np.cos(n * x) + b_n[n] * np.sin(n * x)
    approx += (a_n[0] / 2)

    # Plot fx over x and approxmiation over x. Using different linestyles. Add a legend.
    # DO NOT call plt.show()
    ax.plot(x, fx, linestyle=(0, (1, 1)), color='green', label='f(x)')
    ax.plot(x, approx, linestyle=(5, (10, 3)), color='red', label='f(x) approx')
    ax.legend()
    # Return the two coefficient vectors
    return a_n, b_n


def run(figure):
    ##############################
    ### Change here
    width = 3
    functions = ((11, lambda x: x ** 2, 'x^2'),
                 (2, np.cos, 'cos(x)'),
                 (7, lambda x: x, 'x'),
                 (30, lambda x: np.abs(x), '|x|'),
                 (2, np.sin, 'sin(x)'),
                 (50, lambda x: x ** 3, 'x^3'))
    fig, ax = plt.subplots(math.ceil(len(functions) / width), width)
    for i, of in enumerate(functions):
        axi = ax[i // width, i % width]
        ###
        fourier_series(axi, of[1], of[0], 10000)
        axi.set_title(of[2])
    # Do not change
    if figure is None:
        fig.show()
    else:
        fig.savefig(figure)


if __name__ == '__main__':
    run('pic')
