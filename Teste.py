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
        for i in range(0,6):
            novo_texto = novo_texto.replace('&nbsp;'[i],'')

    return novo_texto


texto = format_text("<p>eu tenho aqui&nbsp; um texto &nbsp;qualquer</p>")

print(texto)