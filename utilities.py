#This python program is used to check whether a cell within 
#the sudoku board is safe to fill with a certain number.
#The program returns True if the cell is safe to fill with
#the number, and False if the cell is not safe to fill with
#the number.

import pyautogui as pg
pg.PAUSE = 0

def isSafe(board, row, col, num):
    # Check if 'num' is not already present in row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if 'num' is not already present in column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if 'num' is not already present in box
    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True

def printBoard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if(j == 2 or j == 5):
                print("|", end=" ")
        if(i == 2 or i == 5):
            print("\n- - - - - - - - - - -")
        else:
            print("\n")

def getInput():
    board = []
    #get the input from the user for a 9*9 integer matrix
    for i in range(9): 
        board.append(list(map(int, input().split()))) #get the input for each row and append it to the board
    return board

def assign(board, row, col, num):
    board[row][col] = num
    #go to cell
    if(row>0):
        pg.press('down', presses = row)
    if(col>0):
        pg.press('right', presses = col)
    if(num == 0):
        pg.press('backspace')
    else:
        pg.press(str(num))
    #go back to top left
    if(col>0):
        pg.press('left', presses = col)
    if(row>0):
        pg.press('up', presses = row)

    
def EnterBoard(board): #enter the board into the sudoku website
    for i in range(9):
        for j in range(9):
            pg.press(board[i][j])
            if(j != 8):
                pg.press('right')
            if(j == 8 and i != 8):
                pg.press('down')
                pg.press('left', presses = 8)
            if(j == 8 and i == 8):
                pg.press('enter')

def ConvertToChar(board): #convert the board to characters for pyautogui to enter
    grid_char = []
    for i in range(9):
        grid_char.append([])
        for j in range(9):
            grid_char[i].append(str(board[i][j]))
    return grid_char