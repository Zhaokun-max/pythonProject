import multiprocessing
from time import sleep, ctime

def clock(interval):
    while True:
        print("The time is %s" % ctime())
        sleep(interval)


if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(1,))
    p.start()