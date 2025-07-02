import requests

url='http://api.socks5.io/user_get_ip_list?token=heukGZ8xfJQELPhL1710306791930&type=dc&qty=1&country=&time=5&format=txt&filter=1'

response=requests.get(url)
print(response.text)