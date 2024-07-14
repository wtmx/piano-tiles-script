import pyautogui
import time

time.sleep(0.5)
iml = pyautogui.screenshot(region=(675,680,397,180)) # x-pos, y-pos, width, height
# iml = pyautogui.screenshot(region=(675,140,397,720)) # x-pos, y-pos, width, height
iml.save(r"C:\Users\wtmx9\OneDrive\Documents\Coding\Adv-Img-Recognition-Bot\savedimage.png")