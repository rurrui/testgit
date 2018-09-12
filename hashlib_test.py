import hashlib

md5 = hashlib.md5()
md5.update('wzhuiyigedauyge'.encode('utf-8'))
print(md5.hexdigest())
md6 = hashlib.md5()
md6.update('wzhuiyigedauyga'.encode('utf-8'))
print(md6.hexdigest())
print(len(md6.hexdigest()))