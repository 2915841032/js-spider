- [ ] 此网站的解密就是一个AES,RPC就是在网页中的解密位置。增加一个远程连接，可以用来远程解密。或者加密等操作，通常用于爬虫加密无法解决的情况下才使用。因为这个有一个弊端。网页注入不能关，所以实在解不出来了，需要数据,很急的时候才用。

```
        function b(t) {
            var e = d.a.enc.Hex.parse(t)
              , n = d.a.enc.Base64.stringify(e)
              , a = d.a.AES.decrypt(n, f, {
                iv: m,
                mode: d.a.mode.CBC,
                padding: d.a.pad.Pkcs7
            })
              , r = a.toString(d.a.enc.Utf8);
            return r.toString()
        }
```

