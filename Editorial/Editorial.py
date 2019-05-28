# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from datetime import date
import unirest


def get_link(response,pos_inicial=0,pos_final=0):
    trava = False
    link = ''

    while trava == False:
        if response.body[pos_final] != '"':
            link += response.body[pos_final]
            pos_final += 1
        else:
            trava = True

    return link


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


def editorial(texto):
    folha = 'https://www1.folha.uol.com.br/opiniao/'
    editorial = unirest.get(folha)

    mes = str(date.today().month) if date.today().month >= 10 else '0'+str(date.today().month)
    data = str(date.today().year)+'/'+mes+'/'

    pos_inicial = editorial.body.find(folha+data)
    pos_final = pos_inicial
    link1 = unirest.get(get_link(editorial,pos_inicial,pos_final))

    pos_inicial = editorial.body.find(folha+data, pos_inicial+1)
    pos_inicial = editorial.body.find(folha+data, pos_inicial+1)
    pos_inicial = editorial.body.find(folha+data, pos_inicial+1)
    pos_final = pos_inicial
    link2 = unirest.get(get_link(editorial,pos_inicial,pos_final))

    if texto == 1:
        pos_inicial = link1.body.find('<p>')
        pos_final = link1.body.find('<div class="c-news__stars u-no-print js-continue-reading-hidden">',pos_inicial)
        texto1 = format_text(link1.body[pos_inicial:pos_final])
        titulo = link1.body[link1.body.find('<title>')+7:link1.body.find('</title>')]+'\n\n'

        return titulo+texto1
    else:
        pos_inicial = link2.body.find('<p>')
        pos_final = link2.body.find('<div class="c-news__stars u-no-print js-continue-reading-hidden">',pos_inicial)
        texto2 = format_text(link2.body[pos_inicial:pos_final])
        titulo = link2.body[link2.body.find('<title>')+7:link2.body.find('</title>')]+'\n\n'
        
        return titulo+texto2


def start(bot, update):
    print(update.message.chat['first_name']+': '+update.message.text)

    response_message = "Digite /texto1 ou /texto2 para obter os editoriais"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def texto1(bot, update):
    print(update.message.chat['first_name']+': '+update.message.text)

    response_message = editorial(1)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def texto2(bot, update):
    print(update.message.chat['first_name']+': '+update.message.text)
    
    response_message = editorial(2)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def unknown(bot, update):
    print(update.message.chat['first_name']+': '+update.message.text)
    
    response_message = "Comando não encontrado, Digite /texto1 ou /texto2 para obter os editoriais"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token='825493456:AAE8L0hsuywcXH4tkRSRgn7UBk84j_eKvPA')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('texto1', texto1))
    dispatcher.add_handler(CommandHandler('texto2', texto2))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("Iniciado: Folha editorial\n")
    main()