from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from datetime import date
import requests
import json


token = '801318402:AAGXLUMERy1QUgYTp5RKtHM4gE2zyLI0xcA'


def main():
    teste = json.loads(requests.get('https://api.telegram.org/bot'+token+'/getUpdates').text)
    requests.post('https://api.telegram.org/bot'+token+'/deleteWebhook')

    import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    print("Iniciado: PKGOHelpBot\n")
    main()