from io import StringIO

f=StringIO('HI\nWZh\nLOVE')
while True:
    line=f.readline()
    if line:
        print(line.strip())
    else:
        break