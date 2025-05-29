import requests


headers = {
    "Host": "img.bosszhipin.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/11581",
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-dest": "image",
    "referer": "https://servicewechat.com/",
    "accept-language": "zh-CN,zh;q=0.9"
}
url = "https://img.bosszhipin.com/beijin/fe/build/20240219/5d8c272aec07216bc6db76fbae332728170b65e927d2730f6bb61e3b7bce0931da574d19d1d82c88.jpeg"
response = requests.get(url, headers=headers)

print(response.text)
print(response)
with open('1.jpg', 'wb') as f:
    f.write(response.content)