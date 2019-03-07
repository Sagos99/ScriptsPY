import os.path


print("\n-------------[ Bem vindo ao sistema de Login ]--------------")
print("1 - Fazer Login")
print("2 - Criar conta")
print("3 - Ver contas existentes")
print("4 - Sair\n")

logado = False
login = None

contas = []
senhas = []
saldos = []

if not os.path.isfile("contas.txt"):    # verifica se contas.txt existe
    arquivo = open("contas.txt","w")
    arquivo.write("admin,admin")
    arquivo.close()

arquivo = open("contas.txt","r")

for linha in arquivo:
    corta = linha.split(",")
    contas.append(corta[0])
    monta = ""
    ultimo = corta[1]

    for letra in range(len(corta[1])-1):
        monta += corta[1][letra]

    senhas.append(monta)

else:
    senhas.pop(len(senhas)-1)
    senhas.append(ultimo)

arquivo.close()

def validaNick(verifica):
    nick = ""

    for n in verifica:
        if not "-" in n:
            nick += n

    if len(verifica) < 5 or len(verifica) > 16:
        print("Seu usuário precisa ter entre 5 a 16 caracteres")
        return None
    elif not nick.isalnum():
        print("Caracteres especiais não é permitido")
        return None
    elif verifica[0].isnumeric() or not verifica[0].isalnum():
        print("O primeiro caracter precisa ser letra")
        return None
    elif "-" in verifica[len(verifica)-1]:
        print("Seu usuário não pode terminar com traço")
        return None
    else:
        return verifica

def menuDeslogado(escolha):
    global contas
    global senhas
    global logado
    global login
    valido = False

    if escolha == "1":
        login = input("Digite seu login: ")

        if not login in contas:
            resposta = input("Este login não existe, Deseja criar uma nova conta? [s/n]: ")

            if resposta[0].lower() == "s":
                login = validaNick(login)
                logado = menuDeslogado("2")
                return False
            else:
                return False

        senha = input("Digite sua senha: ")

        for x in range(len(contas)):
            if login == contas[x] and senha == senhas[x]:
                valido = True

        if valido == True:
            print("\nLogado com sucesso")
            return True
        else:
            print("\nLogin ou senha inválidos")
            login = None
            return False

    elif escolha == "2":
        if login == None:
            while login == None:
                login = validaNick(input("Digite seu login a ser criado: "))

            if not login in contas:
                contas.append(login)
                senha = input("Digite sua senha: ")

                while senha == "":
                    print("Sua senha não pode ser vazia")
                    senha = input("Digite sua senha: ")

                conf_senha = input("Digite sua senha novamente: ")

                if senha == conf_senha:
                    senhas.append(senha)

                    arquivo = open("contas.txt","w")

                    arquivo.write(contas[0]+","+senhas[0])

                    for salvar in range(1,len(contas)):
                        arquivo.write("\n"+contas[salvar]+","+senhas[salvar])

                    arquivo.close()

                    print("\nConta criada com sucesso")
                    login = None
                    return False
                else:
                    print("\nAs senhas não coincidem")
                    contas.remove(login)
                    login = None
                    return False

            else:
                print("\nEste nome de usuário já existe")
                login = None
                return False
        else:
            contas.append(login)
            senha = input("Digite sua senha: ")
            conf_senha = input("Digite sua senha novamente: ")

            if senha == conf_senha:
                senhas.append(senha)

                arquivo = open("contas.txt","w")

                arquivo.write(contas[0]+","+senhas[0])

                for salvar in range(1,len(contas)):
                    arquivo.write("\n"+contas[salvar]+","+senhas[salvar])

                arquivo.close()

                print("\nConta criada com sucesso")
                return False
            else:
                print("\nAs senha não coincidem")
                contas.remove(login)
                login = None
                return False

    elif escolha == "3":
        print("\n"+str(contas))
        return False
    elif escolha == "4":
        print("Até logo!")
        print("------------------------------------------------------------")
        pass
    else:
        print("Opção inválida")
        return False

def menuLogado(opcao,adm):
    global logado
    global login

    if adm == True:
        if opcao == "1":
            pass
        elif opcao == "2":    # conta adm
            logado = False
            login = None
            print("Teste")
        else:
            print("Opção inválida")


    else:
        if opcao == "1":
            pass
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            logado = False
            login = None
        else:
            print("Opção inválida")


logado = menuDeslogado(input("Escolha uma Opção: "))

while logado == False:
    print("\n1 - Fazer Login")
    print("2 - Criar conta")
    print("3 - Ver contas existentes")
    print("4 - Sair\n")

    logado = menuDeslogado(input("Escolha uma Opção: "))

while logado == True:
    if login == "admin":
        print("\n1 - Apagar conta")
        print("2 - Logoff\n")

        opcao = menuLogado(input("Escolha uma Opção: "),True)
    else:
        print("\n1 - Sacar")
        print("2 - Depositar")
        print("3 - Transferir")
        print("4 - Logoff\n")

        opcao = menuLogado(input("Escolha uma Opção: "),False)