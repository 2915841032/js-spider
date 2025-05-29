import requests

cookies = {
    'qgqp_b_id': '9bdb9ca9b646fe394967659dc65eaf73',
    'st_si': '58046925978346',
    'st_asi': 'delete',
    'isoutside': '0',
    'st_pvi': '98779991159654',
    'st_sp': '2023-05-30%2020%3A50%3A41',
    'st_inirUrl': 'https%3A%2F%2Fwww.bing.com%2F',
    'st_sn': '13',
    'st_psi': '20230827133617813-113200301712-8206466277',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'qgqp_b_id=9bdb9ca9b646fe394967659dc65eaf73; st_si=58046925978346; st_asi=delete; isoutside=0; st_pvi=98779991159654; st_sp=2023-05-30%2020%3A50%3A41; st_inirUrl=https%3A%2F%2Fwww.bing.com%2F; st_sn=13; st_psi=20230827133617813-113200301712-8206466277',
    'Pragma': 'no-cache',
    'Referer': 'http://quote.eastmoney.com/zixuan/?from=favor',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'codes': '0.159605,0.000963,0.002038,1.603087,0.399989,0.000977,0.002245,0.159934,0.399001,1.000001,0.002511,1.512760,0.300842,0.300059',
}

response = requests.get(
    'http://quote.eastmoney.com/zixuan/api/info/infomines',
    params=params,
    # cookies=cookies,
    headers=headers,
    verify=False,
)
print(response.text)