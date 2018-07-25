def count1():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count1()
f1()
f2()
f3()
#闭包
def a():
    x=10
    def b():
        x+=1
        print(x)
    return b
demo=a()
demo()