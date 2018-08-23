from pyautogui import *
import time
xMax, yMax = size()
while True:
    time.sleep(0.01)
    x, y = position()
    if(x == 0 or y == 0 or x == (xMax - 1) or y == (yMax - 1)):
        print("you hit the edge of screen.And the position is",x,y)
        