# -*- coding: utf-8 -*-


def format_text(texto):
    novo_texto = ''
    block = False

    for letra in texto:
        if block == False and letra != '<':
            novo_texto += letra

        if letra == '<':
            block = True
        elif letra == '>':
            block = False

    if '&nbsp;' in novo_texto:
        novo_texto = novo_texto.replace('&nbsp;','')

    return novo_texto


texto = format_text("<p>eu tenho aqui&nbsp; um texto &nbsp;qualquer em pt br & espero que funcione ; xD</p>")

print(texto)