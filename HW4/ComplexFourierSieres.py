import numpy as np
import matplotlib.pyplot as plt

# A
def complexFourier(f, cn, res, m):
    x = np.linspace(-np.pi, np.pi, res)
    func = eval(f)
    sm = 0
    for n in range(-m, m + 1):
        try:
            sm += eval(cn) * np.exp(1j * n * x)
        except ZeroDivisionError:
            continue
        stitle = "complex fourier series of " + f1
        plt.title(stitle)
        plt.plot(x, sm)
        plt.plot(x, func)
        plt.show()
    return sm


if __name__ == '__main__':
    #B
    f1 = "np.exp(x)"
    cn1 = '((((-1)**n) * (np.exp(np.pi) - np.exp(-np.pi))) / (2 * np.pi * (1 - 1j * n)))'
    f2 = "x"
    cn2 = '(-((-1)**n)/(1j*n))'

    #C
    y1 = complexFourier(f1, cn1, 400, 10)
    y2 = complexFourier(f2, cn2, 400, 10)
    x = np.linspace(-np.pi, np.pi, 400)
    plt.plot(x, y1)
    plt.plot(x, y2)
