from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

# namedtuple实现了一个可以以属性调用的tuple对象
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)

# deque适用于队列和栈，用于优化插入与删除操作，因为list是线性排列的，导致插入与删除操作效率会很低，所以使用deque代替
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

# 使用defaultdict时，对于不存在的key会返回一个缺省值
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

# 计数器
c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1
print(c)