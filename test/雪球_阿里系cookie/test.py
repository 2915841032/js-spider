import re

import requests


def get_cookie():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }

    url = 'https://xueqiu.com/today'
    response = requests.get(url, headers=headers)
    print(response.text)
    arg1 = re.findall("var arg1='(.*?)';", response.text)[0]
    acw_tc = response.cookies.get('acw_tc')
    return arg1, acw_tc

if __name__ == '__main__':
    arg1, acw_tc = get_cookie()
    print(arg1, acw_tc)
