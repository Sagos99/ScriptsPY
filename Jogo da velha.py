campo = []
game_over = False
jogador = True
turno = 0

for x in range(0, 3):
  campo.append(["-"] * 3)

def print_campo(campo):
  global jogador
  print ("\n"*100)
  if jogador == True:
    print ("Turno do Jogador: X\n")
  else:
    print ("Turno do Jogador: O\n")
  print ("  A B C")
  num = 1
  for linha in campo:
    print (str(num)," ".join(linha))
    num += 1
  print ("\n"*5)

print_campo(campo)

def jogar():
  global jogador,game_over,turno

  jogada = input("Digite um campo: ").lower()

  while True:
    if len(jogada) < 2:
      jogada = input("Entrada Inválida, Tente novamente: ").lower()
    elif not jogada[0] in "abc":
     jogada = input("Entrada Inválida, Tente novamente: ").lower()
    elif not jogada[1] in "123":
      jogada = input("Entrada Inválida, Tente novamente: ").lower()
    else:
      if jogada[0] == "a":
        y = 0
      elif jogada[0] == "b":
        y = 1
      else:
        y = 2
    
      x = int(jogada[1])-1
      break

  if campo[x][y] == "-":
    if jogador == True:
      campo[x][y] = "X"
      jogador = False
      turno += 1
    else:
      campo[x][y] = "O"
      jogador = True
      turno += 1
  else:
    print ("Espaço já ocupado, escolha outro campo")
    jogar()

  print_campo(campo)

  if campo[0][0] == "X" and campo[0][1] == "X" and campo[0][2] == "X":
    print ("X Venceu")
    game_over = True
  elif campo[1][0] == "X" and campo[1][1] == "X" and campo[1][2] == "X":
    print ("X Venceu")
    game_over = True
  elif campo[2][0] == "X" and campo[2][1] == "X" and campo[2][2] == "X":
    print ("X Venceu")
    game_over = True
  elif campo[0][0] == "X" and campo[1][0] == "X" and campo[2][0] == "X":
    print ("X Venceu")
    game_over = True
  elif campo[0][1] == "X" and campo[1][1] == "X" and campo[2][1] == "X":
    print ("X Venceu")
    game_over = True
  elif campo[0][2] == "X" and campo[1][2] == "X" and campo[2][2] == "X":
    print ("X Venceu")
    game_over = True
  elif campo[0][0] == "X" and campo[1][1] == "X" and campo[2][2] == "X":
    print ("X Venceu")
    game_over = True
  elif campo[0][2] == "X" and campo[1][1] == "X" and campo[2][0] == "X":
    print ("X Venceu")
    game_over = True
  elif campo[0][0] == "O" and campo[0][1] == "O" and campo[0][2] == "O":
    print ("Bolinha Venceu")
    game_over = True
  elif campo[1][0] == "O" and campo[1][1] == "O" and campo[1][2] == "O":
    print ("Bolinha Venceu")
    game_over = True
  elif campo[2][0] == "O" and campo[2][1] == "O" and campo[2][2] == "O":
    print ("Bolinha Venceu")
    game_over = True
  elif campo[0][0] == "O" and campo[1][0] == "O" and campo[2][0] == "O":
    print ("Bolinha Venceu")
    game_over = True
  elif campo[0][1] == "O" and campo[1][1] == "O" and campo[2][1] == "O":
    print ("Bolinha Venceu")
    game_over = True
  elif campo[0][2] == "O" and campo[1][2] == "O" and campo[2][2] == "O":
    print ("Bolinha Venceu")
    game_over = True
  elif campo[0][0] == "O" and campo[1][1] == "O" and campo[2][2] == "O":
    print ("Bolinha Venceu")
    game_over = True
  elif campo[0][2] == "O" and campo[1][1] == "O" and campo[2][0] == "O":
    print ("Bolinha Venceu")
    game_over = True
  elif turno == 9:
    print ("Empate!")
    game_over = True

while game_over == False:
  jogar()