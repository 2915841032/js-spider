function encrypt(text) {
    const Ae = require('crypto-js'); // 引入加密库

    // 加密的密钥和IV
    const key = Ae.enc.Utf8.parse("68zhehao20776519");
    const iv = Ae.enc.Utf8.parse("aa176b7519e84710");

    // 明文转换为UTF-8字节数据
    const message = Ae.enc.Utf8.parse(text);

    // 使用AES加密
    const encrypted = Ae.AES.encrypt(message, key, {
        iv: iv,
        padding: Ae.pad.Pkcs7
    });

    // 将加密后的密文转为Base64编码并返回
    return encrypted.toString();
}

const plainText = '{"page":"23","sortType":3,"isSel":"true","rows":9,"isFavorites":false,"wpType":1}';
const encryptedText = encrypt(plainText);

console.log(encryptedText);
