from utilities import isSafe, printBoard, assign

# Spiral Backtracking is another modified version of the Backtracking algorithm.
# Instead of picking the next cell top to bottom and left to right, it 
# picks the next cell in an inward spiral.
# The Algorithm tends to do well when the majority entries near 4 edges 
# are prefilled. Interestingly, this Algorithm is significantly slower 
# than normal Backtracking Algorithm in most cases. 
# The reason for this might lie in the nature of Sudoku, which makes choosing 
# next cells spirally a poor choice.

def spiralBacktrack(board):
    row = 0
    col = 0
    while row < 9 and col<9:
        if board[row][col] == 0:
            for num in range(1, 10):
                if isSafe(board, row, col, num):
                    board[row][col] = num # fill the cell with the number
                    if spiralBacktrack(board):
                        return True # board is filled
                    board[row][col] = 0 # backtrack
            return False # board is not filled
        if(row%2 == 0):
            if(col < 8):
                col += 1
            else:
                row += 1
        else:
            if(col>0):
                col -= 1
            else:
                row += 1

    return True # board is filled

def spiralBacktrack_visualiser(board):
    row = 0
    col = 0
    while row < 9 and col<9:
        if board[row][col] == 0:
            for num in range(1, 10):
                if isSafe(board, row, col, num):
                    assign(board, row, col, num) # fill the cell with the number
                    if spiralBacktrack_visualiser(board):
                        return True # board is filled
                    assign(board, row, col, 0) # backtrack
            return False # board is not filled
        if(row%2 == 0):
            if(col < 8):
                col += 1
            else:
                row += 1
        else:
            if(col>0):
                col -= 1
            else:
                row += 1

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
    if spiralBacktrack(board):
        print("Sudoku solved")
        printBoard(board)
    else:
        print("No solution")
