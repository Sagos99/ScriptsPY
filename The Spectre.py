from time import sleep

local = "/Users/samuel/Sagos/The Spectre.txt"
arquivo = open(local,"w")
arquivo.write("")
arquivo.close()
sleep(15.5)


def escrever(letra,tempo):
    arquivo = open(local,"a")
    arquivo.write(letra)
    arquivo.close()
    sleep(tempo)




for x in range(2):

    if x == 0:
        escrever("Hello ",0.8)
        escrever("hello\n",2)
        escrever("Can you ",1)
        escrever("hear me, ",2)
        escrever("as I scream ",1.3)
        escrever("your name\n\n",1.5)

        escrever("Hello ",0.8)
        escrever("hello\n",0.8)
        escrever("Do you ",0.8)
        escrever("need me, ",1.4)
        escrever("before ",1.1)
        escrever("I fade away\n\n",2)
    else:
        escrever("Hello ",0.8)
        escrever("hello\n",2)
        escrever("Nice to ",1)
        escrever("meet you, ",2)
        escrever("voice inside ",1.3)
        escrever("my head\n\n",1.5)

        escrever("Hello ",0.8)
        escrever("hello\n",0.8)
        escrever("I believe ",0.8)
        escrever("you, ",1.4)
        escrever("how can ",1.1)
        escrever("I forget\n\n",2)

    escrever("Is this ",0.9)
    escrever("a place that I ",1)
    escrever("call home\n",2.3)
    escrever("To find ",0.7)
    escrever("what I've ",1)
    escrever("become\n",1.5)
    escrever("Walk along ",0.8)
    escrever("the path ",1)
    escrever("unknown\n\n",2.8)

    escrever("We Live\n",1)
    escrever("We Love\n",1)
    escrever("We Lie\n\n",1.4)

    escrever("Deep in ",0.5)
    escrever("the dark ",0.7)
    escrever("I don't need ",0.9)
    escrever("the light\n",1.5)
    escrever("There's a ",0.8)
    escrever("ghost ",1)
    escrever("inside me\n",1.8)
    escrever("It all ",0.8)
    escrever("belongs to ",1)
    escrever("the other ",0.8)
    escrever("side\n\n",1.7)

    escrever("We Live\n",1)
    escrever("We Love\n",1)
    escrever("We Lie\n\n",5.8)

    escrever("We Live\n",1)
    escrever("We Love\n",1)

    if x == 0:
        escrever("We Lie\n\n",22.5)
    else:
        escrever("We Lie",0.1)