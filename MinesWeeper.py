##########################################
########### Bot campo minado #############
########### By: Samuel Ramos #############
##########################################


import pyautogui
from time import sleep
from random import randint
# from playsound import playsound


sleep(2)

# img = pyautogui.screenshot(region=(151, 99, 1059, 566)) # Captura o campo minado

pyautogui.click(randint(151,1059),randint(99,566)) # Pega um valor aleatório para fazer o first_click
pyautogui.moveTo(1,1)


numbers_one = list(pyautogui.locateAllOnScreen(r'img\01.png'))
print('Encontrou %s números' % str(len(numbers_one)))


img = pyautogui.screenshot(region=(151, 99, 1059, 566)) # Captura o campo minado
img.save(r'img\tela.png')