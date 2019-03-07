# -*- coding: utf-8 -*-

import pyautogui
from time import sleep
from vagalume import lyrics

artist_name = str(raw_input('Nome do artista: '))
song_name = str(raw_input('Nome da música: '))

sleep(6) # Tempo para dar um alt+tab

try:
    result = lyrics.find(artist_name, song_name)

    if result.is_not_found():
        print('Artista ou música não encontrados')
    else:
        pyautogui.typewrite(result.song.lyric, interval=0.1)
        pyautogui.typewrite('\n', interval=0.1)

except Exception as e:
    print('Erro ao buscar música: ', str(e))