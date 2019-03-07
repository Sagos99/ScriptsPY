from tkinter import messagebox
from datetime import datetime as hr
from time import sleep as slp


print("Script Rodando...")

rdd = 0
h = input("Digite o horário: ")

if h == "":
	h = "11:40"

print("Alarme definido para %s" % (h))

def msg(hr):
	global rdd
	messagebox.showinfo("Despertador", "Hora atual: %s" % (hr))


while rdd == 0:
	hora = str(hr.today())[11:16]
	if hora == h:
		rdd = 1
		msg(hora)

print("Script Concluído")