import io

try:
    f=open(r'C:\Users\rurui\Desktop\hello.txt','r')
    print(f.read())

finally:
    if f:
        f.close()
# 可以使用一种更为简单的语法糖，引入with语句帮我们执行f.close()
print("================================================")
with open(r'C:\Users\rurui\Desktop\hello.txt','r') as f:
    print(f.read(-1))
    print("=================================================")
    line=f.readline()
    #print(f.readline(-1)
f1=open('xyz.txt','r')
for line in open('xyz.txt'):
    print(line)
