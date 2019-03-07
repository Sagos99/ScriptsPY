import datetime

qtd_linhas = 0
tarefas = []
news_task = []
linha = -1

local = '/home/samuel/Documentos/Sagos/Tarefas.txt'

hoje = str(datetime.date.today())

ano = hoje[0:4]
mes = hoje[5:7]
dia = hoje[8:10]

hoje = dia+'/'+mes+'/'+ano

print('Lendo arquivo ...')
arquivo = open(local,'r')

for x in arquivo:
    qtd_linhas += 1
    tarefas.append(x) 

arquivo.close()
print('Verificando tasks ...')

for x in reversed(range(qtd_linhas)):
    if tarefas[x][0] == '#' and tarefas[x][38:39] != '#':
        data = tarefas[x][38:48]
        if data == hoje:
            print('As tasks de hoje já foram adicionadas')
            print('Script cancelado.')
            break
        else:
            linha = x
            print('Escrevendo novas tasks ...')
            break

if linha != -1:
    news_task.append('##################################### %s #####################################\n' % (hoje))
    for x in range(linha+1,qtd_linhas-1):
        if tarefas[x][74:82] == 'Pendente':
            news_task.append(tarefas[x])
    news_task.append('######################################################################################')

    arquivo = open(local,'a')

    arquivo.write('\n\n\n\n')

    for x in news_task:
        arquivo.write(x)

    arquivo.close()
    print('Novas tasks foram adicionadas!')