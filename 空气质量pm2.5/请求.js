const CryptoJS = require('crypto-js')

const  askiZExYII01 = "aPnyDR5Ca6FMIfdw";//AESkey，可自定义
const  asideGdRY692 = "bNpeyqJl34VlZ7ng";//密钥偏移量IV，可自定义

const  ackK9cbiA0YB = "dX1N15fjv5KdeCyi";//AESkey，可自定义
const  acimrLO29gRI = "f3v35CzxuYjqwizp";//密钥偏移量IV，可自定义

const  dsk9EbiUpi5W = "hIFclTxH0JalYZiu";//DESkey，可自定义
const  dsi3gJ2aZe1f = "xMFHANC8X1TunaGs";//密钥偏移量IV，可自定义

const  dckE15Yk15AF = "oHLKvpN54hwpLWjt";//DESkey，可自定义
const  dcik4kPiOWjo = "pdgLk9FGBd5kXbm0";//密钥偏移量IV，可自定义

const aes_local_key = 'emhlbnFpcGFsbWtleQ==';
const aes_local_iv = 'emhlbnFpcGFsbWl2';
function ObjectSort(obj){
    var newObject = {};
    Object.keys(obj).sort().map(function(key){
        newObject[key] = obj[key];
    });
    return newObject;
}
var BASE64 = {
    encrypt: function(text) {
        var b = new Base64();
        return b.encode(text);
    },
    decrypt: function(text) {
        var b = new Base64();
        return b.decode(text);
    }
};

var DES = {
 encrypt: function(text, key, iv){
    var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.DES.encrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString();
 },
 decrypt: function(text, key, iv){
    var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.DES.decrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8);
  }
};

var AES = {
  encrypt: function(text, key, iv) {
    var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
    // console.log('real key:', secretkey);
    // console.log('real iv:', secretiv);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.AES.encrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString();
  },
  decrypt: function(text, key, iv) {
    var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.AES.decrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8);
  }
};
function Base64() {
    _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
    this.encode = function(a) {
        var c, d, e, f, g, h, i, b = "", j = 0;
        for (a = _utf8_encode(a); j < a.length; )
            c = a.charCodeAt(j++),
            d = a.charCodeAt(j++),
            e = a.charCodeAt(j++),
            f = c >> 2,
            g = (3 & c) << 4 | d >> 4,
            h = (15 & d) << 2 | e >> 6,
            i = 63 & e,
            isNaN(d) ? h = i = 64 : isNaN(e) && (i = 64),
            b = b + _keyStr.charAt(f) + _keyStr.charAt(g) + _keyStr.charAt(h) + _keyStr.charAt(i);
        return b
    }
    ,
    this.decode = function(a) {
        var c, d, e, f, g, h, i, b = "", j = 0;
        for (a = a.replace(/[^A-Za-z0-9\+\/\=]/g, ""); j < a.length; )
            f = _keyStr.indexOf(a.charAt(j++)),
            g = _keyStr.indexOf(a.charAt(j++)),
            h = _keyStr.indexOf(a.charAt(j++)),
            i = _keyStr.indexOf(a.charAt(j++)),
            c = f << 2 | g >> 4,
            d = (15 & g) << 4 | h >> 2,
            e = (3 & h) << 6 | i,
            b += String.fromCharCode(c),
            64 != h && (b += String.fromCharCode(d)),
            64 != i && (b += String.fromCharCode(e));
        return b = _utf8_decode(b)
    }
    ,
    _utf8_encode = function(a) {
        var b, c, d;
        for (a = a.replace(/\r\n/g, "\n"),
        b = "",
        c = 0; c < a.length; c++)
            d = a.charCodeAt(c),
            128 > d ? b += String.fromCharCode(d) : d > 127 && 2048 > d ? (b += String.fromCharCode(192 | d >> 6),
            b += String.fromCharCode(128 | 63 & d)) : (b += String.fromCharCode(224 | d >> 12),
            b += String.fromCharCode(128 | 63 & d >> 6),
            b += String.fromCharCode(128 | 63 & d));
        return b
    }
    ,
    _utf8_decode = function(a) {
        for (var b = "", c = 0, d = c1 = c2 = 0; c < a.length; )
            d = a.charCodeAt(c),
            128 > d ? (b += String.fromCharCode(d),
            c++) : d > 191 && 224 > d ? (c2 = a.charCodeAt(c + 1),
            b += String.fromCharCode((31 & d) << 6 | 63 & c2),
            c += 2) : (c2 = a.charCodeAt(c + 1),
            c3 = a.charCodeAt(c + 2),
            b += String.fromCharCode((15 & d) << 12 | (63 & c2) << 6 | 63 & c3),
            c += 3);
        return b
    }
}
function hex_md5(a) {
    return binl2hex(core_md5(str2binl(a), a.length * chrsz))
}
function b64_md5(a) {
    return binl2b64(core_md5(str2binl(a), a.length * chrsz))
}
function str_md5(a) {
    return binl2str(core_md5(str2binl(a), a.length * chrsz))
}
function hex_hmac_md5(a, b) {
    return binl2hex(core_hmac_md5(a, b))
}
function b64_hmac_md5(a, b) {
    return binl2b64(core_hmac_md5(a, b))
}
function str_hmac_md5(a, b) {
    return binl2str(core_hmac_md5(a, b))
}
function md5_vm_test() {
    return "900150983cd24fb0d6963f7d28e17f72" == hex_md5("abc")
}
function core_md5(a, b) {
    var c, d, e, f, g, h, i, j, k;
    for (a[b >> 5] |= 128 << b % 32,
    a[(b + 64 >>> 9 << 4) + 14] = b,
    c = 1732584193,
    d = -271733879,
    e = -1732584194,
    f = 271733878,
    g = 0; g < a.length; g += 16)
        h = c,
        i = d,
        j = e,
        k = f,
        c = md5_ff(c, d, e, f, a[g + 0], 7, -680876936),
        f = md5_ff(f, c, d, e, a[g + 1], 12, -389564586),
        e = md5_ff(e, f, c, d, a[g + 2], 17, 606105819),
        d = md5_ff(d, e, f, c, a[g + 3], 22, -1044525330),
        c = md5_ff(c, d, e, f, a[g + 4], 7, -176418897),
        f = md5_ff(f, c, d, e, a[g + 5], 12, 1200080426),
        e = md5_ff(e, f, c, d, a[g + 6], 17, -1473231341),
        d = md5_ff(d, e, f, c, a[g + 7], 22, -45705983),
        c = md5_ff(c, d, e, f, a[g + 8], 7, 1770035416),
        f = md5_ff(f, c, d, e, a[g + 9], 12, -1958414417),
        e = md5_ff(e, f, c, d, a[g + 10], 17, -42063),
        d = md5_ff(d, e, f, c, a[g + 11], 22, -1990404162),
        c = md5_ff(c, d, e, f, a[g + 12], 7, 1804603682),
        f = md5_ff(f, c, d, e, a[g + 13], 12, -40341101),
        e = md5_ff(e, f, c, d, a[g + 14], 17, -1502002290),
        d = md5_ff(d, e, f, c, a[g + 15], 22, 1236535329),
        c = md5_gg(c, d, e, f, a[g + 1], 5, -165796510),
        f = md5_gg(f, c, d, e, a[g + 6], 9, -1069501632),
        e = md5_gg(e, f, c, d, a[g + 11], 14, 643717713),
        d = md5_gg(d, e, f, c, a[g + 0], 20, -373897302),
        c = md5_gg(c, d, e, f, a[g + 5], 5, -701558691),
        f = md5_gg(f, c, d, e, a[g + 10], 9, 38016083),
        e = md5_gg(e, f, c, d, a[g + 15], 14, -660478335),
        d = md5_gg(d, e, f, c, a[g + 4], 20, -405537848),
        c = md5_gg(c, d, e, f, a[g + 9], 5, 568446438),
        f = md5_gg(f, c, d, e, a[g + 14], 9, -1019803690),
        e = md5_gg(e, f, c, d, a[g + 3], 14, -187363961),
        d = md5_gg(d, e, f, c, a[g + 8], 20, 1163531501),
        c = md5_gg(c, d, e, f, a[g + 13], 5, -1444681467),
        f = md5_gg(f, c, d, e, a[g + 2], 9, -51403784),
        e = md5_gg(e, f, c, d, a[g + 7], 14, 1735328473),
        d = md5_gg(d, e, f, c, a[g + 12], 20, -1926607734),
        c = md5_hh(c, d, e, f, a[g + 5], 4, -378558),
        f = md5_hh(f, c, d, e, a[g + 8], 11, -2022574463),
        e = md5_hh(e, f, c, d, a[g + 11], 16, 1839030562),
        d = md5_hh(d, e, f, c, a[g + 14], 23, -35309556),
        c = md5_hh(c, d, e, f, a[g + 1], 4, -1530992060),
        f = md5_hh(f, c, d, e, a[g + 4], 11, 1272893353),
        e = md5_hh(e, f, c, d, a[g + 7], 16, -155497632),
        d = md5_hh(d, e, f, c, a[g + 10], 23, -1094730640),
        c = md5_hh(c, d, e, f, a[g + 13], 4, 681279174),
        f = md5_hh(f, c, d, e, a[g + 0], 11, -358537222),
        e = md5_hh(e, f, c, d, a[g + 3], 16, -722521979),
        d = md5_hh(d, e, f, c, a[g + 6], 23, 76029189),
        c = md5_hh(c, d, e, f, a[g + 9], 4, -640364487),
        f = md5_hh(f, c, d, e, a[g + 12], 11, -421815835),
        e = md5_hh(e, f, c, d, a[g + 15], 16, 530742520),
        d = md5_hh(d, e, f, c, a[g + 2], 23, -995338651),
        c = md5_ii(c, d, e, f, a[g + 0], 6, -198630844),
        f = md5_ii(f, c, d, e, a[g + 7], 10, 1126891415),
        e = md5_ii(e, f, c, d, a[g + 14], 15, -1416354905),
        d = md5_ii(d, e, f, c, a[g + 5], 21, -57434055),
        c = md5_ii(c, d, e, f, a[g + 12], 6, 1700485571),
        f = md5_ii(f, c, d, e, a[g + 3], 10, -1894986606),
        e = md5_ii(e, f, c, d, a[g + 10], 15, -1051523),
        d = md5_ii(d, e, f, c, a[g + 1], 21, -2054922799),
        c = md5_ii(c, d, e, f, a[g + 8], 6, 1873313359),
        f = md5_ii(f, c, d, e, a[g + 15], 10, -30611744),
        e = md5_ii(e, f, c, d, a[g + 6], 15, -1560198380),
        d = md5_ii(d, e, f, c, a[g + 13], 21, 1309151649),
        c = md5_ii(c, d, e, f, a[g + 4], 6, -145523070),
        f = md5_ii(f, c, d, e, a[g + 11], 10, -1120210379),
        e = md5_ii(e, f, c, d, a[g + 2], 15, 718787259),
        d = md5_ii(d, e, f, c, a[g + 9], 21, -343485551),
        c = safe_add(c, h),
        d = safe_add(d, i),
        e = safe_add(e, j),
        f = safe_add(f, k);
    return Array(c, d, e, f)
}
function md5_cmn(a, b, c, d, e, f) {
    return safe_add(bit_rol(safe_add(safe_add(b, a), safe_add(d, f)), e), c)
}
function md5_ff(a, b, c, d, e, f, g) {
    return md5_cmn(b & c | ~b & d, a, b, e, f, g)
}
function md5_gg(a, b, c, d, e, f, g) {
    return md5_cmn(b & d | c & ~d, a, b, e, f, g)
}
function md5_hh(a, b, c, d, e, f, g) {
    return md5_cmn(b ^ c ^ d, a, b, e, f, g)
}
function md5_ii(a, b, c, d, e, f, g) {
    return md5_cmn(c ^ (b | ~d), a, b, e, f, g)
}
function core_hmac_md5(a, b) {
    var d, e, f, g, c = str2binl(a);
    for (c.length > 16 && (c = core_md5(c, a.length * chrsz)),
    d = Array(16),
    e = Array(16),
    f = 0; 16 > f; f++)
        d[f] = 909522486 ^ c[f],
        e[f] = 1549556828 ^ c[f];
    return g = core_md5(d.concat(str2binl(b)), 512 + b.length * chrsz),
    core_md5(e.concat(g), 640)
}
function safe_add(a, b) {
    var c = (65535 & a) + (65535 & b)
      , d = (a >> 16) + (b >> 16) + (c >> 16);
    return d << 16 | 65535 & c
}
function bit_rol(a, b) {
    return a << b | a >>> 32 - b
}
function str2binl(a) {
    var d, b = Array(), c = (1 << chrsz) - 1;
    for (d = 0; d < a.length * chrsz; d += chrsz)
        b[d >> 5] |= (a.charCodeAt(d / chrsz) & c) << d % 32;
    return b
}
function binl2str(a) {
    var d, b = "", c = (1 << chrsz) - 1;
    for (d = 0; d < 32 * a.length; d += chrsz)
        b += String.fromCharCode(a[d >> 5] >>> d % 32 & c);
    return b
}
function binl2hex(a) {
    var d, b = hexcase ? "0123456789ABCDEF" : "0123456789abcdef", c = "";
    for (d = 0; d < 4 * a.length; d++)
        c += b.charAt(15 & a[d >> 2] >> 8 * (d % 4) + 4) + b.charAt(15 & a[d >> 2] >> 8 * (d % 4));
    return c
}
function binl2b64(a) {
    var d, e, f, b = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", c = "";
    for (d = 0; d < 4 * a.length; d += 3)
        for (e = (255 & a[d >> 2] >> 8 * (d % 4)) << 16 | (255 & a[d + 1 >> 2] >> 8 * ((d + 1) % 4)) << 8 | 255 & a[d + 2 >> 2] >> 8 * ((d + 2) % 4),
        f = 0; 4 > f; f++)
            c += 8 * d + 6 * f > 32 * a.length ? b64pad : b.charAt(63 & e >> 6 * (3 - f));
    return c
}
function encode_param(a) {
    var b = new Base64;
    return b.encode(a)
}
function encode_secret() {
    var b, a = appId;
    for (b = 0; b < arguments.length; b++)
        a += arguments[b];
    return a = a.replace(/\s/g, ""),
    hex_md5(a)
}
function decode_result(a) {
    var b = new Base64;
    return b.decode(b.decode(b.decode(a)))
}
var hexcase = 0
  , b64pad = ""
  , chrsz = 8
  , appId = "b73a4aaa989f54997ef7b9c42b6b4b29";
var hexcase = 0;
var b64pad = "";
function hex_md5(s) {
    return rstr2hex(rstr_md5(str2rstr_utf8(s)))
}
function b64_md5(s) {
    return rstr2b64(rstr_md5(str2rstr_utf8(s)))
}
function any_md5(s, e) {
    return rstr2any(rstr_md5(str2rstr_utf8(s)), e)
}
function hex_hmac_md5(k, d) {
    return rstr2hex(rstr_hmac_md5(str2rstr_utf8(k), str2rstr_utf8(d)))
}
function b64_hmac_md5(k, d) {
    return rstr2b64(rstr_hmac_md5(str2rstr_utf8(k), str2rstr_utf8(d)))
}
function any_hmac_md5(k, d, e) {
    return rstr2any(rstr_hmac_md5(str2rstr_utf8(k), str2rstr_utf8(d)), e)
}
function md5_vm_test() {
    return hex_md5("abc").toLowerCase() == "900150983cd24fb0d6963f7d28e17f72"
}
function rstr_md5(s) {
    return binl2rstr(binl_md5(rstr2binl(s), s.length * 8))
}
function rstr_hmac_md5(key, data) {
    var bkey = rstr2binl(key);
    if (bkey.length > 16)
        bkey = binl_md5(bkey, key.length * 8);
    var ipad = Array(16)
      , opad = Array(16);
    for (var i = 0; i < 16; i++) {
        ipad[i] = bkey[i] ^ 0x36363636;
        opad[i] = bkey[i] ^ 0x5C5C5C5C
    }
    var hash = binl_md5(ipad.concat(rstr2binl(data)), 512 + data.length * 8);
    return binl2rstr(binl_md5(opad.concat(hash), 512 + 128))
}
function rstr2hex(input) {
    try {
        hexcase
    } catch (e) {
        hexcase = 0
    }
    var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
    var output = "";
    var x;
    for (var i = 0; i < input.length; i++) {
        x = input.charCodeAt(i);
        output += hex_tab.charAt((x >>> 4) & 0x0F) + hex_tab.charAt(x & 0x0F)
    }
    return output
}
function rstr2b64(input) {
    try {
        b64pad
    } catch (e) {
        b64pad = ''
    }
    var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var output = "";
    var len = input.length;
    for (var i = 0; i < len; i += 3) {
        var triplet = (input.charCodeAt(i) << 16) | (i + 1 < len ? input.charCodeAt(i + 1) << 8 : 0) | (i + 2 < len ? input.charCodeAt(i + 2) : 0);
        for (var j = 0; j < 4; j++) {
            if (i * 8 + j * 6 > input.length * 8)
                output += b64pad;
            else
                output += tab.charAt((triplet >>> 6 * (3 - j)) & 0x3F)
        }
    }
    return output
}
function rstr2any(input, encoding) {
    var divisor = encoding.length;
    var i, j, q, x, quotient;
    var dividend = Array(Math.ceil(input.length / 2));
    for (i = 0; i < dividend.length; i++) {
        dividend[i] = (input.charCodeAt(i * 2) << 8) | input.charCodeAt(i * 2 + 1)
    }
    var full_length = Math.ceil(input.length * 8 / (Math.log(encoding.length) / Math.log(2)));
    var remainders = Array(full_length);
    for (j = 0; j < full_length; j++) {
        quotient = Array();
        x = 0;
        for (i = 0; i < dividend.length; i++) {
            x = (x << 16) + dividend[i];
            q = Math.floor(x / divisor);
            x -= q * divisor;
            if (quotient.length > 0 || q > 0)
                quotient[quotient.length] = q
        }
        remainders[j] = x;
        dividend = quotient
    }
    var output = "";
    for (i = remainders.length - 1; i >= 0; i--)
        output += encoding.charAt(remainders[i]);
    return output
}
function str2rstr_utf8(input) {
    var output = "";
    var i = -1;
    var x, y;
    while (++i < input.length) {
        x = input.charCodeAt(i);
        y = i + 1 < input.length ? input.charCodeAt(i + 1) : 0;
        if (0xD800 <= x && x <= 0xDBFF && 0xDC00 <= y && y <= 0xDFFF) {
            x = 0x10000 + ((x & 0x03FF) << 10) + (y & 0x03FF);
            i++
        }
        if (x <= 0x7F)
            output += String.fromCharCode(x);
        else if (x <= 0x7FF)
            output += String.fromCharCode(0xC0 | ((x >>> 6) & 0x1F), 0x80 | (x & 0x3F));
        else if (x <= 0xFFFF)
            output += String.fromCharCode(0xE0 | ((x >>> 12) & 0x0F), 0x80 | ((x >>> 6) & 0x3F), 0x80 | (x & 0x3F));
        else if (x <= 0x1FFFFF)
            output += String.fromCharCode(0xF0 | ((x >>> 18) & 0x07), 0x80 | ((x >>> 12) & 0x3F), 0x80 | ((x >>> 6) & 0x3F), 0x80 | (x & 0x3F))
    }
    return output
}
function str2rstr_utf16le(input) {
    var output = "";
    for (var i = 0; i < input.length; i++)
        output += String.fromCharCode(input.charCodeAt(i) & 0xFF, (input.charCodeAt(i) >>> 8) & 0xFF);
    return output
}
function str2rstr_utf16be(input) {
    var output = "";
    for (var i = 0; i < input.length; i++)
        output += String.fromCharCode((input.charCodeAt(i) >>> 8) & 0xFF, input.charCodeAt(i) & 0xFF);
    return output
}
function rstr2binl(input) {
    var output = Array(input.length >> 2);
    for (var i = 0; i < output.length; i++)
        output[i] = 0;
    for (var i = 0; i < input.length * 8; i += 8)
        output[i >> 5] |= (input.charCodeAt(i / 8) & 0xFF) << (i % 32);
    return output
}
function binl2rstr(input) {
    var output = "";
    for (var i = 0; i < input.length * 32; i += 8)
        output += String.fromCharCode((input[i >> 5] >>> (i % 32)) & 0xFF);
    return output
}
function binl_md5(x, len) {
    x[len >> 5] |= 0x80 << ((len) % 32);
    x[(((len + 64) >>> 9) << 4) + 14] = len;
    var a = 1732584193;
    var b = -271733879;
    var c = -1732584194;
    var d = 271733878;
    for (var i = 0; i < x.length; i += 16) {
        var olda = a;
        var oldb = b;
        var oldc = c;
        var oldd = d;
        a = md5_ff(a, b, c, d, x[i + 0], 7, -680876936);
        d = md5_ff(d, a, b, c, x[i + 1], 12, -389564586);
        c = md5_ff(c, d, a, b, x[i + 2], 17, 606105819);
        b = md5_ff(b, c, d, a, x[i + 3], 22, -1044525330);
        a = md5_ff(a, b, c, d, x[i + 4], 7, -176418897);
        d = md5_ff(d, a, b, c, x[i + 5], 12, 1200080426);
        c = md5_ff(c, d, a, b, x[i + 6], 17, -1473231341);
        b = md5_ff(b, c, d, a, x[i + 7], 22, -45705983);
        a = md5_ff(a, b, c, d, x[i + 8], 7, 1770035416);
        d = md5_ff(d, a, b, c, x[i + 9], 12, -1958414417);
        c = md5_ff(c, d, a, b, x[i + 10], 17, -42063);
        b = md5_ff(b, c, d, a, x[i + 11], 22, -1990404162);
        a = md5_ff(a, b, c, d, x[i + 12], 7, 1804603682);
        d = md5_ff(d, a, b, c, x[i + 13], 12, -40341101);
        c = md5_ff(c, d, a, b, x[i + 14], 17, -1502002290);
        b = md5_ff(b, c, d, a, x[i + 15], 22, 1236535329);
        a = md5_gg(a, b, c, d, x[i + 1], 5, -165796510);
        d = md5_gg(d, a, b, c, x[i + 6], 9, -1069501632);
        c = md5_gg(c, d, a, b, x[i + 11], 14, 643717713);
        b = md5_gg(b, c, d, a, x[i + 0], 20, -373897302);
        a = md5_gg(a, b, c, d, x[i + 5], 5, -701558691);
        d = md5_gg(d, a, b, c, x[i + 10], 9, 38016083);
        c = md5_gg(c, d, a, b, x[i + 15], 14, -660478335);
        b = md5_gg(b, c, d, a, x[i + 4], 20, -405537848);
        a = md5_gg(a, b, c, d, x[i + 9], 5, 568446438);
        d = md5_gg(d, a, b, c, x[i + 14], 9, -1019803690);
        c = md5_gg(c, d, a, b, x[i + 3], 14, -187363961);
        b = md5_gg(b, c, d, a, x[i + 8], 20, 1163531501);
        a = md5_gg(a, b, c, d, x[i + 13], 5, -1444681467);
        d = md5_gg(d, a, b, c, x[i + 2], 9, -51403784);
        c = md5_gg(c, d, a, b, x[i + 7], 14, 1735328473);
        b = md5_gg(b, c, d, a, x[i + 12], 20, -1926607734);
        a = md5_hh(a, b, c, d, x[i + 5], 4, -378558);
        d = md5_hh(d, a, b, c, x[i + 8], 11, -2022574463);
        c = md5_hh(c, d, a, b, x[i + 11], 16, 1839030562);
        b = md5_hh(b, c, d, a, x[i + 14], 23, -35309556);
        a = md5_hh(a, b, c, d, x[i + 1], 4, -1530992060);
        d = md5_hh(d, a, b, c, x[i + 4], 11, 1272893353);
        c = md5_hh(c, d, a, b, x[i + 7], 16, -155497632);
        b = md5_hh(b, c, d, a, x[i + 10], 23, -1094730640);
        a = md5_hh(a, b, c, d, x[i + 13], 4, 681279174);
        d = md5_hh(d, a, b, c, x[i + 0], 11, -358537222);
        c = md5_hh(c, d, a, b, x[i + 3], 16, -722521979);
        b = md5_hh(b, c, d, a, x[i + 6], 23, 76029189);
        a = md5_hh(a, b, c, d, x[i + 9], 4, -640364487);
        d = md5_hh(d, a, b, c, x[i + 12], 11, -421815835);
        c = md5_hh(c, d, a, b, x[i + 15], 16, 530742520);
        b = md5_hh(b, c, d, a, x[i + 2], 23, -995338651);
        a = md5_ii(a, b, c, d, x[i + 0], 6, -198630844);
        d = md5_ii(d, a, b, c, x[i + 7], 10, 1126891415);
        c = md5_ii(c, d, a, b, x[i + 14], 15, -1416354905);
        b = md5_ii(b, c, d, a, x[i + 5], 21, -57434055);
        a = md5_ii(a, b, c, d, x[i + 12], 6, 1700485571);
        d = md5_ii(d, a, b, c, x[i + 3], 10, -1894986606);
        c = md5_ii(c, d, a, b, x[i + 10], 15, -1051523);
        b = md5_ii(b, c, d, a, x[i + 1], 21, -2054922799);
        a = md5_ii(a, b, c, d, x[i + 8], 6, 1873313359);
        d = md5_ii(d, a, b, c, x[i + 15], 10, -30611744);
        c = md5_ii(c, d, a, b, x[i + 6], 15, -1560198380);
        b = md5_ii(b, c, d, a, x[i + 13], 21, 1309151649);
        a = md5_ii(a, b, c, d, x[i + 4], 6, -145523070);
        d = md5_ii(d, a, b, c, x[i + 11], 10, -1120210379);
        c = md5_ii(c, d, a, b, x[i + 2], 15, 718787259);
        b = md5_ii(b, c, d, a, x[i + 9], 21, -343485551);
        a = safe_add(a, olda);
        b = safe_add(b, oldb);
        c = safe_add(c, oldc);
        d = safe_add(d, oldd)
    }
    return Array(a, b, c, d)
}
function md5_cmn(q, a, b, x, s, t) {
    return safe_add(bit_rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b)
}
function md5_ff(a, b, c, d, x, s, t) {
    return md5_cmn((b & c) | ((~b) & d), a, b, x, s, t)
}
function md5_gg(a, b, c, d, x, s, t) {
    return md5_cmn((b & d) | (c & (~d)), a, b, x, s, t)
}
function md5_hh(a, b, c, d, x, s, t) {
    return md5_cmn(b ^ c ^ d, a, b, x, s, t)
}
function md5_ii(a, b, c, d, x, s, t) {
    return md5_cmn(c ^ (b | (~d)), a, b, x, s, t)
}
function safe_add(x, y) {
    var lsw = (x & 0xFFFF) + (y & 0xFFFF);
    var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
    return (msw << 16) | (lsw & 0xFFFF)
}
function bit_rol(num, cnt) {
    return (num << cnt) | (num >>> (32 - cnt))
}
function lk(method, obj){
    var appId = '271c2aab7dd615dacbadcb41d3c77fa4';
    var clienttype = 'WEB';
    var timestamp = new Date().getTime();
    // console.log(method, obj,ObjectSort(obj),appId + method + timestamp + 'WEIXIN' + JSON.stringify(ObjectSort(obj)));
    var param = {
      appId: appId,
      method: method,
      timestamp: timestamp,
      clienttype: clienttype,
      object: obj,
      secret: hex_md5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj)))
    };
    param = BASE64.encrypt(JSON.stringify(param));
    param = DES.encrypt(param, dckE15Yk15AF, dcik4kPiOWjo);
    return param;
};

console.log(lk("GETDATA",{'city': "北京"}))