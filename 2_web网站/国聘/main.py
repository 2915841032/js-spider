import requests
import json


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "device": "pc",
    "origin": "https://www.iguopin.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.iguopin.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "subsite": "iguopin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}
url = "https://gp-api.iguopin.com/api/jobs/v1/recom-job"
data = {
    "search": {
        "page": 3,
        "page_size": 20,
        "keyword": "Python",
        "remove_job_id": [
            "142511160397136179",
            "142511158132212019",
            "142498998576480560",
            "142409810577457459",
            "142351200665207088",
            "142396855244821324",
            "142395872469057843",
            "142270004123926834",
            "142153299544506451",
            "140658993180709165",
            "140659410144857843",
            "139599065045274357",
            "133956002306329259",
            "141236327935906091",
            "141485653354348630",
            "141113252728803062",
            "141113256419790582",
            "142409704126021942",
            "142396384224482124",
            "142396387110163276"
        ]
    },
    "recom": {
        "update_time": True,
        "company_nature": True,
        "hot_job": True
    }
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)