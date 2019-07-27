from time import sleep


def get_link():
    try:
        queue_file = open('queue.txt', 'r')
        queue = queue_file.read()
        queue_file.close()

        queue = queue.split('\n')
            
        if queue[len(queue)-1] == '':
            queue.pop(len(queue)-1)

        link = queue[0]
        queue.pop(0)

    except:
        queue_file = open('queue.txt', 'w')
        queue_file.close()
        link = []

    return link


def main():
    link = get_link()

    print(link)

main()