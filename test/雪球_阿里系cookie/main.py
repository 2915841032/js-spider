import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "acw_tc": "1a0c640a17497199784654990e005b95e782bed354817a663a21de3e2d8ee2",
    "xq_a_token": "1761314ec4bc6cbe0dec68e68a1d6903623a1853",
    # "xqat": "1761314ec4bc6cbe0dec68e68a1d6903623a1853",
    # "xq_r_token": "113ff6c9d2f7990e25c1079246420fdf17bcc4f7",
    # "xq_id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc1MTI0NTg0MywiY3RtIjoxNzQ5NzE5OTU0NjA0LCJjaWQiOiJkOWQwbjRBWnVwIn0.QeppRdqcgSwl1gFvI66g0ZBXL0X2SXMw57nV-Ymb65YsQZPpO4y1QdSpMeU46-9u3osGvdoSLczvclZuDHIfONVPTfTt3K2KQNxNN7fqQqSYFinAf44RDJNm4MSyv7BeBl13_POG3KbLz7e2dA7AnDiG8YMvo4LggXOhAovdcKIx38s3xK3wDtF-5kuSCkUhm_CORQmnMdWfJBbL5C06QaYMg8y4OyBUpMHuqaTkQ-hDyoOvBp-z9QjUAKzMomu5l6ZZ8aoRiIGhbotghZvsiEDEYKiytfTj6GUeD0lnmR-yyftvFi-Mnw7AfBpB9USYUYeulJ0Cf9o-tY4rKo9cAg",
    # "cookiesu": "481749719978472",
    # "u": "481749719978472",
    # "device_id": "eb373c5ace5685ff8a448bc0802627db",
    # ".thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7": "tJAji3cSgv5TDsZ2/IWMEPuC8qUuofzXsK+DTODFJebJ2vnB6elriXtld/9ADu9UtMU8FZdU1ONtb5hJ4k3e1w%3D%3D",
    # "ssxmod_itna": "iqROD5BK0KAIjx4qeqhxmxYKGQO3qBP01DppxQyK08D6CxB40QX=kGToPoHD00Nn7rjey01qDsT8D4GzDiwPGhDBeYFYB1kr4z=WtogpeeICd9Gd5hnYlp7fsCmHRuGvCzDC+pxCPGnD067UDmqDxGGI4GwDGoD34DiDDPDb4iDAweD7qDFGnRQcWbDm4GWGeGfDDoDY4bPxiUYDDtvlqG2tObzDDNslhDDe8GotpaVGpmkXQKFv74Yx0UTDBLKAI5Yv6SLg2TFk/gbNbrDzLCDtTTb/e0ksObiyjWiUYNMxoLdQm6MIBDq0w7jGxCq4iGxUpqjD4D+7ew3Ch5lN4aI3INiDDAUxN3u40Y2/AgbyS8yM3n=t0rWib8OFl4NBbQvG/3qtnrNI0DF0xCqY80xoBt8Dhn5xeD",
    # "ssxmod_itna2": "iqROD5BK0KAIjx4qeqhxmxYKGQO3qBP01DppxQyK08D6CxB40QX=kGToPoHD00Nn7rjey0x4DWyDUGDAeTBx7pdo/P1Rhd=IDGNFT+/=Sh7CvedlpA23ydCwcdBKqlHnn=TYle02K01G0ULQn7OiUWupc80jevi67UGL5eeb4qlLDZwdEDwoXFB3Yg2dcb76VWWuR7gWYTZnMba=E+hDXiTfx7=HWZ4jtZOtZU0GLBMGswbfqUZdE8=fxmniB/4t9l+QxL=coFDuKt7=Fv7GTOOGiynUi=Clj=lMnzbSzSSrLXDReBRhZfPwznRFu6Ac8YPsKq4uu27YkUbjb9PDw45RmI4qvDC0KEUiAFHHATW+PE+n4wxEQWxIRKruD0rVbgE80fRwzGb6SRn+4pboHKvk/o7SYUI414cKghCCrqYIz+HQ9Rz+rAAR4G4+99/FTV9rNc7Pc7KsWVGRaG3/Du5Hq/F5mb9B02+0BPjPqaw1h5Em4PEB78IRC3g3aW/yNudmS+Wm4xbKnfYFBexc4T=5DxQU0nOlPmkLHnqd0Iy3WoZ4S33d4=9S+14TYcIGURxWovwFaVpFI4l8=tRdWN0OmTOyqCvwvVOAmRv9CCIT87AcST4LuA8Ah/lYTvu5+jd9CCyn=qIjt89vBU4Nfgm+PWOm1XbrLTPPvO9wI7eI9LZLaQUxxBhqAxDhW8QfvNbfiLDmrKoP76e4BD3Kt1g4K5404Wq7bZ3qP88jiQmmQd3QizmZoiKGp+9Qq078Y2Zg4YruxeDxzGK6r3SKRxQm5QvPYdlX8jKZXdGKPD"
}
url = "https://xueqiu.com/statuses/hot/listV2.json"
params = {
    "since_id": "-1",
    "max_id": "784273",
    "size": "15",
    "md5__1038": "2840ce7d37-jsB0IuD0Yundu6iVsiesdzidiwuLb3fX2t5cNuVyuXK=Qud_JOj8sjdJy8uqvSiBKu8ur4uTuj41duFKSXuSUi7uRFbiMuzsuHqrhVtuVhuX7KaBX5RWuUU3uouu4i1qUTarU0aZiriUX88uyZxmhUjdap4yiZKgSRl7ipUyiimXrp2mrUzzu"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)