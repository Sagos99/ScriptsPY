local = "/Users/samuel/Sagos/Notes/Tags for commit.txt"

arquivo = open(local,"r")

for linha in arquivo:
    print(linha)

arquivo.close()