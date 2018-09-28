import json

l = [1, 2, 3, 'wzh', 'rurui', 'whvihs']
with open(r'jsonwrite2.json', 'w') as f:
    json.dump(l, f)
