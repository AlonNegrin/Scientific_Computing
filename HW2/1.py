import numpy as np


# ---------- 1 ---------- #

def normip(v, p):
    return (sum(abs(i ** p) for i in v)) ** (1 / p)


print("question 1: ")

v = np.array([1, 2j, -3, 1, 7], dtype=complex)
print("1a) norm is ", normip(v, 2), "\n")

v = np.array([1, 5, 3j, -1 + 1j, 2], dtype=complex)
v_norm = normip(v, 2)
unit_vector = np.array(v / v_norm)

print("1b) unit vector is ", unit_vector, "\n")

v = np.array([6, 7, 1j, 2j, 7])
u = np.array([2, 1, -2j, -3, 8])
w = u - v
print("1c) distance between u and v is ", normip(w, 2))
