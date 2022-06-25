## Introduction:
-	The game of Sudoku exploded in popularity worldwide in 2005. Almost every major newspaper
    now publishes a Sudoku puzzle daily. Handheld game players let you play anytime, anywhere and
    create puzzles on demand at various levels of difficulty.
- A completed Sudoku puzzle is a 9×9 grid (i.e., a two-dimensional array) in which the digits 1
  through 9 appear once and only once in each row, each column and each of nine 3×3 grids.
    
    ![image](https://user-images.githubusercontent.com/94821815/175758912-e0fb135b-ffe2-480b-939e-b0aa2b47936e.png)

-	The objective is to fill a nine-by-nine (9x9) grid with digits so that each row, column and 3x3 section contain number between 1 and 9, with each number used once and only once in each section. The Sudoku game players are provided with partially filled grid meant to be solved.

-	Solving Sudoku is not something requiring any complex mathematical knowledge but rather needs sound logical and reasoning ability.

## About:

This Script is a Sudoku Solver that is designed to get values form the daily sudoku from NewYorkTimes(https://www.nytimes.com/puzzles/sudoku/easy) and solve it using different algorithms such as Backtrack, greedyBacktrack, reverseBackTrack and zigzagBacktrack. The solved sudoku is then entered into the same site.

## Working:

-	Every time this Script is executed, it scrapes values from NYTimes sudoku page.
-	Then it uses one of the various algorithms discussed above to solve the problem.
-	The we automate the script to enter values into the sudoku given in the website.
- The algorithm also shows gives a visual of how the algorithm computes the value.

## Requirements:
In order to run the Script, the require **Python & PyGame** and you can install the requirements using:
```
pip install -r requirements.txt
```

## Execution:
-	Clone this repository using
```
git clone https://github.com/Ishaan1742/Sudoku_Solver.git
```
**OR**
Zip Download the Repository and Extract it's contents.
-	Now run the [webscrap_sudoku_NY](https://github.com/Ishaan1742/Sudoku_Solver/blob/master/webscrap_sudoku_NY.py) file directly in your Terminal using
```                         
python webscrap_sudoku_NY
```
**OR**
```
python3 webscrap_sudoku_NY
```
