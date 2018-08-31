# this snippets test a problem of shared variable thar occured in thread

import threading

# your salary
balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for x in range(1000000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
# note
# 由于两个线程使用了共享变量balance，多线程执行并非同时进而是切换执行所以
# 导致balance计算会被两个线程争夺，从而导致balance最终计算结果不为0