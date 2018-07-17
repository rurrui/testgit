[x*x for x in range(1,11)]
[x*x for x in range(1,11) if x%2==0]
[m+n for m in 'ABC' for n in 'XYZ']
#display the files under the current folder
import os
[d for d in os.listdir('.')]
[d for d in os.listdir('C:')]
# list comprehesions dict
dic={'x':'A','y':'B','z':'C'}
[k+'='+v for k,v in dic.items()]
#Uppercase To Lowercase
L1 = ['Hello', 'World', 18, 'Apple', None]
[s.lower() for s in L1 if isinstance(s,str)]
