import numpy as np

A = np.array([[1, 1, 0], [1, -2, 1], [2, 1, 2]])
y = np.array([2, -1, 3])
x = np.array([[1], [2], [-2]])
B = np.array([[1, -1, 1], [-1, 0, 1], [3, 2, 1]])
C = np.array([[1, -1j], [-1, 1j], [0, 2j]], dtype=complex)

print("Ax :")
print(A @ x)
print("\n")

print("BxC cannot be multiplied")
print("\n")
# print(B@x@C)  //this one cannot be multiplied.

print("yAB :")
print(y @ A @ B)
print("\n")

print("CCtx :")
print(C @ C.transpose() @ x)
print("\n")

print("yx :")
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
