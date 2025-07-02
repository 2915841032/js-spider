import requests


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.mafengwo.cn/wenda/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "PHPSESSID": "49ntm68ettj1jdkpff5p2plvr1",
    "mfw_uuid": "684bb83f-e133-557a-1c3c-876798f3843f",
    "oad_n": "a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222025-06-13+13%3A33%3A51%22%3B%7D",
    "__mfwc": "direct",
    "__mfwa": "1749792833065.95242.1.1749792833065.1749792833065",
    "__mfwlv": "1749792833",
    "__mfwvn": "1",
    "uva": "s%3A106%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1749792833%3Bs%3A10%3A%22last_refer%22%3Bs%3A38%3A%22https%3A%2F%2Fwww.mafengwo.cn%2Fi%2F5376978.html%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B",
    "__mfwurd": "a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1749792833%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D",
    "__mfwuuid": "684bb83f-e133-557a-1c3c-876798f3843f",
    "bottom_ad_status": "0",
    "__omc_chl": "",
    "__omc_r": "",
    "__mfwb": "a443513dc1a3.9.direct",
    "__mfwlt": "1749793768",
    "ariaDefaultTheme": "undefined",
    "w_tsfp": "ltvuV0MF2utBvS0Q7aPunUinFzEmcD44h0wpEaR0f5thQLErU5mB2IFzvcL2OXbc48xnvd7DsZoyJTLYCJI3dwMRR8zHd4hDigiYwdcg1YdGUxlmGc/fDVYYcO0h6DkTfnhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5Wnb5Q35KFpyUOgQhkaRhiwfWnAj4RKyIuEPZ0iuJs6pSqA="
}
url = "https://www.mafengwo.cn/qa/ajax_qa/more"
params = {
    "qa_page": "index",
    "type": "0",
    "mddid": "",
    "tid": "",
    "key": "",
    "page": "2",
    "time": ""
}
response = requests.get(url, headers=headers,params=params)

print(response.text)
print(response)