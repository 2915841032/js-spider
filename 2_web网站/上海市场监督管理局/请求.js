function sign() {
    window = global;
    const JSEncrypt = require('JSEncrypt')
    var encryptor = new JSEncrypt()  // 创建加密对象实例
    //之前ssl生成的公钥，复制的时候要小心不要有空格
    var pubKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCMFPpXdR/mA3FOyB2L6HaxKRMBDWAPWA2j3qjBdDCu4lTiJ+ip9PwJW3XtaBonyeBdo22AYhMkLjAzfJnoFOFtbOf+oF4Ht4pgR3csXQqJsgvMSPInzexdayTD5Vg/quIgLlWVBLn670O2YOHd9/Ojc2GidoJnUO4D8YlfSd/sEwIDAQAB"
    encryptor.setPublicKey(pubKey)//设置公钥
    var Timestamp=new Date().getTime()+'' //获取时间戳
    console.log(Timestamp)
    var rsaPassWord = encryptor.encrypt(Timestamp) // 对内容进行加密
    console.log(rsaPassWord)
    return {'sign':rsaPassWord,'Timestamp':Timestamp}
}
sign()