import re

str=re.match('^UTC[+-]+0?(\d*):\d*','UTC-12:00').groups(0)
print(str[0])
