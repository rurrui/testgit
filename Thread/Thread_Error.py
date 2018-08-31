# this snippets test a problem of shared variable thar occured in thread

import threading, time

# your salary
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


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(5,))
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print('Multi Threads time is %s' % str(time.time() - start))
t3 = threading.Thread(target=run_thread2, args=(5,))
start2 = time.time()
t3.start()
t3.join()
print('Single Thread time is %s' % str(time.time() - start2))

