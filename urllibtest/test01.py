from urllib import request

url=r'https://github.com/rurrui'
with request.urlopen(url) as f:
    x=f.geturl()
    y=f.info()
    z=f.getcode()
    print(x)
    print(y)
    print(z)
    print(f.read().decode('utf-8'))