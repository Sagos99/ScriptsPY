from time import sleep
from random import uniform as rfloat

reCorreta = [0, 1, 1, 1]
taxaAprendizagem = 0.01


def stepFunction(soma):
    if (soma >= 1):
        return 1
    else:
        return 0

def calculaSaida(e1,e2,r):
    global pesos
    global taxaAprendizagem
    global totalErros
    global resposta
    global tentativas
    global reCorreta

    s = 0
    totalErros = 0
    resposta = []
    tentativas += 1

    for x in range(len(reCorreta)):
        s = (e1[x]*pesos[0]) + (e2[x]*pesos[1])

        if stepFunction(s) != r[x]:
            totalErros += 1
            pesos[0] += taxaAprendizagem*e1[x]*(abs(r[x]-stepFunction(s)))
            pesos[1] += taxaAprendizagem*e1[x]*(abs(r[x]-stepFunction(s)))

            if pesos[0] >= 1:
                pesos[0] = rfloat(0.005,2)
            if pesos[1] >= 1:
                pesos[1] = rfloat(0.005,2)
        
        resposta.append(stepFunction(s))


x1 = [0,0,1,1]
x2 = [0,1,0,1]
resposta = []
totalErros = 1
pesos = [0.01, 0.3]
tentativas = 0


while totalErros != 0:
    calculaSaida(x1,x2,reCorreta)
    print("\n"*120)
    print("Resposta correta: %s\n" % (reCorreta))
    print("Peso atual w1: "+str(pesos[0])[0:4])
    print("Peso atual w2: "+str(pesos[1])[0:4]+"\n")
    print("Resultado: %s" % (resposta))
    print("Tentativas: %s" % (tentativas))
    print("Total de erros: "+str(totalErros)+"\n")
    sleep(0.08)
else:
    print("Rede neural completa em %s tentativas\nResultado: %s" % (tentativas,resposta))