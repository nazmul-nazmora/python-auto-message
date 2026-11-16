"""Auto Message"""

import pyautogui 
import time

count = 7
while count > 0:
    time.sleep(2)
    pyautogui.write("What are you doing? ")
    time.sleep(1)
    pyautogui.press("enter")
    count -= 1
