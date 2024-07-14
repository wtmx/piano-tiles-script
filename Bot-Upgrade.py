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

# Tile 1 Position: X:  717 Y:  802 RGB: ( 32,  20,  36)
# Tile 2 Position: X:  816 Y:  822 RGB: ( 30,  19,  36)
# Tile 3 Position: X:  920 Y:  799 RGB: ( 27,  20,  36)
# Tile 4 Position: X: 1021 Y:  824 RGB: ( 23,  20,  36)

# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#     time.sleep(0.01) # pause script for 0.01s
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# press q to stop the script

# Attempt to implement alternate way to play Piano Tiles variation

while keyboard.is_pressed('q') == False:
    try:
        image_location = pyautogui.locateOnScreen('piano3-tile.png', region=(675,680,397,180), confidence=0.8)
        print(f"Image found at: {image_location}")
        time.sleep(0.1)

    except pyautogui.ImageNotFoundException:
        print("Image not found on screen.")
        time.sleep(0.1)
    
    

    # pic = pyautogui.screenshot(region=(675,680,397,180)) # x-pos, y-pos, width, height
    # width, height = pic.size

    # for x in range(0,width,50):
    #     for y in range(0,height,50):

    #         r,g,b = pic.getpixel((x,y))
    #         if b == 36:
    #             click(x + 675, y + 0)
    #             time.sleep(0.05)
    #             break

