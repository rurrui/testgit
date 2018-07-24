sorted([2,9,77,60,5])
sorted([2,9,77,60,5],reverse=True)
sorted(['Zpp','wzh','rurui','abc'],key=str.lower,reverse=True)
#
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L1=sorted(L,key=by_name)
print(L1)
def by_score(t):
    return t[1]
L2=sorted(L,key=by_score)
print(L2)