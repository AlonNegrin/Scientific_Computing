import numpy as np
from matplotlib import pyplot as plt

A = np.array([[1, 1, 0], [1, -2, 1], [2, 1, 2]])
y = np.array([2, -1, 3])
x = np.array([[1], [2], [-2]])
B = np.array([[1, -1, 1], [-1, 0, 1], [3, 2, 1]])
C = np.array([[1, -1j], [-1, 1j], [0, 2j]], dtype=complex)

# ------------------------------------------ 1 -------------------------------------- #

print(A @ x)
print("\n")

# print(B@x@C)  //this one cannot be multiplied.

print(y @ A @ B)
print("\n")

print(C @ C.transpose() @ x)
print("\n")

print(y @ x)
print("\n")

print("first option :", np.sum(A @ B))  # first option.

# second option.
AB = np.ones([3, 3], dtype="int")
result = 0
for i in range(3):
    for j in range(3):
        AB[i][j] = sum((A[i][k] * B[k][j] for k in range(3)))
        result += AB[i][j]
print("second option :", result)
print("\n")

# ------------------------------------------ 2 -------------------------------------- #

w = np.array([2, 3, -3j, -1, 3], dtype=complex)
v = np.array([1j, -1j, 2, 1, 5], dtype=complex)
u = np.array([2j, 3, 5, -2, 5], dtype=complex)


def innerProd(v1, v2):
    if np.shape(v1) != np.shape(v2):
        print("Dimension Error")
        return
    else:
        v1 = np.array(v1)
        v2 = np.array(v2).conjugate()

        product = 0
        for n in range(len(v1)):
            product += v1[n] * v2[n]
    return product


print(innerProd(u, v * 2))
print(innerProd(u, (v + 2 * w)))

# ------------------------------------------ 3 -------------------------------------- #

Ts = 1 / 44100
x = np.arange(0, 1 - Ts, Ts)
y1 = np.cos(2 * np.pi * 1 * x)
plt.plot(x, y1)
y2 = np.sin(2 * np.pi * 1 * x)
plt.plot(x, y1, 'b', x, y2, 'r')
plt.show()

fs = 44100
Ts = 1 / fs
x = np.arange(0, 1 - Ts, Ts)
u = np.cos(2 * np.pi * x)
v = np.sin(2 * np.pi * x)
print("option 1 : ", innerProd(u, v))
print("option 2 : ", sum(u * v))
