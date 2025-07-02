import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.zhipin.com/gongsi/job/ab9fdc6f043679990HY~.html",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "traceid": "F-fb8ae79sSRT3ZBKl",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    # "ab_guid": "24a4ebc3-1ab8-4d1f-a9e6-d24deb810980",
    # "__zp_seo_uuid__": "9b017bc5-f66a-495d-9462-f929ca113035",
    # "__l": "r=https%3A%2F%2Fspidertools.cn%2F&l=%2Fgongsi%2Fab9fdc6f043679990HY%7E.html&s=1",
    # "__zp_stoken__": "0df7fSzfDsMORwqvCuFI7GwYbIBs6KjQ3JMKOTUs7TE5OSzc6TExLN1IuOjvDm8K6GcO5dXDDhTY1Jjc6OTVLUTpOUBY3TsWQwro6NkHDucK1LMSLdFnDilnClMK1HUQ0UgloBlVNKMKwwrQ0OE1Rw4fCusKLw47Ds8K0d8ODw6fDj3nDjzg1UTo%2BNCIJBgQ0NWJbWQpHVkpjcFMTU11hJ1FROjfClcSCw7pANR4KIR8THAgTHSEbHwQfEyEFHiAcCh4FGwdCTsKWwrTDm0XGgMODw57EosOFwr7CnMKKxIFIw7vCocSBwqfDlsKfw6dbwqDCmsKjwpTDp8KVwqLCucOqwrzCmsKpwqFIxJHCucKsYsKFfMKwwqTCpWVHb8KnwrfCtMODXnDCmnBzwrhqaWBJwqZswrYTwpF8f1djXsKOIFVwCjTCkUjCqMOK"
}
url = "https://www.zhipin.com/wapi/zpgeek/brand/job/querylist.json"
params = {
    "brandId": "ab9fdc6f043679990HY~",
    "page": "3",
    "pageSize": "50",
    "positionLv1": "",
    "city": "",
    "degree": "",
    "experience": "",
    "salary": "",
    "query": ""
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)