from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from multiprocessing import Process
from datetime import datetime
import requests


path_history = 'files/history.txt'
token = '1046877700:AAEayRhNPKIzb3g-wVb0nAttbxkPI_ZqZXk'


# Caso o arquivo de histórico não exista, cria
try:
    history_file = open(path_history, 'r')
    history_file.close()
except:
    history_file = open(path_history, 'w')
    history_file.close()


# Função para guardar e mostrar todas as mensagens enviadas ao bot
def history(msg):
    history_file = open(path_history, 'a')
    history_file.write(msg+'\n')
    history_file.close()
    print(msg)


# Função que monta os logs com data e hora e ID de cada usuário
def logger(update):
    if update:
        log = datetime.strftime(datetime.now(), '%H:%M:%S %d/%m/%Y')
        log += ' '+str(update.message.chat_id)+' '+update.message.chat['first_name']+': '+update.message.text
        return log
    else:
        return 'Erro: objeto vazio'


# Função responsável por enviar todos os tipos de mensagens aos usuários
def setAnswer(user,message):
    print('entro aqui')
    if user and message:
        message = message.replace('&','')
        answer = requests.get('https://api.telegram.org/bot'+str(token)+'/sendMessage?chat_id='+str(user)+'&text='+str(message))
        # https://api.telegram.org/bot1046877700:AAEayRhNPKIzb3g-wVb0nAttbxkPI_ZqZXk/sendMessage?chat_id=556607954&text=Mensagenzinha
        return True
    else:
        return False


# Função para dar boas vindas a novos usuários do privado
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


# Cria os objetos para ser assincrono
tSetAnswer = Process(target=setAnswer)


def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', getHelp))

    updater.start_polling()
    updater.idle()


#if __name__ == '__main__':
print('Professor Oak online!')
tSetAnswer = Process(target=setAnswer)
main()