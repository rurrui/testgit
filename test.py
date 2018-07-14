a='abc'
b=a
a='cba'
print(b)
s1=72
s2=85
r=(s2-s1)/s1*100
print('%.2f%%' % r)
#list && tuple
L=[
    ['Apple','Google','Microsoft'],
    ['Java','Python','c#','C++'],
    ['Adam','Bart','Lisa']
]
print(L[0][1])
print(L[1][1])
print(L[2][2])
#list append/insert/pop
list=['wzh','whvihs','ldm']
print(list)
list.append('rurui')
print(list)
list.insert(1,'rurrui')
print(list)
list.pop(1)
print(list)
#if elif
height=1.75
weight=80.5
bmi=weight/(height*height)
print(bmi)
if bmi<18.3:
    print('very thin')
elif bmi<25:
    print('normal')
elif bmi<28:
    print("over noral")
elif bmi<32:
    print("obesity")
else:
    print("very obesity")