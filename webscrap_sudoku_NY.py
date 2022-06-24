from turtle import back
import webbrowser
import requests
from bs4 import BeautifulSoup
import json
import numpy as np
from Backtrack import backtrack, backtrack_visualiser
from greedyBacktrack import greedyBacktrack, greedyBacktrack_visualiser
from zigzagBacktrack import zigzagBacktrack, zigzagBacktrack_visualiser
from reverseBacktrack import reverseBacktrack, reverseBacktrack_visualiser
from utilities import ConvertToChar, EnterBoard, printBoard
import time

difficulty = "hard"

url = "https://www.nytimes.com/puzzles/sudoku/" + difficulty

page = requests.get(url)
#open page in webbrowser
webbrowser.open(url)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find_all("div", {"class":"pz-game-screen"})[0]
script = table.find_all("script", {"type":"text/javascript"})
text = script[0].get_text().split("=")[1]
Dict = json.loads(text)
grid = np.array( Dict[difficulty]["puzzle_data"]["puzzle"] ).reshape(9,9).tolist()

def direct_enter(grid):
    greedyBacktrack(grid) # solve the puzzle using greedy backtrack
    grid = ConvertToChar(grid) # convert the grid to characters
    printBoard(grid) # print the grid
    time.sleep(0.5) # wait for 0.5 seconds
    EnterBoard(grid) # enter the grid into the website

time.sleep(0.5) # wait for 0.5 second
reverseBacktrack_visualiser(grid) # visualise the backtrack
#direct_enter(grid) # enter the grid into the website


