from utilities import isSafe, printBoard, assign

# Greedy Backtrack follows a greedy strategy wherein it starts filling numbers 
# in the board from the cell which has the least number of possible options.
# It does this by first finding the cell with the least number of possibilities.
# Fills the cell and then recursively calls the function again to fill the next
# cell. If the board is filled, the function returns True.
# If the board is not filled, the function returns False.
# The function is recursive and calls itself until the board is filled.

def greedyBacktrack(board):
    #greedy approach by trying to find the empty cell with minimum possibilities.
    min = 9
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                count = 0
                for val in range(1,10):
                    if(isSafe(board, i, j, val)):
                        count = count + 1 #count the number of possibilities for the cell
                if(count < min): #if the number of possibilities is less than the current minimum, update the minimum
                    min = count
                    row = i
                    col = j
    if(min == 9):
        return True #board is filled
    for val in range(1,10):
        if(isSafe(board, row, col, val)):
            board[row][col] = val #fill the cell with the number
            if(greedyBacktrack(board)):
                return True #board is filled
            board[row][col] = 0 #backtrack
    return False #board is not filled

def greedyBacktrack_visualiser(board):
    #greedy approach by trying to find the empty cell with minimum possibilities.
    min = 9
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                count = 0
                for val in range(1,10):
                    if(isSafe(board, i, j, val)):
                        count = count + 1 #count the number of possibilities for the cell
                if(count < min): #if the number of possibilities is less than the current minimum, update the minimum
                    min = count
                    row = i
                    col = j
    if(min == 9):
        return True #board is filled
    for val in range(1,10):
        if(isSafe(board, row, col, val)):
            assign(board, row, col, val) #fill the cell with the number
            if(greedyBacktrack_visualiser(board)):
                return True #board is filled
            assign(board, row, col, 0) #backtrack
    return False #board is not filled

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
            
    if(greedyBacktrack(board)):
        print("Sudoku solved")
        printBoard(board)   #print the board
    else:
        print("No solution")