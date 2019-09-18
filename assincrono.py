from multiprocessing import Process
from time import sleep

def teste01():
    while True:
        print('Teste01 sendo executado!')
        sleep(1)

def teste02():
    while True:
        print('Teste02 sendo executado!')
        sleep(0.5)



if __name__ == "__main__":
    t1 = Process(target=teste01)
    t2 = Process(target=teste02)

    t1.start()
    t2.start()

    t1.join()
    t2.join()