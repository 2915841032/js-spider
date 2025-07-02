import json
import requests
from requests import Session

# Create a session object
session = Session()

# Set common headers
session.headers.update({
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "http://htgs.ccgp.gov.cn/GS8/contractpublish/index",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "X-Requested-With": "XMLHttpRequest"
})

# Set cookies
session.cookies.update({
    "$HMF_CI": "bf62b4d99a9d5666420de48b30220ad9b243b02b8ebd15aa30d0be3693a3c26633251b073becad9a1dd9e4e41293b87a7f70569e65ee5800354c9343db36c3c03c",
    "Hm_lvt_1c442ef4c90c7fc502a739de0fc642e0": "1750164816",
    "HMACCOUNT": "A36D408D98116C95",
    "Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5": "1750164817",
    "JSESSIONIDGS8": "j0Z9-ncRCuhCSHr73-fhAesout2i9ifHp3feQd6PiOd_OM5n9PQK\\u0021-64666437",
    "CSH_DF": "5vr4GVey0x8EiYz9VGuYabghWrKnMu9LuPvb+nidNvbuu8385mOfzXz6Z2HMd6C6hd",
    "CSH_UF": "8cf04e281318af421dc03fc482e00bfd",
    "Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5": "1750166138",
    "Hm_lpvt_1c442ef4c90c7fc502a739de0fc642e0": "1750166138"
})

# First request to get the code
url = "http://htgs.ccgp.gov.cn/GS8/genCodeImg"
params = {"t": "0.6617852839310656"}
response = session.get(url, params=params, verify=False)
coderes = response.json()['msg']

print(coderes)

# Update headers for the second request (adding Content-Type)
session.headers.update({
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://htgs.ccgp.gov.cn"
})


# Second request
url = "http://htgs.ccgp.gov.cn/GS8/contractpublish/getContractByAjax"
params = {"contractSign": "0"}
data = {
    "searchContractCode": "",
    "searchContractName": "",
    "searchProjCode": "",
    "searchProjName": "",
    "searchPurchaserName": "中国救援浙江机动专业支队",
    "searchSupplyName": "",
    "searchAgentName": "",
    "searchPlacardStartDate": "",
    "searchPlacardEndDate": "",
    "code": "pageNoChange",
    "isChange": "",
    "currentPage": "9",
    "codeResult": f"{coderes}"
}
response = session.post(url, params=params, data=data)

print(response.text)
# Save the response
with open('4.json', 'w', encoding='utf-8') as f:
    json.dump(response.text, f, ensure_ascii=False, indent=4)