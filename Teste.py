# -*- coding: utf-8 -*-

from unicodedata import normalize


def formatar_texto(txt, codif='utf-8'):
    try:
        # Muda texto para maiúsculo, removendo espaços e acentos, limitando quantidade de caracteres para 10
        text = normalize('NFKD', txt.decode(codif).upper().replace(' ','')).encode('ASCII', 'ignore')[0:10]
    except:
        text = 'ERROR'

    return text



print(formatar_texto('Colégio Móbile'))