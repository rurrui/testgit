#utf-8
def product(*args):
    pro=1
    if len(args)<=0:
        print("No argument")
    else:
        for num in args:
            pro=pro*num
    print(pro)
L=[1,2,3,4,5]
product(*L)
