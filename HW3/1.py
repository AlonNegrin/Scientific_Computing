import numpy as np


# return the norm l(p) of v
def normip(v, p):
    return (sum(abs(i ** p) for i in v)) ** (1 / p)


# A = MxN matrix | M <= N
# returns A and the QR decomposition of A.
def QRDecomposition(A):
    eps = 1e-14
    m, n = A.shape
    R = np.zeros((n, n))
    Q = np.zeros((m, n))
    for j in range(n):
        v = A[:, j]
        for i in range(j - 1):
            R[i, j] = np.transpose(Q[:, i]) @ v
            v = v - R[i, j] * Q[:, i]
        if np.all(np.abs(v) <= eps):
            A = np.delete(A, j, 1)
            n -= 1
        else:
            R[j, j] = normip(v, 2)
            Q[:, j] = v / R[j, j]
    return A, Q, R


A = np.array([[1, 1, 3],
              [2, 1, 4],
              [3, -1, 1],
              [2, 1, 4],
              [1, 0, 1]])
A, Q, R = QRDecomposition(A)
print(Q @ R)
