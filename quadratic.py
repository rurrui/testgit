#utf_8
import math
def quadramatic(a,b,c):
    dirt=(b*b)-(4*a*c)
    if dirt<0:
        print("无解")
    elif dirt==0:
        x=(-b)/(2*a)
        print(x)
    else:
        x1=(-b)+math.sqrt(dirt)/(2*a)
        x2=(-b)-math.sqrt(dirt)/(2*a)
        print(x1)
        print(x2)
quadramatic(1,3,-4)