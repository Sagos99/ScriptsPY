def count_pack(stack_size, quantidade):
    pack = 0

    while quantidade > stack_size:
        quantidade -= stack_size
        pack += 1

    return str(pack)+' pack e '+str(quantidade)+' item\n'


stack_size = int(input('O quanto o item stacka? '))
quantidade = int(input('Quantidade que o cara pediu: '))

msg = count_pack(stack_size, quantidade)

print(msg)
input('Pressione enter para sair...')