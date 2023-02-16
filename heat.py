import numpy as np
import matplotlib.pyplot as plt

ncols = 1000
nrows = 1000

Amat = np.zeros([nrows, ncols])  # init matrix
tolerance = 10  # iterations
temp1 = 45
temp2 = 0
right, left, down = temp1, temp1, temp1  # all sides 45 degrees
up = temp2  # up side is 0 degrees

# init termostats on sides of the matrix.
Amat[0, :] = up
Amat[-1, :] = down
Amat[:, 0] = left
Amat[:, -1] = right

# show the initiated matrix
plt.imshow(Amat, cmap='hot')
plt.colorbar()
plt.show()

Aold = Amat
diffMat = np.inf
iter = 0
while diffMat > tolerance:
    Up = Amat[:-2, 1:-1]
    Down = Amat[2:, 1:-1]
    Left = Amat[1:-1, :-2]
    Right = Amat[1:-1, 2:]

    Anew = (Up + Down + Left + Right) / 4
    diffMat = np.sum(np.abs(Anew - Aold[1:-1, 1:-1]))
    Aold[1:-1, 1:-1] = Anew
    if iter % 100 == 0:
        plt.imshow(Anew,cmap='hot')
        plt.grid(axis='both')
        plt.colorbar()
        plt.show()
    iter += 1
print("itertations -", iter)
