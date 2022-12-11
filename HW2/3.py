import random

import numpy as np
import matplotlib.pyplot as plt


def normip(v, p):
    return (sum(abs(i ** p) for i in v)) ** (1 / p)


# ---------- 3 ---------- #

# ----------- a ---------- #
X = np.zeros([8, 8])
X[1, 1:3] = 1
X[1, 5:7] = 1
X[3, 3:5] = 1
X[5:7, 1::5] = 1
X[6, 2:6] = 1
plt.imshow(X, cmap='gray')
plt.show()

for i in range(8):
    for j in range(8):
        X[i, j] = 1 if X[i, j] == 0 else 0

plt.imshow(X, cmap='gray')
plt.show()

Y = X.copy()
Y[1, 5:7] = 1


# ----------- b ---------- #
def FrobeniusInnerProduct(A, B):
    result = sum((A.flatten() * B.flatten()))
    normA = normip(A.flatten(), 2)
    normB = normip(B.flatten(), 2)
    return result / (normA * normB)


print(FrobeniusInnerProduct(X, Y))

# ----------- c ---------- #

for i in range(8):
    for j in range(8):
        X[i, j] = 1 if X[i, j] == 0 else 0

fip = 0
Xtest = np.zeros([8, 8])
count = 0

while fip <= 0.7:
    plt.subplot(1, 2, 1)
    Xtest[1:7, 1:7] = np.random.randint(0, 2, (6, 6))
    count += 1
    fip = FrobeniusInnerProduct(Xtest, X)

    if fip < 0.7:
        plt.suptitle("access denied - " + str(format(fip, ".2f")))
        print("access denied")
    else:
        print("access permitted after", count, "options , with " + str(format(fip, ".2f")) + "% similarity")
        plt.suptitle("access permitted - " + str(format(fip, ".2f")))

    plt.title("template face")
    plt.imshow(X, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.title("test face")
    plt.imshow(Xtest, cmap='gray')
    plt.show()
