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
from sys import platform
import os

difficulty = "hard"
url = "https://www.nytimes.com/puzzles/sudoku/" + difficulty

if platform == "linux" or platform == "linux2":
     chrome_path = '/usr/bin/google-chrome %s --incognito'
     webbrowser.get(chrome_path).open(url)
elif platform == "darwin":
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s --incognito'     
    os.system("open -na \"Google Chrome\" --args --incognito \"{}\"".format(url)) 
elif platform == "win32":
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe --incognito %s'
    webbrowser.get(chrome_path).open_new(url)


page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser") 
table = soup.find_all("div", {"class":"pz-game-screen"})[0]
script = table.find_all("script", {"type":"text/javascript"})
text = script[0].get_text().split("=")[1]
Dict = json.loads(text)
grid = np.array( Dict[difficulty]["puzzle_data"]["puzzle"] ).reshape(9,9).tolist()

def direct_enter(grid):
    greedyBacktrack(grid) # solve the puzzle using greedy backtrack
    grid = ConvertToChar(grid) # convert the grid to characters
    time.sleep(1) # wait for the page to load
    printBoard(grid) # print the grid
    EnterBoard(grid) # enter the grid into the website

#time.sleep(1) # wait for 1 second
greedyBacktrack_visualiser(grid) # visualise the backtrack
#direct_enter(grid) # enter the grid into the website


