import re

regular_str = r'\bhi\b.*\bLucky\b'
str = 'uhiqwLucky'
if re.match(regular_str, str):
    print('ok')
else:
    print('no')
