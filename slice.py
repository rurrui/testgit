L=list(range(100))
L
L[0:10]
L[0:10:2]
L[-10:]
L[-10:-1]
#function trim()
def trim(s):
    while 1:
        if s[:1]!=' ' and s[-1:]!=' ':
            break
        elif s[:1]==' ':
            s=s[1:]
        else:
            s=s[:-1]
    return s
n=input("please input a string")
print(trim(n))
