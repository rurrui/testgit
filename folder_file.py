import os

fiels=[]
def find(path):
    list=os.listdir(path)
    for f in list:
        currentName=os.path.join(path,f)
        if(f=='$RECYCLE.BIN' or f=='System Volume Information'):
            continue
        elif os.path.isdir(currentName):
            find(currentName)
        elif os.path.isfile(currentName):
            fiels.append(currentName)
find('D:\\')
print(fiels)

