#map
def f(x):
    return x*x
L=list(map(f,[1,2,3,4,5,6,7,8,9]))
L
#Not map
M=[]
for n in [1,2,3,4,5,6,7,8,9]:
    M.append(f(n))
print(M)
#reduce strToint
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def strToint(s):
    def fn(x,y):
        return x*10+y
    def charToint(s):
        return DIGITS[s]
    return reduce(fn,map(charToint,s))
strToint('13579')
#practice
def normalize(name):
    str=''
    for n in range(len(name)):
        if n==0:
            str=name[n].upper()
        else:
            str=str+name[n].lower()
    return str
L1=['wZh','eWW','wq']
L2=list(map(normalize,L1))
print(L2)
