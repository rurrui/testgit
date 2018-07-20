#prod
from functools import reduce
def fn(x,y):
    return int(x)*int(y)
def prod(l):
    return reduce(fn,l)
l=list(input("please input list"))
a=prod(l)
print(a)
