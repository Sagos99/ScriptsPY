import pyautogui
from time import sleep


local = "/Users/samuel/Sagos/Scripts/texto.txt"

msg = None

while msg != "!sair":
    arquivo = open(local, "r") 
    msg = arquivo.read()
    arquivo.close()
    
    if msg != "":
        if msg != "!sair":
            pyautogui.click(1501, 972)
            pyautogui.typewrite(msg+'\n', interval=0.1)

        arquivo = open(local, "w") 
        arquivo.write("")
        arquivo.close()

    if msg == "!sair":
        break

    sleep(5)