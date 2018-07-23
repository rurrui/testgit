#filter函数返回类型为Iterator，是一个惰性序列
def not_empty(s):
    return s and s.strip()
list(filter(not_empty,['a','','b',None]))
#利用filter实现素数生成
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it=_odd_iter()    #初始化序列
    while True:
        n=next(it)    #返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it)
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break