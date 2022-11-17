import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


# ---------- 2 ---------- #
def cosArray(low_bound, high_bound, freq):
    t = np.arange(low_bound, high_bound, 1 / 10000)
    return np.cos(2 * np.pi * freq * t)


def cosPlay():
    for i in range(500, 20000, 500):
        sd.play(cosArray(0, 1, i), 10000, blocking=True)
        plt.plot(cosArray(0, 1, i))
        plt.show()


def cosPlayB():
    freq = 440
    while freq < 20000:
        print(freq)
        sd.play(cosArray(0, 1, freq), 10000, blocking=True)
        plt.plot(cosArray(0, 1, freq))
        plt.show()
        freq = freq * 2 ** (1 / 12)
