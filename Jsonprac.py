import json

'''
d=dict(name='wzh',age=23,score=99)
str=json.dumps(d)
print(str)
'''
# json写入
'''
with open('jsontest.txt','w') as f:
    json.dump(d,f)
'''
# loads把json字符串反序列化
json_str='{"name":"wzh","gender":"male","age":"23"}'
s=dict()
s=json.loads(json_str)
print(s)