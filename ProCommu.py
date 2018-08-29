from multiprocessing import Process, Queue
import os, time, random


# 写入子进程
def write(q):
    print('Process to write %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put %s to Queue' % value)
        q.put(value)
        time.sleep(random.random())


# 读出子进程
def read(q):
    print('Process to read %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue' % value)


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
