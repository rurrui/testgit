#dict
d={"wzh":99,"rurui":98,"whvihs":97}
d["wzh"]    
list=(1,2,3)
d[list]="1111"
d
#hex()
n=100
print(hex(n))
#my_abs
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x>0:
        return x
    else:
        return -x
#print(my_abs(-99))  
my_abs("1")
abs("1")