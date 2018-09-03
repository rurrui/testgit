import threading

# 为了让每个线程使用不同的变量，我们可以使用threadlocal来实现
# 创建一个全局thread_local变量
global_school = threading.local()


def process_student():
    # 获取当前线程变量的值
    std = global_school.student
    print('Hello,%s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    global_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('wzh',), name='thread_1')
t2 = threading.Thread(target=process_thread, args=('rurui',), name='thread_2')
t1.start()
t2.start()
t1.join()
t2.join()
