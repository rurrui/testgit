import re

# 匹配电话号码,例如010-12345678，0356-3647440，(010)12345678,(0356)3647440
regular_str = r'0\d{2}-\d{8}|0\d{3}-\d{7}|\(0\d{2}\)\d{8}'
print('请输入测试号码')
str = input()
if re.match(regular_str, str):
    print('ok')
else:
    print('no')
