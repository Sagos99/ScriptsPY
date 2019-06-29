from time import sleep
import codecs
from pyperclip import copy


global name
name = '[Script]'

def load_config():
    try:
        print(name,'Carregando arquivo de configuração...')
        arquivo = open('config.cfg', "r")
        linha = int(arquivo.readline())
        arquivo.close()
        print(name,'Arquivo carregado!\n')
        return linha

    except:
        print(name,'Arquivo não encontrado, Criando novo arquivo...')
        arquivo = open('config.cfg', 'w')
        arquivo.writelines('0')
        arquivo.close()
        print(name,'Arquivo de configuração criado!')
        return 0

def load_local():
    try:
        arquivo = open('local.txt', "r")
        local = arquivo.read()
        arquivo.close()
        return local

    except:
        print(name,'Por favor configure o arquivo local...')
        return ''


def read_client():
    try:
        path = load_local()
        arquivo = codecs.open(path+'Client.txt', encoding='utf-8')
        lista = arquivo.readlines()
        arquivo.close()

        # Retorna o número de linhas e a última linha do arquivo
        return [len(lista),lista[len(lista)-1]]
    except:
        return 0,''


old_qty = load_config()
current_qty,texto = read_client()

while True:
    sleep(0.5)

    if '@From' in texto and old_qty != current_qty and '] #' not in texto:
        position = 0
        arquivo = open('config.cfg', 'w')
        arquivo.writelines(str(current_qty))
        arquivo.close()
        old_qty = current_qty

        for letra in texto:
            position += 1
            if '@' == letra:
                break

        texto = texto[position-1:]
        print(texto)

        if 'your' in texto and 'for' in texto:
            words = texto.split(' ')
            active = False
            item = ''

            for word in words:
                if active == True and word not in 'listed for':
                    item = item+word+' '
                if word == 'your':
                    active = True

                if word == 'for':
                    active = False

            item = item[:len(item)-1]
            copy(item)
    else:
        current_qty,texto = read_client()