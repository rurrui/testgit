import io

file=open('xyz.txt')
while True:
    line =file.readline()
    if line:
        print(line[:-1])
    else:
        break