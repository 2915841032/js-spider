import requests
import json


headers = {
    "Host": "api-c.liepin.com",
    "x-fscp-version": "1.1",
    "x-fscp-std-info": "{\"client_id\":80001,\"version\":\"3.15.3\",\"version_code\":31503,\"dev_type\":1,\"channel_code\":\"mp_tx_weixin\"}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/13639",
    "Content-Type": "application/json",
    "xweb_xhr": "1",
    "x-fscp-trace-id": "663k4534wlur4s1a",
    "x-client-type": "wxa",
    "x-fscp-bi-stat": "{\"virtual_device_id\":\"kxe66rzwugxajeh9\"}",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx4d70579bfaefd959/440/page-frame.html",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
cookies = {
    "_mscid": "cx_wx_01",
    "__gc_id": "c543e57e79134e82a302c42b36975ff6",
    "__sessionId": "2ep02j4j09iizqv9",
    "__uuid": "opSQK0bgLnQDvWlmiCxViDzBpheE",
    "acw_tc": "ac11000117481582430066725e006abdd19ed34df1530e205cea90200c787f",
    "XSRF-TOKEN": "G56KYTOVQWq0mQ6bWq9gzg",
    "UniqueKey": "5688ef2df986b97941344312b1f2ca2b",
    "liepin_login_valid": "0",
    "lt_auth": "6bxfMn0Gy1j97SGMiGBdt6lN29qoVWqf%2FChY0UoBhYK%2BW%2FHj4P%2FqRgiPq7AO%2BioIqxJ9fv0zMLf6Pen7wXFP70UV%2BVGkk565t%2FOz1H8KHrVlLf2k1f30lMmDRZYglX8EwXtnoykRxkWm4S0yW5fT2WP5t5jX1o2my%2FP0iCyWqBg8",
    "FE-hasUserLogin": "true"
}
url = "https://api-c.liepin.com/api/com.liepin.csearch.clam.minipro-home-recommend-job"
data = {
    "data": {
        "sortType": "MP_STU_HP_MIX",
        "operateKind": "UP",
        "selectedExpect": {
            "expectId": 200123697572,
            "expectJobtitle": "NX0035",
            "expectDq": "180020",
            "expectIndustry": "000",
            "expectMonthSalaryLower": 8000,
            "expectMonthSalaryUpper": 10000,
            "expectSalmonths": 12,
            "expectJobtitleType": "0"
        },
        "existFallbackResult": False
    },
    "version": "3.15.3",
    "version_code": 31503,
    "dev_type": 1,
    "client_id": 80001
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data,verify=False)

print(response.text)
print(response)