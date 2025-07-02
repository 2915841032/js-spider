
import requests


data = {
    'group': 'rpc-test',
    'action': 'clientTime'
}
res = requests.post('http://127.0.0.1:5620/business-demo/invoke', data=data)
print(res.text)