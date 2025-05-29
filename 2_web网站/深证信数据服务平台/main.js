CryptoJS = require("crypto-js")
Math1 = {
    "lfsjr": "tempenc",
    "JQXgn": "1234567887654321",
    "CGVAQ": "script",
    "RCmPP": "data:text/javascript;base64,",
    "fJcEo": "var xhr=new XMLHttpRequest();xhr.open('GET','/api/m'+'code/slatkey');xhr.send();xhr.onreadystatechange=function(){if(xhr.readyState!=4)return;var r=xhr.responseText;/^\\w+$/.test(r)&&localStorage.setItem('tempenc',r)}"
}


function getResCode() {
    _0x1e077e = CryptoJS["AES"]["encrypt"](CryptoJS["enc"]["Utf8"]["parse"](Math["floor"](Math["floor"](new Date()["getTime"](), -6658 + 8604 + -946))), CryptoJS["enc"]["Utf8"]["parse"]("1234567887654321"), {
        'iv': CryptoJS["enc"]["Utf8"]["parse"]("1234567887654321"),
        'mode': CryptoJS["mode"]["CBC"],
        'padding': CryptoJS["pad"]["Pkcs7"]
    });

    return CryptoJS["enc"]["Base64"]["stringify"](_0x1e077e["ciphertext"]);
}

console.log(getResCode())

//写一个AES的cbc加密函数,使用utf-8编码,变量名为标准,不用混淆
function encryptTimestamp1() {
    // 获取当前时间戳
    const timestamp = new Date().getTime();

    // 定义密钥和初始化向量 (IV)
    const key = CryptoJS.enc.Utf8.parse("1234567887654321");
    const iv = CryptoJS.enc.Utf8.parse("1234567887654321");

    // 将时间戳转换为 UTF-8 编码的格式
    const message = CryptoJS.enc.Utf8.parse(timestamp.toString());

    // 使用 AES 加密时间戳，采用 CBC 模式和 PKCS7 填充
    const encrypted = CryptoJS.AES.encrypt(message, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });

    // 返回加密后的 Base64 字符串
    return encrypted.toString(CryptoJS.enc.Base64);
}

// console.log(encryptTimestamp1())

