# 测试多进程间的数据传输，使用queue
from multiprocessing import Process, Queue
import os


# 为queue赋值的子进程方法
def set(q):
    print('Child Process %s is start' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s in queue' % value)
        q.put(value)


# 取值queue的子进程方法
def get(q):
    print('Child Process %s is start' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue' % value)


if __name__ == '__main__':
    # 父进程创建队列
    q = Queue()
    pw = Process(target=set, args=(q,))
    pr = Process(target=get, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
