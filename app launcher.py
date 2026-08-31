import pyautogui
import time 

app = input("enter app name : ")

pyautogui.press("win")
time.sleep(1)

pyautogui.write(app)
time.sleep(1)

pyautogui.press("enter")
