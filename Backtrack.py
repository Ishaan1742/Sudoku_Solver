from utilities import isSafe, printBoard

# Backtrack algorithm is a recursive algorithm that tries to fill the board
# with numbers in a way that satisfies the constraints. It does this by following 
# a top - bottom, left - right approach. It starts with the top left cell and tries to
# fill it with a number. If it is safe to fill it with a number, it fills it and
# recursively calls the function again to fill the next cell. If the board is
# filled, the function returns True. If the board is not filled, the function
# returns False.

def backtrack(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if isSafe(board, row, col, num):
                        board[row][col] = num # fill the cell with the number
                        if backtrack(board):
                            return True # board is filled
                        board[row][col] = 0 # backtrack
                return False # board is not filled
    return True # board is filled

if '__main__' == __name__:
    board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 0, 7, 8, 9, 1, 0, 3],
            [7, 8, 9, 1, 2, 3, 4, 0, 6],
            [2, 3, 0, 0, 6, 7, 8, 0, 1],
            [5, 6, 7, 8, 9, 1, 2, 0, 4],
            [8, 9, 0, 2, 3, 4, 5, 0, 7],
            [3, 0, 5, 6, 7, 8, 0, 1, 2],
            [6, 7, 0, 9, 1, 2, 3, 0, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
    if backtrack(board):
        print("Sudoku solved")
        printBoard(board)
    else:
        print("No solution")