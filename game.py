import os
import time
import threading
import random
from playsound import playsound # playsound version 1.2.2 is required (pip install -I playsound==1.2.2)

if os.name == "nt":
    def clearScreen():
        os.system("cls")
else:
    def clearScreen():
        os.system("clear")

def play(path):
    def playThread():
        playsound(path)
        time.sleep(1)

    pThread = threading.Thread(target=playThread)
    pThread.start()

def centerStr(orientation="hor"):
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    
    if orientation == "hor":
        return " " * (width//3)
    elif orientation == "ver":
        return "\n" * (height//4)
    else:
        return "{}".center(width).format(orientation)

def init():
    # global speed, grid
    # speed = int(input("Select speed (1-10): "))
    # if speed < 1 or speed > 10:
    #     speed = 1
    # speed = 3 - (speed * 0.2)
    
    clearScreen()

    grid = [[rgb("░░░", 90, 90, 90) for i in range(20)] for i in range(20)]

    grid[2][1] = rgb("███", 50, 255, 50)
    grid[2][2] = rgb("███", 0, 200, 0)
    grid[2][3] = rgb("███", 0, 200, 0)
    grid[2][4] = rgb("███", 0, 200, 0)
    grid[2][5] = rgb("███", 0, 200, 0)

    width = os.get_terminal_size().columns

    print(centerStr("ver") + "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓".center(width))
    for i in grid:
        line = "┃"
        for x in i:
            line = line + x
        line = line + "┃"
        print(line.center(width))
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛".center(width) + centerStr("ver"))

def rgb(text, red, green, blue):
    return (f"\033[38;2;{red};{green};{blue}m{text}\033[38;2;255;255;255m")

# print("HIHIHIXA " + rgb("HERES AN APPLE: ", 255, 0, 50) + "🍎" + " SNAKE: " + rgb("🞖", 50, 255, 50) + rgb("🞖 🞖 🞖 🞖", 0, 200, 0))

while True:
    init()