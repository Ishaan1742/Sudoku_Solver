from Backtrack import *
from greedyBacktrack import *
from zigzagBacktrack import *
from reverseBacktrack import *
from utilities import *
import time

grid = getInput()
greedyBacktrack(grid) #call the greedy backtrack function, grid is now a solved grid.

#convert grid to chararcter array for sending to sudoku.com or any website as pyautogui works with characters
grid = ConvertToChar(grid)

time.sleep(5) #click on the grid (manually)

#Display solution
printBoard(grid)

#Enter the numbers into the grid on www.sudoku.com or any website.
EnterBoard(grid)



