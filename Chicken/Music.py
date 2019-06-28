from time import sleep


def read_queue():
    try:
        queue_file = open('queue.txt', 'r')
        queue = queue_file.read()
        queue_file.close()

        queue.split('\n') # Erro com esse \n

    except:
        queue = []
        queue_file = open('queue.txt', 'w')
        queue_file.close()

    return queue



def main():
    queue = read_queue()
    print(queue)

    import ipdb; ipdb.set_trace()



while True:
    main()
    sleep(1)