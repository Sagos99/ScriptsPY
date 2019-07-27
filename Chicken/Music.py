from time import sleep


def read_queue():
    try:
        queue_file = open('queue.txt', 'r')
        queue = queue_file.read()
        queue_file.close()

    except:
        queue = []
        queue_file = open('queue.txt', 'w')
        queue_file.close()

    return queue



def main():
    queue = read_queue()
    print(queue)
    queue.split('\n')
    print('\n')
    print(queue)



# while True:
#     main()
#     sleep(1)

main()