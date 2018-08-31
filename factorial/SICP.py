# SICP

def fac(n, acc=1):
    if n > 1:
        return (fac((n - 1), (acc * n)))
    else:
        return acc


print(fac(6))
