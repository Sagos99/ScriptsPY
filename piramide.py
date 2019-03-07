from time import sleep
import random

letra = "O"
tamanho = random.randint(5,150)
velocidade = random.uniform(0.006,0.02)



a = ""


while True:
	for n in range(tamanho):
		print(a)
		a += letra
		sleep(velocidade)

	for n in range(tamanho):
		print(a)
		a = a[:-1]
		sleep(velocidade)

	tamanho = random.randint(5,150)
	velocidade = random.uniform(0.005,0.01)