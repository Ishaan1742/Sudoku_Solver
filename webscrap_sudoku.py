from selenium import webdriver
from bs4 import BeautifulSoup
from utilities import printBoard, ConvertToChar, EnterBoard
from greedyBacktrack import greedyBacktrack

url = "https://nine.websudoku.com/?"
PATH = "/Users/ishaan/PycharmProjects/Sudoku_Solver/msedgedriver"
driver = webdriver.Edge(PATH)
driver.get(url)
page_content = driver.page_source
soup = BeautifulSoup(page_content, "html.parser")
table = soup.find_all("table", {"id":"puzzle_grid"})[0]
rows = table.find_all("tr")
grid = []
for row in rows:
    cells = row.find_all("td")
    list_ = []
    for cell in cells:
        try : 
            x = int(cell.input["value"])
        except: 
            x = 0
        list_.append(x)
    grid.append(list_)

greedyBacktrack(grid)
grid = ConvertToChar(grid)
printBoard(grid)
EnterBoard(grid)
        
