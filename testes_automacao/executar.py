import pyautogui
import time

pyautogui.PAUSE = 1
while False:
    currentMouseX, currentMouseY = pyautogui.position() 
    print(currentMouseX, currentMouseY)
    time.sleep(4)
pyautogui.position(0, 1)
# pyautogui.hotkey("win", "r")
# pyautogui.write("gpedit.msc")
# pyautogui.write("notepad")
# pyautogui.hotkey("enter")
# time.sleep(5)
# pyautogui.hotkey("Tab")
# pyautogui.click(785, 242) # seleciona janela
time.sleep(3)
pyautogui.click(415, 461)
# pyautogui.click()