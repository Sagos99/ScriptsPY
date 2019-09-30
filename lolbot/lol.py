from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import requests
import json



def getInfo(summonerName):
    APIKey = 'RGAPI-b4ddfc6b-29e3-47d4-a316-cbfcb3c8cfc2'

    summonerData  = requestSummonerData(summonerName, APIKey)
    rankedData = requestRankedData(summonerData['id'], APIKey)

    info = 'Invocador:\t'+str(summonerData['name'])+'\n'
    info += 'Level:\t'+str(summonerData['summonerLevel'])+'\n\n'

    wins = rankedData[0]['wins']
    losses = rankedData[0]['losses']
    ratio = wins / (wins + losses)

    info += 'Rank:\t\t'+rankedData[0]['tier'] + ' ' + rankedData [0]['rank'] + ' ' + str(rankedData [0]['leaguePoints']) + ' pdl\n'
    info += 'W/L:\t\t'+str(wins) + ' / ' +str(losses)+'\n'
    info += 'W/L Ratio:\t' + str(round((ratio) * 100.0, 2)) + '%\n'

    return info


def requestSummonerData(summonerName, APIKey):
    URL = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + APIKey
    response = requests.get(URL)
    return response.json()

def requestRankedData(ID, APIKey):
    URL = 'https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + str(ID) + '?api_key=' + APIKey
    response = requests.get(URL)
    return response.json()


# Integração com bot do Telegram
def start(bot, update):
    print(str(update.message.chat_id)+' '+update.message.chat['first_name']+': '+update.message.text)

    response_message = 'Digite /SeuNick'
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def infoAccount(bot, update):
    print(str(update.message.chat_id)+' '+update.message.chat['first_name']+': '+update.message.text)
    
    response_message = getInfo(update.message.text[1:])
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token='835912285:AAEU3R8O98WCxHW3UVnCWdgytzgzmyDnpD0')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.command, infoAccount))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print('Iniciado: Bot LoL BR\n')
    main()