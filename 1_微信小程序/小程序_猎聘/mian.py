import requests
import json


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Referer": "https://servicewechat.com/wx4d70579bfaefd959/422/page-frame.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
    "x-client-type": "wxa",
    "x-fscp-bi-stat": "{\"virtual_device_id\":\"5mi7d22eiepk7cxa\"}",
    "x-fscp-std-info": "{\"client_id\":80001,\"version\":\"3.13.15\",\"version_code\":31315,\"dev_type\":1,\"channel_code\":\"mp_tx_weixin\"}",
    "x-fscp-trace-id": "t5qu8qreyjl85r8b",
    "x-fscp-version": "1.1",
    "xweb_xhr": "1"
}
cookies = {
    "_mscid": "cx_wx_01",
    "__gc_id": "4f724111392146428cd299faf80c0de6",
    "__sessionId": "wsvnkcnlwmddj5ja",
    "acw_tc": "ac11000117442648079312603e0063c6a2555233623b1c7177d265d21a20ea",
    "XSRF-TOKEN": "77iUiFkuT4KiwDmIRSeQSg",
    "__uuid": "opSQK0f8t1m3Mhxy7wJvOfLpeKdo",
    "UniqueKey": "5688ef2df986b97941344312b1f2ca2b",
    "liepin_login_valid": "0",
    "lt_auth": "sukMMn0Gy1j97SGMiGBdt6lN29qoVWqf%2FChY0UoBhYK%2BW%2FHj4P%2FqRgiPq7AO%2BioIqxkjJPwzMLf6Mer4zXtM7UUT%2BFGkk565t%2FOz1H8KHbVsLfjygPaoks%2BDSJ0jkHkJzHpkr3EZlRr%2BigQbcr768FLxt5jW7rec88vPswW%2FgTE%3D",
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
        "existFallbackResult": True
    },
    "version": "3.13.15",
    "version_code": 31315,
    "dev_type": 1,
    "client_id": 80001
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)