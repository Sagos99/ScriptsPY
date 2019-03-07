import pyautogui
from time import sleep

sleep(15.8)


def escrever(letra,tempo,enter,espera):
    pyautogui.typewrite(letra, interval=tempo)

    if enter == True:
        pyautogui.press('esc')
        pyautogui.press('enter')

    sleep(espera)



for x in range(2):

    if x == 0:
        escrever("Hello",0.04,False,0)
        escrever(" hello",0.05,True,0.8)
        escrever("Can you",0.09,False,0.3)
        escrever(" hear me",0.09,False,1)
        escrever(", as I scream your name",0.07,True,0)
        escrever("",0,True,0)

        escrever("Hello",0.04,False,0)
        escrever(" hello",0.05,True,0.8)
        escrever("Do you",0.07,False,0)
        escrever(" need",0.09,False,0.5)
        escrever(" me",0.13,False,0.1)
        escrever(", before",0.04,False,0.3)
        escrever(" I fade away",0.05,True,0)
        escrever("",0,True,0.3)
    else:
        escrever("Hello",0.04,False,0)
        escrever(" hello",0.05,True,0.8)
        escrever("Nice to",0.09,False,0.3)
        escrever(" meet you",0.09,False,1)
        escrever(", voice inside",0.05,False,0)
        escrever(" my head",0.05,True,0)
        escrever("",0,True,0.3 )

        escrever("Hello",0.05,False,0)
        escrever(" hello",0.08,True,0)
        escrever("I believe",0.08,False,0)
        escrever(" you",0.05,False,0)
        escrever(", how can",0.05,False,0)
        escrever(" I forget",0.05,True,0)
        escrever("",0,True,2)

    escrever("Is this",0.02,False,0.2)
    escrever(" a place that I",0.03,False,0)
    escrever(" call home",0.13,True,0.7)
    escrever("To find",0.05,False,0.3)
    escrever(" what I've",0.05,False,0.2)
    escrever(" become",0.05,True,0.3)
    escrever("Walk along",0.05,False,0)
    escrever(" the path",0.05,False,0.3)
    escrever(" unknown",0.1,True,0)
    escrever("",0,True,1.3)

    escrever("We Live",0.015,True,0.22)
    escrever("We Love",0.015,True,0.22)
    escrever("We Lie",0.015,True,0.22)
    escrever("",0,True,0.4)

    escrever("Deep in",0.05,False,0)
    escrever(" the dark",0.05,False,0)
    escrever(" I don't need",0.05,False,0)
    escrever(" the light",0.05,True,0)
    escrever("There's a",0.05,False,0)
    escrever(" ghost",0.05,False,0.1)
    escrever(" inside me",0.1,True,0.9)
    escrever("It all",0.05,False,0)
    escrever(" belongs to",0.05,False,0)
    escrever(" the other",0.05,False,0)
    escrever(" side",0.14,True,0)
    escrever("",0,True,0.7)

    escrever("We Live",0.015,True,0.22)
    escrever("We Love",0.015,True,0.22)
    escrever("We Lie",0.015,True,0.22)
    escrever("",0,True,4.1)

    escrever("We Live",0.015,True,0.22)
    escrever("We Love",0.015,True,0.22)

    if x == 0:
        escrever("We Lie",0.015,True,0)
        escrever("",0,True,22.5)
    else:
        escrever("We Lie",0.015,False,0)