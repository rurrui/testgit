# 使用一个lock解决多线程的资源争夺现象
import threading

# init balance
balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def thread_run(n):
    for i in range(100000):
        # 获取锁
        lock.acquire()
        try:
            # 可以不受干扰的使用chang_it方法
            change_it(n)
        finally:
            # 释放锁
            lock.release()


t1 = threading.Thread(target=thread_run, args=(5,))
t2 = threading.Thread(target=thread_run, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
