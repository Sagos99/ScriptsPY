import pyautogui

if pyautogui.locateOnScreen('/Users/samuel/Sagos/Scripts/rosa.jpg', grayscale=True):
    x,y = pyautogui.locateCenterOnScreen('/Users/samuel/Sagos/Scripts/rosa.jpg', grayscale=True)
    pyautogui.moveTo(x, y, 1)
else:
    print("Cor rosa não encontrado")