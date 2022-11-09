import numpy as np

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


print("u * 2v = ")
print(innerProd(u, v * 2))
print()
print("u * (2v*w) = ")
print(innerProd(u, (v + 2 * w)))
