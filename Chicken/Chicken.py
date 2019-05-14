# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from bs4 import BeautifulSoup
import urllib.request
import pafy
import vlc


class Play_music:
    
    fila = []
    block_queue = False

    url = ''
    video = None
    best = None
    playurl = None

    Instance = None
    player = None
    Media = None

    def start(self,bot, update):
        print(update.message.chat['first_name']+': '+update.message.text)

        response_message = "Digite /help para obter os comandos"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )


    def help(self,bot, update):
        print(update.message.chat['first_name']+': '+update.message.text)
        
        response_message = "/play nome_da_música ou url\n/pause pausa a música\n/resume continua a música atual\n/np mostra o nome da atual música"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )


    def fila(self,link,bot,update):

        if self.video != None and self.player.is_playing() == 1:
            bot.send_message(
                chat_id=update.message.chat_id,
                text='A fila não está pronta T.T'
            )

            # bot.send_message(
            #     chat_id=update.message.chat_id,
            #     text='Adicionado a fila: '+pafy.new(self.link).title
            # )
        else:
            if self.player != None:
                self.player.stop()

            self.url = link
            self.video = pafy.new(self.url)
            self.best = self.video.getbest()
            self.playurl = self.best.url

            self.Instance = vlc.Instance()
            self.player = self.Instance.media_player_new()
            self.Media = self.Instance.media_new(self.playurl)
            self.Media.get_mrl()
            self.player.set_media(self.Media)
            self.player.play()

            bot.send_message(
                chat_id=update.message.chat_id,
                text='Reproduzindo: '+self.video.title
            )


    def play(self,bot, update):
        print(update.message.chat['first_name']+': '+update.message.text)
        
        try:
            textToSearch = update.message.text.split(' ',1)[1]

            query = urllib.parse.quote(textToSearch)
            url = "https://www.youtube.com/results?search_query=" + query
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                link = 'https://www.youtube.com' + vid['href']
                break

            self.fila(link,bot,update)

        except Exception as e:
            print('Erro: '+str(e))
            bot.send_message(
                chat_id=update.message.chat_id,
                text='Oops, digite o nome de uma música ou envie a url'
            )


    def pause(self,bot, update):
        print(update.message.chat['first_name']+': '+update.message.text)
        
        if self.block_queue == False:
            self.block_queue = True
            self.player.set_pause(1)
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text='Oops, a música já está pausada'
            )

    def resume(self,bot, update):
        print(update.message.chat['first_name']+': '+update.message.text)

        if self.block_queue == True:        
            self.block_queue = False
            self.player.set_pause(0)
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text='Oops, a música já está tocando'
            )


    def np(self,bot, update):
        print(update.message.chat['first_name']+': '+update.message.text)

        if self.video != None and self.player.is_playing() == 1:
            bot.send_message(
                chat_id=update.message.chat_id,
                text='Tocando no momento: '+self.video.title
            )
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text='Nenhuma música tocando no momento.'
            )


    def unknown(self,bot, update):
        print(update.message.chat['first_name']+': '+update.message.text)
        
        response_message = "Comando não encontrado\nDigite /help para obter os comandos"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )


    def main(self):
        updater = Updater(token='823044227:AAH2fTfEVflRAfLWBRLWHgdulRVQ7BnwjD8')
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler('start', self.start))
        dispatcher.add_handler(CommandHandler('help', self.help))
        dispatcher.add_handler(CommandHandler('play', self.play))
        dispatcher.add_handler(CommandHandler('pause', self.pause))
        dispatcher.add_handler(CommandHandler('resume', self.resume))
        dispatcher.add_handler(CommandHandler('np', self.np))
        dispatcher.add_handler(MessageHandler(Filters.command, self.unknown))

        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    print("ChickenMusic iniciado!\n")    
    Play_music().main()