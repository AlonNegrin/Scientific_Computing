import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

from functools import partial
from matplotlib.animation import FuncAnimation
import numpy as np


def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield b
        a, b = b, a + b
    return None


def plot_fib(fn, ax, matrix_p):
    matrix = matrix_p[0]
    
    matrix = np.roll(matrix, (fn, fn), axis=(0, 1))
    
    matrix[:fn, 0, 0] = 1
    matrix[:fn, fn-1, 1] = 1
    matrix[0, :fn, 2] = 1
    matrix[fn-1, :fn, :2] = 1
    
    ax.imshow(matrix)
    
    matrix_p[0] = matrix


def plot_rotation(fn, ax, matrix_p):
    matrix = matrix_p[0]
    ax.imshow(np.roll(matrix, (fn, fn), axis=(0, 1)))


fig, ax = plt.subplots()

m = [np.zeros((200, 200, 3), dtype=np.float32)]
FuncAnimation(fig,
              partial(plot_fib, ax=ax, matrix_p=m),
              fib(12),
              repeat=False)

fig.show() # Option 1
plt.show(block=True) # Option 2





fig, ax = plt.subplots()

FuncAnimation(fig,
              partial(plot_rotation, ax=ax, matrix_p=m),
              fib(24),
              repeat=False)

fig.show()
