import numpy as np
import matplotlib.pyplot as plt


# updating the cells according to the rules
def update_Board(board):
    # init an empty matrix to store each corresponding cell number of neighbours.
    neighbours = np.zeros(board.shape)
    # Count the number of living cells around each cell
    neighbours += np.roll(board, 1, 0)
    neighbours += np.roll(board, -1, 0)
    neighbours += np.roll(board, 1, 1)
    neighbours += np.roll(board, -1, 1)
    neighbours += np.roll(np.roll(board, 1, 0), 1, 1)
    neighbours += np.roll(np.roll(board, -1, 0), -1, 1)
    neighbours += np.roll(np.roll(board, 1, 0), -1, 1)
    neighbours += np.roll(np.roll(board, -1, 0), 1, 1)

    board = (neighbours == 3) | (board & (neighbours == 2))
    return board

# displays the board at a giving moment
def display_board(board):
    plt.imshow(board, cmap='gray')
    plt.show()

# N - grid size
# p - probability of a cell to be initiated
def play(N, p):
    board = np.random.choice([0, 1], size=(N, N), p=[1 - p, p])
    display_board(board)
    while board.any():
        board = update_Board(board)
        display_board(board)


play(256, 0.15)
