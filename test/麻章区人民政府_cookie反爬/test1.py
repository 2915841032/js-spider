import requests
import re
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

def get_cookie():
    url = 'http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc'
    response = requests.get(url, headers=headers)
    szxx_session = response.cookies.get('szxx_session')
    CSRF = re.findall("var _CSRF = '(.*?)';", response.text)
    return szxx_session, CSRF


def get_data():
    szxx_session, CSRF = get_cookie()
    cookies = {
        "szxx_session": szxx_session
    }
    headers['X-Csrf-Token'] = CSRF[0]
    url = "http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList"
    data = {
        "offset": "0",
        "limit": "20",
        "site_id": "759010",
        "time_from": "1669392000",
        "time_to": "1700582399"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)

    print(response.text)
    print(response)
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write(response.text)

get_data()