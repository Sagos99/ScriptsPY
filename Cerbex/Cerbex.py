# -*- coding: utf-8 -*-
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import unirest


def start(bot, update):
    print(str(update.message.chat_id)+' '+update.message.chat['first_name']+': '+update.message.text)

    response_message = 'Olá '+update.message.chat['first_name']+' ^^'
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def ditto(bot, update):
    print(str(update.message.chat_id)+' '+update.message.chat['first_name']+': '+update.message.text)

    response_message = u'Possíveis aparições de ditto:\n\n'

    response = unirest.get("https://pokemon-go1.p.rapidapi.com/possible_ditto_pokemon.json",
    headers={
        "X-RapidAPI-Host": "pokemon-go1.p.rapidapi.com",
        "X-RapidAPI-Key": "e9b0d5fec5msh4383c8fa32ee394p1b7c53jsn938b9968e3c7"
    }
    )

    for item in response.body:
        response_message += response.body.get(item).get('name')+u'\n'


    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def unknown(bot, update):
    print(str(update.message.chat_id)+' '+update.message.chat['first_name']+': '+update.message.text)
    
    response_message = "Comando não encontrado."
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token='806322217:AAGzhhAVnQDDIE-FSlWGnLlV48eH1Xyfg8c')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ditto', ditto))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print('Iniciado: Cerbex\n')
    main()