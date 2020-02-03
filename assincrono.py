from multiprocessing import Process
from time import sleep

def teste01(num=0):
    while True:
        num += 1
        print('Primeiro: '+str(num))
        sleep(2)

def teste02(num=0):
    while True:
        num += 1
        print('Segundo: '+str(num))
        sleep(0.7)



if __name__ == "__main__":
    t1 = Process(target=teste01)
    t2 = Process(target=teste02)

    t1.start()
    t2.start()

    t1.join()
    t2.join()