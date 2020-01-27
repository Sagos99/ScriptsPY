from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from multiprocessing import Process
from datetime import datetime


path_history = 'files/history.txt'
token = '1046877700:AAEayRhNPKIzb3g-wVb0nAttbxkPI_ZqZXk'


# Caso o arquivo de histórico não exista, cria
try:
    history_file = open(path_history, 'r')
    history_file.close()
except:
    history_file = open(path_history, 'w')
    history_file.close()


# Função para guardar todas as mensagens enviadas ao bot
def history(msg):
    history_file = open(path_history, 'a')
    history_file.write(msg+'\n')
    history_file.close()
    print(msg)


# Função para mostrar os logs
def logger(update):
    if update:
        log = datetime.strftime(datetime.now(), '%H:%M:%S %d/%m/%Y')
        log += ' '+str(update.message.chat_id)+' '+update.message.chat['first_name']+': '+update.message.text
        return log
    else:
        return 'Erro: objeto vazio'


# Função responsável por enviar todos os tipos de mensagens aos usuários
def setAnswer(user,message):
    if message:
        message = message.replace('&','')
        answer = requests.get('https://api.telegram.org/bot'+str(token)+'/sendMessage?chat_id='+str(user)+'&text='+str(message))
        return True
    else:
        return False


# Função para dar boas vindas a novos usuários
def start(bot, update):
    history(logger(update))

    response_message = 'Digite /help para ver os comandos'
    tSetAnswer.start(update.message.chat_id,response_message)
    tSetAnswer.join()


# Função para mostrar uma mensagem de ajuda aos usuários
def getHelp(bot, update):
    history(logger(update))
    response_message = "/km Quilômetros\n\nnovos comandos em breve"

    tSetAnswer.start(update.message.chat_id,response_message)
    tSetAnswer.join()


def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', getHelp))

    updater.start_polling()
    updater.idle()


tSetAnswer = Process(target=setAnswer)


if __name__ == '__main__':

    print('Professor Oak online!')
    main()