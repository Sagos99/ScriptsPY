def stepFunction(soma):
    if (soma >= 1):
        return 1
    else:
        return 0


peso = 0

x1 = [0,0,1,1]
x2 = [0,1,0,1]

respostas = [0, 0, 0, 1]


def calculando(peso):
    global x1
    global x2
    global respostas

    tentativas = 0
    acertos = 0

    for x in range(4):
        soma = (x1[x]*peso) + (x2[x]*peso)
        tentativas += 1

        if stepFunction(soma) == respostas[x]:
            acertos += 1

    precisao = (acertos/tentativas)*100

    return precisao


for quantidade in range(15):
    if calculando(peso) == 100.0:
        print("%s tem um peso de 100 porcento" % (str(peso)[0:3]))
    #else:
        #print("%s tem um peso de %s porcento" % (str(peso)[0:3],str(calculando(peso))))
    peso += 0.1