CryptoJS=require("crypto-js")
function getResCode() {
    // 生成秒级时间戳并转换为UTF8明文
    const timestamp = Math.floor(Date.now() / 1000);
    const plainText = CryptoJS.enc.Utf8.parse(timestamp.toString());

    // 定义加密密钥和初始化向量
    const key = CryptoJS.enc.Utf8.parse("1234567887654321");
    const iv = CryptoJS.enc.Utf8.parse("1234567887654321");

    // 执行AES-CBC加密
    const encrypted = CryptoJS.AES.encrypt(plainText, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });

    // 返回Base64格式密文
    return CryptoJS.enc.Base64.stringify(encrypted.ciphertext);
}

console.log(getResCode())