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
#loop
names=['wzh','whvihs','rurui']
for name in names:
    print(name)
#the sum of 1 to 100
sum=0
for x in range(101):
    sum=sum+x
print(sum)
#while
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
#loop values
values=["111","222","3333"]
for a in values:
    print("hello "+a)
#break
n=0
while n<=100:
    if n>10:
        break
    print(n)
    n=n+1
print("end")
#continue
num=0
while num<10:
    num=num+1
    if num%2==0:
        continue
    print(num)