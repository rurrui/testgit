#function findMinAndMax
def findMinAndMax(L):
    min=L[0]
    max=L[0]
    for num in L:
        if num<=L[0]:
            min=num
        else:
            max=num
    mam=(min,max)
    return mam
print(findMinAndMax([1,2,3,4,5]))