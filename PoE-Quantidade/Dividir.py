quantidade = int(input('Quantidade que o comprador deseja: '))
stack = int(input('Quantidade do stack: '))

pacote = 0

while quantidade >= stack:
    quantidade -= stack
    pacote += 1

if pacote >= 1 and quantidade >= 1:
    print('Você deve separar '+str(pacote)+' stacks e '+str(quantidade)+' item\n')
elif pacote == 0 and quantidade >= 1:
    print('Não precisa separar\n')
elif pacote >= 1 and quantidade == 0:
    print('Você deve separar '+str(pacote)+' stacks\n')


input('Pressione Enter para sair.')
