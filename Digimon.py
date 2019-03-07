nome = None

while nome != 'exit':
    nome = input('Digite um nome: ')

    if nome != 'exit':
        digimon = nome[:len(nome)-3]+'mon'
        print('Nome digimon: %s\n' % (str(digimon)))

        arquivo = open("digimon.txt","a")
        arquivo.write(nome+' > '+digimon+'\n')
        arquivo.close()
else:
    print('Valeeeu, Faloooou!')