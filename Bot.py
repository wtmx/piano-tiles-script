# Install these libraries from an administrator terminal (windows):

# pip install pywin32
# pip install keyboard
# pip install pyautogui
# pip install opencv-python

# Here are the libraries to paste at the start of the scripts:

from pyautogui import *
# import pyscreeze
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Tile 1 Position: X: 674 Y: 839
# Tile 2 Position: X: 805 Y: 839
# Tile 3 Position: X: 909 Y: 839
# Tile 4 Position: X: 1042 Y: 839

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) # pause script for 0.01s
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


# press q to stop the script
while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(674, 839)[0] == 0: # check R value of pixel
        click(674, 839)
    if pyautogui.pixel(805, 839)[0] == 0:
        click(805, 839)
    if pyautogui.pixel(909, 839)[0] == 0:
        click(909, 839)
    if pyautogui.pixel(1042, 839)[0] == 0:
        click(1042, 839)
