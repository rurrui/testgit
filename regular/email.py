import re

# 设计一个可以匹配类似rurui@live.com的正则表达式
regular_email = r'^([0-9a-zA-Z\.]*)\@([0-9a-zA-Z]*)\.com'
print('input a email:')
test_email = input()
if re.match(regular_email, test_email):
    m = re.match(regular_email, test_email)
    print(m.groups())
    print('ok')
else:
    print('no')
