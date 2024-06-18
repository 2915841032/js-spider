// -*- coding: utf-8 -*-
const CryptoJS = require('crypto-js')

const  ask4u6FbhGV8 = "a0QHmC1Ova5958nC";//AESkey，可自定义
const  asi2hhkBUJbo = "bMu71lHRX6bRmPxU";//密钥偏移量IV，可自定义

const  acky6QolJSJi = "dLRSzDrm8xkryEyL";//AESkey，可自定义
const  acixHVhiNqmK = "fex6AA4zRfVrSPmr";//密钥偏移量IV，可自定义

const  dskQCqpdBOGo = "hEaIOlrX7tlhAOkz";//DESkey，可自定义
const  dsiqYiQHbZQp = "xMBwDXG1HOubUV04";//密钥偏移量IV，可自定义

const  dckCheMkUojW = "oi4aKMxMECWSyTaz";//DESkey，可自定义
const  dciEekKS6Cws = "p2uRrSFcN9oKLrKY";//密钥偏移量IV，可自定义

const aes_local_key = 'emhlbnFpcGFsbWtleQ==';
const aes_local_iv = 'emhlbnFpcGFsbWl2';

function osZ34YC04S(obj) {
    var newObject = {};
    Object.keys(obj).sort().map(function(key){
      newObject[key] = obj[key];
    });
    return newObject;
}
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



var data_post=function(m0fhOhhGL, oNLhNQ){
    var aMFs = '3c9208efcfb2f5b843eec8d96de6d48a';
    var cVWG2 = 'WEB';
    var t5GECZQ = new Date().getTime();

    var pKmSFk8 = {
      appId: aMFs,
      method: m0fhOhhGL,
      timestamp: t5GECZQ,
      clienttype: cVWG2,
      object: oNLhNQ,
      secret: CryptoJS.MD5(aMFs + m0fhOhhGL + t5GECZQ + cVWG2 + JSON.stringify(osZ34YC04S(oNLhNQ))).toString()
    };
    pKmSFk8 = BASE64.encrypt(JSON.stringify(pKmSFk8));
    pKmSFk8 = AES.encrypt(pKmSFk8, acky6QolJSJi, acixHVhiNqmK);
    return pKmSFk8;
};
m0fhOhhGL="GETDAYDATA"
oNLhNQ={'city': "北京", 'month': "201401"}

console.log(data_post(m0fhOhhGL,oNLhNQ))