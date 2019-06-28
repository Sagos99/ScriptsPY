from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import sched, time


s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print("Doing stuff...")
    # do your stuff
    #s.enter(5, 1, do_something, (sc,))
    

s.enter(30, 1, do_something, (s,))

def start(bot, update):
    print(str(update.message.chat_id)+' '+update.message.chat['first_name']+': '+update.message.text)

    response_message = 'Olá '+update.message.chat['first_name']+' ^^'
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

    s.run()
    s.enter(30, 1, do_something, (s,))


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
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print('Iniciado: Cerbex\n')
    main()