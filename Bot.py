##########################################
########### Bot campo minado #############
############# Samuel Ramos ###############
######## Criado dia: 05/11/2018 ##########
##########################################



import pyautogui

msg = None

while msg != "!sair":
    msg = input("Digite uma mensagem: ")
    
    if msg == "!sair":
        break
    
    pyautogui.click(1501, 972)
    pyautogui.typewrite(msg+'\n', interval=0.1)
    pyautogui.click(342, 775)