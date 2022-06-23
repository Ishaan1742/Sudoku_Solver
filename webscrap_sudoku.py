# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 19:06:35 2022

@author: Krithikavvgreat
"""

import webbrowser
import requests
from bs4 import BeautifulSoup
from greedyBacktrack import greedyBacktrack
from utilities import EnterBoard, printBoard, ConvertToChar
import time

url = "https://nine.websudoku.com/?"
#launch url in browser
webbrowser.open(url)
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
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
        