#filter函数返回类型为Iterator，是一个惰性序列
def not_empty(s):
    return s and s.strip()
list(filter(not_empty,['a','','b',None]))