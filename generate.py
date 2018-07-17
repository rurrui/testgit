g=(x*x for x in range(10))
next(g)
next(g)
next(g)
next(g)
next(g)
#Fabonacci
def fib(max):
    n=0
    a=0
    b=1
    while n<max:
        print(b)
        a=b
        b=a+b
        n=n+1
    return 'done'
fib(10)
#Fabonacci generate
def fib2(Max):
    n,a,b=0,0,1
    while n<Max:
        yield b
        a=b
        b=a+b
        n=n+1
    return 'done'
g=fib2(6)
while True:
    try:
        x=next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break
