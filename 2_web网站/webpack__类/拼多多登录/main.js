T = {
    "passwordEncrypt": true,
    "publicKey": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC6zHXNom934tsG9SC73vAUv99bIuSRVaLsuTMY+OL6aS6eB7AuNoU+m9gPCrI7aFrT7CSiKTJ47DNwCNZO52AlLzvB6TjdUwuIXWpinE8VCsYAZgOCrx+mK9Sy0OuwnqNj5D2wUdGoN0nxbl1q2akeAa18A/iBpiXx0SZQexbEowIDAQAB"
}

var e = '123456'
i = {}
i.a = function e(e) {
    e = e || {},
        this.default_key_size = parseInt(e.default_key_size, 10) || 1024,
        this.default_public_exponent = e.default_public_exponent || "010001",
        this.log = e.log || !1,
        this.key = null
}

cencrypt = function (e) {
    var t = function (e, t) {
        if (t < e.length + 11)
            return console.error("Message too long for RSA"),
                null;
        for (var n = [], r = e.length - 1; r >= 0 && t > 0;) {
            var o = e.charCodeAt(r--);
            o < 128 ? n[--t] = o : o > 127 && o < 2048 ? (n[--t] = 63 & o | 128,
                n[--t] = o >> 6 | 192) : (n[--t] = 63 & o | 128,
                n[--t] = o >> 6 & 63 | 128,
                n[--t] = o >> 12 | 224)
        }
        n[--t] = 0;
        for (var i = new K, a = []; t > 2;) {
            for (a[0] = 0; 0 == a[0];)
                i.nextBytes(a);
            n[--t] = a[0]
        }
        return n[--t] = 2,
            n[--t] = 0,
            new O(n)
    }(e, this.n.bitLength() + 7 >> 3);
    if (null == t)
        return null;
    var n = this.doPublic(t);
    if (null == n)
        return null;
    var r = n.toString(16);
    return 0 == (1 & r.length) ? r : "0" + r
}

function l(e) {
    var t, n, r = "";
    for (t = 0; t + 3 <= e.length; t += 3)
        n = parseInt(e.substring(t, t + 3), 16),
            r += c.charAt(n >> 6) + c.charAt(63 & n);
    for (t + 1 == e.length ? (n = parseInt(e.substring(t, t + 1), 16),
        r += c.charAt(n << 2)) : t + 2 == e.length && (n = parseInt(e.substring(t, t + 2), 16),
        r += c.charAt(n >> 2) + c.charAt((3 & n) << 4)); (3 & r.length) > 0;)
        r += "=";
    return r
}

i.encrypt = function (e) {
    try {
        return l(cencrypt(e))
    } catch (t) {
        return !1
    }
}
i.setPublicKey = function(e) {
                this.setKey(e)
            }
// function I(e, t) {
//     var n = new i.a;
//     return n.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC6zHXNom934tsG9SC73vAUv99bIuSRVaLsuTMY+OL6aS6eB7AuNoU+m9gPCrI7aFrT7CSiKTJ47DNwCNZO52AlLzvB6TjdUwuIXWpinE8VCsYAZgOCrx+mK9Sy0OuwnqNj5D2wUdGoN0nxbl1q2akeAa18A/iBpiXx0SZQexbEowIDAQAB"),  n.encrypt(e)
//
// }
//
// console.log(I("username=18229425733&password=123456&ts=1748084108613", T))