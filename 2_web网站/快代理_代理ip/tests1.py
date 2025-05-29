import requests

IP = {'http': '117.42.94.228:20079'}  # 指定对应的 IP 进行访问网址
print(IP)
try:
    r = requests.get('https://www.bilibili.com/', proxies=IP,
                     timeout=3)  # proxies 设定对应的代理 IP 进行访问， timeout 设定相应的时间之后停止等待响应
    print('ok')
except:
    print("无效")
