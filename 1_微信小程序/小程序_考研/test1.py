import json

data = open('response.json', 'r',encoding='utf-8')
data = json.load(data)
with open('response1.json', 'w',encoding='utf-8') as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=4))
