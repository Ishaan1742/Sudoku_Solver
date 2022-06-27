from utilities import isSafe, printBoard, assign

# Reverse Backtrack algorithm is same as the backtrack algorithm but
# differs in the fact that it follows a bottom-top and right-left approach.
# It starts with the bottom right cell and tries to fill it with a number.
# If it is safe to fill it with a number, it fills it and recursively calls
# the function again to fill the next cell. If the board is filled, the
# function returns True. If the board is not filled, the function returns
# False. This may fare better in comparison to normal backtrack algorithm, in
# cases when the bottom/right halves of the Sudoku are comparitively denser 
# than the top/left halves.

def reverseBacktrack(board):
    for row in range(8, -1, -1):
        for col in range(8, -1, -1):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if isSafe(board, row, col, num):
                        board[row][col] = num # fill the cell with the number
                        if reverseBacktrack(board):
                            return True # board is filled
                        board[row][col] = 0 # backtrack
                return False # board is not filled
    return True # board is filled

def reverseBacktrack_visualiser(board, curr_row = 0, curr_col = 0):
    for row in range(8, -1, -1):
        for col in range(8, -1, -1):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if isSafe(board, row, col, num):
                        curr_row, curr_col = assign(board, row, col, num, curr_row, curr_col) # fill the cell with the number
                        return_value, curr_row, curr_col = reverseBacktrack_visualiser(board, curr_row, curr_col)
                        if return_value:
                            return True, curr_row, curr_col # board is filled
                        curr_row, curr_col = assign(board, row, col, 0, curr_row, curr_col) # backtrack
                return False, curr_row, curr_col # board is not filled
    return True, curr_row, curr_col # board is filled

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
    if(reverseBacktrack(board)):
        print("Sudoku solved")
        printBoard(board)
    else:
        print("No solution")
        
