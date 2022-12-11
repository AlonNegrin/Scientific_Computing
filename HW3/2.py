import os

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time


def innerProduct(x1, x2, normal=0):
    ip = sum(x1 * x2)
    if normal == 1:
        n1 = np.sqrt(sum(x1 * x1))
        n2 = np.sqrt(sum(x2 * x2))
        ip = ip / (n1 * n2)
    return ip


def Chirp(dur, f0, u, fs):
    Ts = 1 / fs
    tt = np.linspace(0, dur, int(dur / Ts))
    sig = lambda t: np.cos(2 * np.pi * f0 * t + 2 * np.pi * u * (t ** 2))
    return sig(tt), tt


def plot(tt, sig):
    t_start = tt[0:200]
    t_end = tt[len(tt) - 200:]
    plt.subplot(2, 1, 1)
    plt.plot(t_start, sig[0:200])
    plt.subplot(2, 1, 2)
    plt.plot(t_end, sig[len(tt) - 200:])
    plt.show()


def getChirp(xnoise, chrip, fs):
    p = np.zeros(int(len(xnoise) - len(chrip)))
    for i in range(0, len(xnoise) - len(chrip), 100):
        p[i] = innerProduct(chrip, xnoise[i:i + len(chrip)], normal=1)

    index = np.argmax(p)
    sec = index / fs
    return index, sec


if __name__ == '__main__':
    # A
    fs = 44100
    tt, sig = Chirp(0.7, 1000, 550, fs)

    # B
    sd.play(sig)
    time.sleep(1)
    sd.play(tt)
    plot(sig, tt)

    # C
    xnoise = np.random.randn(15 * fs)
    xnoise[9 * fs: (int(9.7 * fs))] += sig

    # D
    i, second = getChirp(xnoise, sig, fs)
    print("the first signal is in sample number: ", i, " in second: ", second)

    # E
    xnsig = np.load('xnsig.npy')
    chirp = np.load('chirp.npy')

    i, second = getChirp(xnsig, chirp, fs)
    print("the second signal is in sample number: ", i, " in second: ", second)
