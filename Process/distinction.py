from multiprocessing import Process
import os, time

balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for x in range(1000000):
        change_it(n)


def run_thread2(n):
    for x in range(2000000):
        change_it(n)


if __name__ == '__main__':
    p1 = Process(target=run_thread, args=(5,))
    p2 = Process(target=run_thread, args=(5,))
    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Multi Processes time is %s' % str(time.time() - start))
    p3 = Process(target=run_thread2, args=(5,))
    start2 = time.time()
    p3.start()
    p3.join()
    print('Single Process time is %s' % str(time.time() - start2))
