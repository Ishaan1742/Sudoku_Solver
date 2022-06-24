# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 08:53:03 2022

@author: Krithikavvgreat
"""

from multiprocessing.connection import wait
import webbrowser
import requests
from bs4 import BeautifulSoup
import json
import numpy as np
from Backtrack import backtrack
from greedyBacktrack import greedyBacktrack
from utilities import ConvertToChar, EnterBoard, printBoard
import time

difficulty = "medium"

url = "https://www.nytimes.com/puzzles/sudoku/" + difficulty

page = requests.get(url)
#open page in webbrowser and wait for it to load
webbrowser.open(url)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find_all("div", {"class":"pz-game-screen"})[0]
script = table.find_all("script", {"type":"text/javascript"})
text = script[0].get_text().split("=")[1]
Dict = json.loads(text)
grid = np.array( Dict[difficulty]["puzzle_data"]["puzzle"] ).reshape(9,9).tolist()

backtrack(grid) # solve the puzzle using greedy backtrack
grid = ConvertToChar(grid) # convert the grid to characters
printBoard(grid) # print the grid
time.sleep(2)
EnterBoard(grid) # enter the grid into the website
