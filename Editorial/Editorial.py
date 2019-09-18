# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from datetime import date
import unirest

    
def get_editorial(first_text):
    hoje = date.strftime(date.today(), '%d/%m/%Y')
    folha = 'https://www1.folha.uol.com.br/opiniao/editoriais/'
    editorial = unirest.get(folha)
    mes = str(date.today().month) if date.today().month >= 10 else '0'+str(date.today().month)
    data = str(date.today().year)+'/'+mes+'/'
    montando_link = folha.replace('editoriais/', data)
    pos_inicial = editorial.body.find(montando_link)

    if first_text == True:
        try:
            arquivo_texto1 = open('texto1.txt', 'r')
            editorial_txt1 = arquivo_texto1.read()
            arquivo_texto1.close()
        except:
            arquivo_texto1 = open('texto1.txt', 'w')
            editorial_txt1 = None
            arquivo_texto1.close()

        if editorial_txt1 and hoje not in editorial_txt1:
            pos_final = pos_inicial
            link1 = unirest.get(get_link(editorial,pos_inicial,pos_final))

            pos_inicial = link1.body.find('<p>')
            pos_final = link1.body.find('<div class="c-news__stars u-no-print js-continue-reading-hidden">',pos_inicial)
            texto1 = format_text(link1.body[pos_inicial:pos_final])
            titulo1 = link1.body[link1.body.find('<title>')+7:link1.body.find('</title>')]+'\n\n'
            editorial_txt1 = titulo1+texto1

            arquivo_texto1 = open('texto1.txt', 'w')
            arquivo_texto1.write(editorial_txt1)
            arquivo_texto1.close()

        return editorial_txt1

    else:
        try:
            arquivo_texto2 = open('texto2.txt', 'r')
            editorial_txt2 = arquivo_texto2.read()
            arquivo_texto2.close()
        except:
            arquivo_texto2 = open('texto2.txt', 'w')
            editorial_txt2 = None
            arquivo_texto2.close()

        if editorial_txt2 and hoje not in editorial_txt2:
            

            pos_inicial = editorial.body.find(montando_link, pos_inicial+1)
            pos_inicial = editorial.body.find(montando_link, pos_inicial+1)
            pos_inicial = editorial.body.find(montando_link, pos_inicial+1)
            pos_final = pos_inicial
            link2 = unirest.get(get_link(editorial,pos_inicial,pos_final))

            pos_inicial = link2.body.find('<p>')
            pos_final = link2.body.find('<div class="c-news__stars u-no-print js-continue-reading-hidden">',pos_inicial)
            texto2 = format_text(link2.body[pos_inicial:pos_final])
            titulo2 = link2.body[link2.body.find('<title>')+7:link2.body.find('</title>')]+'\n\n'
            editorial_txt2 = titulo2+texto2

            arquivo_texto2 = open('texto2.txt', 'w')
            arquivo_texto2.write(editorial_txt2)
            arquivo_texto2.close()

        return editorial_txt2


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


def response_bot(bot, update):
    print(update.message.chat['first_name']+': '+update.message.text)

    if update.message.text == '/start':
        bot.send_message(
            chat_id=update.message.chat_id,
            text='Digite /texto1 ou /texto2 para obter os editoriais'
        )
    elif update.message.text == '/texto1':
        bot.send_message(
            chat_id=update.message.chat_id,
            text=get_editorial(True)
        )
    elif update.message.text == '/texto2':
        bot.send_message(
            chat_id=update.message.chat_id,
            text=get_editorial(False)
        )
    else:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Comando não encontrado, Digite /texto1 ou /texto2 para obter os editoriais"
        )


def main():
    updater = Updater(token='716611915:AAHoL4tm3lk-ThRAFkxUJjX0toaU8PVXgas')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.command, response_bot))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("Iniciado: Folha editorial\n")
    main()