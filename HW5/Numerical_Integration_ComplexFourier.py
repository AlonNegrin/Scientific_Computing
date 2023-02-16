from functools import partial
import numpy as np
import scipy
import matplotlib.pyplot as plt


def intergrate_by_rects(func, a, b, n):
    x = np.linspace(a, b, n)
    f = func(x)
    h = (b - a) / n
    y = h * np.sum(f[:-1])

    return y


def integrate_by_simpson(func, a, b, n):
    if n % 2 != 0:
        return
    x = np.linspace(a, b, n + 1)
    f = func(x)
    f[1:-1:2] *= 4
    f[2:-2:2] *= 2
    h = (b - a) / n

    y = h / 3 * np.sum(f)
    return y


def integrate_by_trapezoids(func, a, b, n):
    x = np.linspace(a, b, n)
    f = func(x)
    h = (b - a) / n
    y = h / 2 * (f[0] + f[-1] + 2 * np.sum(f[1:-1]))
    return y


def num_integral(func, a, b, n, method='simpson'):
    if method == 'trapez':
        return integrate_by_trapezoids(func, a, b, n)
    if method == 'darboux':
        return intergrate_by_rects(func, a, b, n)
    return integrate_by_simpson(func, a, b, n)


def FourierEstComplex(m, N, func, xl=-np.pi, xr=np.pi, method='darboux'):
    x = np.linspace(xl, xr, N)
    fx = func(x)
    if method != 'quad':
        integral = partial(num_integral, a=xl, b=xr, n=N, method=method)
    else:
        integral = lambda f: scipy.integrate.quad(f, a=xl, b=xr)[0]

    fn = lambda x: func(x) * np.exp(-1j * 2 * np.pi * n * x / (b - a))
    approx = np.zeros(N, dtype='complex128')
    for n in range(-m, m + 1):
        cn = integral(fn) * (1 / (b - a))
        approx += cn * np.exp((1 / (b - a)) * 2 * np.pi * 1j * n * x)

    fig, ax = plt.subplots(1)
    ax.plot(x, approx, color='purple', label='approx')
    ax.plot(x, fx, color='orange', label='f(x)')
    ax.legend()
    plt.show()
    return np.sum(approx)


if __name__ == '__main__':
    f = lambda xs: xs * np.exp(-xs)
    a = 0
    b = 2
    n = 100
    FourierEstComplex(40, 150, f, a, b, 'darboux')
