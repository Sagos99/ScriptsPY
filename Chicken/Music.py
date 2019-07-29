from time import sleep
import pafy
import vlc


Instance = vlc.Instance()
player = Instance.media_player_new()
pause = False

command_file = open('command.txt', 'w')
command_file.write('')
command_file.close()


def get_link():
    try:
        queue_file = open('queue.txt', 'r')
        queue = queue_file.read()
        queue_file.close()

        cut = queue.find('\n')

        if cut != -1:
            link = queue[0:cut]
            queue = queue[cut+1:]

            queue_file = open('queue.txt', 'w')
            queue_file.write(queue)
            queue_file.close()

            return link

        else:
            return ''

    except:
        queue_file = open('queue.txt', 'w')
        queue_file.close()
        link = ''

    return link



def play_music(link):
    pause = False
    video = pafy.new(link)
    best = video.getbest()
    playurl = best.url

    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()


def main():

    if player.is_playing() == 0 and pause == False:
        link = get_link()

        if link:
            play_music(link)

    else:
        command_file = open('command.txt', 'r')
        command = command_file.read()
        command_file.close()

        if command == "pause":
            player.set_pause(1)
        elif command == "resume":
            player.set_pause(0)

        command_file = open('command.txt', 'w')
        command_file.write('')
        command_file.close()


while True:
    main()
    sleep(0.5)