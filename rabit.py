# 
def RabitParent(mounth):
    count=mounth//3
    return (2*(count+1))
def RabitChildren(mounth):
    mounth-=3
    count=mounth//4
    n=0
    while n<count:
        n+=1
        RabitChildren(mounth)
    return pow(2,count-1)
def RabitTotal(mounth):
    num=RabitParent(mounth)+RabitChildren(mounth)
    return num
print(RabitTotal(7))