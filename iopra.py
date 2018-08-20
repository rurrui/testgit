import io

# 一次读出所有文字
'''
with open('testio.txt','r',encoding='utf-8') as f:
    s=f.read()
print(s)
'''
# 一行一行读取
'''
with open('testio.txt','r',encoding='utf-8') as f:
    while True:
        line=f.readline()
        if line:
            print(line.strip())
        else:
            break
'''
# 一次读出所有行，再遍历输出
with open('testio.txt','r',encoding='utf-8') as f:
    lines=f.readlines()
    for line in lines:
        print(line.strip())    