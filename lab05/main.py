from typing import Iterable

import numpy as np
import sounddevice as sd
import time


def sinArray(x, fs, freq):
    t = np.arange(0, x, 1 / fs)
    return np.sin(2 * np.pi * freq * t)


def create_tone(x, fs, s: Iterable[int]):
    return sum(map(lambda freq: sinArray(x, fs, freq), s))


def get_freq(n):
    width = (1209, 1336, 1477, 1633)
    height = (697, 770, 852, 941)
    return [width[n % 4], height[n // 4]]


def get_dial(n, fs, x):
    freqs = get_freq(n)
    return create_tone(x, fs, freqs)


def get_number(number):
    index = {'0': 13, '1': 0, '2': 1, '3': 2, '4': 4, '5': 5, '6': 6, '7': 8, '8': 9, '9': 10}
    for i in number:
        key = index[i]
        print(key)
        sd.play(get_dial(key, 44100, 0.2))
        time.sleep(0.2)


def gramMat(mat):
    A = np.zeros(np.shape(mat), dtype=np.float64)
    for i in range(len(mat)):
        v = mat[:, i].reshape((-1, 1))
        for j in range(i):
            u = A[:, j].reshape((-1, 1))
            v = v - ((np.transpose(u) @ v) / (np.transpose(u) @ u)) * u
        A[:, i] = v[:, 0]
    return A / np.linalg.norm(A, axis=0)


if __name__ == '__main__':
    matA = np.array([[1, 2, 3],
                     [-1, 0, 3],
                     [0, -2, 3]])
    print(gramMat(matA))
