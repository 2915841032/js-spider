import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.iwencai.com",
    "Pragma": "no-cache",
    "Referer": "https://www.iwencai.com/unifiedwap/result?w=%E5%B0%8F%E7%B1%B3&querytype=stock",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "hexin-v": "A8Jw2WZ7EVgMlA0PhY5sv_eXE8Mhk8d8eJW68Qzb7vjiVWx99CMWvUgnCvLf",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://www.iwencai.com/gateway/urp/v7/landing/getDataList"
data = {
    "query": "小米",
    "urp_sort_way": "desc",
    "urp_sort_index": "最新涨跌幅",
    "page": "4",
    "perpage": "50",
    "addheaderindexes": "",
    "condition": "[{\"dateText\":\"\",\"ci\":false,\"indexName\":\"所属概念\",\"indexProperties\":[\"概念id 301278\",\"包含小米概念\"],\"source\":\"new_parser\",\"type\":\"index\",\"indexPropertiesMap\":{\"概念id\":\"301278\",\"包含\":\"小米概念\"},\"reportType\":\"null\",\"score\":0,\"node_type\":\"index\",\"chunkedResult\":\"小米\",\"domain\":\"abs_股票领域\",\"uiText\":\"所属概念是小米\",\"valueType\":\"_所属概念\",\"sonSize\":0}]",
    "codelist": "",
    "indexnamelimit": "",
    "logid": "9e806844a72c2d69d60cbe1f9e554847",
    "ret": "json_all",
    "sessionid": "9e806844a72c2d69d60cbe1f9e554847",
    "source": "Ths_iwencai_Xuangu",
    "date_range%5B0%5D": "20250310",
    "iwc_token": "0ac9fa9517415969794656255",
    "urp_use_sort": "1",
    "user_id": "Ths_iwencai_Xuangu_d2bft8aws64ony5v9gg58jegelhqrfn4",
    "uuids%5B0%5D": "24087",
    "query_type": "stock",
    "comp_id": "6836372",
    "business_cat": "soniu",
    "uuid": "24087"
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)