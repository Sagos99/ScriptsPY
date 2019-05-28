from time import sleep
import pyautogui

sleep(5)
num = 0

while True:
    sleep(0.05)
    pyautogui.write(str(num)+'\n')
    num += 1