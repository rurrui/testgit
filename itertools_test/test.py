import itertools

# 生成一个无限迭代器
'''
natuals=itertools.count(1)
for n in natuals:
    print(n)
'''
# 生成一个传入序列的无限迭代器
'''
cs=itertools.cycle('abc')
for c in cs:
    print(c)
'''

# 可以控制生成的次数
'''
ns=itertools.repeat('wzh',3)
for n in ns:
    print(n)
'''

# takewhile使无限迭代器
'''
control_natuals=itertools.count(1)
cns=itertools.takewhile(lambda x:x<=10,control_natuals)
for n in cns:
    print(n)
'''

# groupby()把相邻的相同元素分组挑出来
'''
for key,group in itertools.groupby('AAABBBCCCDDD'):
    print(key,list(group))
'''
# groupby()的作用函数,可以使upper使大小写忽略后对每个元素分组
for key,group in itertools.groupby('AAaBbbCcc',lambda c: c.upper()):
    print(key,list(group))

def pi(N):
    