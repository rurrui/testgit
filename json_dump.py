import json 


d={'name':'rurui','age':23,'score':23}
json.dumps(d)   # 把Python对像序列化
# 把序列化的json字符串写入json_dump.txt文件中
with open('json_dump.json','w') as f:
    json.dump(d,f,ensure_ascii=False)
print("ok")