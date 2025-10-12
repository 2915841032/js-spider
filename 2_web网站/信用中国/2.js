const sm2 = require('sm-crypto').sm2;
const BigInteger = require('jsbn').BigInteger;

// 转换十进制字符串为十六进制字符串
function Xi(t) {
    return new BigInteger(t, 10).toString(16)
}

// 转换十六进制字符串为十进制字符串
function Yi(t) {
    return new BigInteger(t, 16).toString(10)
}

// 确保字符串长度为64，不足则在前面补0
function $i(t) {
    if (t.length >= 64)
        return t;
    var e = 64 - t.length;
    return "0".repeat(e) + t
}

// 实现Zi函数：在两种格式之间转换
function Zi(t) {
    // 检查输入是否包含逗号（十进制数对格式）
    var e = t.indexOf(",");
    if (e > -1) {
        // 如果包含逗号，将两个十进制数分别转换为十六进制，然后拼接
        var r = Xi(t.slice(0, e));  // 第一个数转换为十六进制
        var n = Xi(t.slice(e + 1)); // 第二个数转换为十六进制
        return $i(r) + $i(n);       // 确保每个都是64位，然后拼接
    } else {
        // 如果不包含逗号，视为十六进制字符串格式
        // 分割为两个部分，分别转换为十进制，然后用逗号连接
        var halfLength = t.length / 2;
        var firstPart = Yi(t.slice(0, halfLength));  // 前半部分转换为十进制
        var secondPart = Yi(t.slice(halfLength));    // 后半部分转换为十进制
        return firstPart + "," + secondPart;         // 用逗号连接
    }
}

// 签名并转换的主函数
function signAndConvert(msg, privateKey, publicKey, userId) {
    // 进行SM2签名
    const signature = sm2.doSignature(msg, privateKey, {
        hash: true,
        publicKey,
        userId
    });

    console.log("原始签名结果:", signature);

    // 应用Zi转换
    const converted = Zi(signature);
    console.log("Zi转换后的结果:", converted);

    return converted;
}

// 测试数据
const msgString = 'appId=27IGtFrNFDc&encryptType=SM4&nonceStr=aae071ef936947a6a8d7e2eed87eea0a&queryContent=f8e3735a2bc6b0b110636dbca6f6059631244ee277cc8ef5d7df2e4ad5afd7b9&signType=SM2&timestamp=1760191974004&version=1.0';
const privateKey = '7faa61bb9051707ad9d9d2c417d61e038a3af871a61c8da534a9061ac1e51c32';
const publicKey = '040f5940c99c46ee9e438487c6a41d880b93f0804ea0e5ef53a062bb08203fc2a675b3d2b7a9aeb1862bb1b8fa5d17a40e300cbbe9a470ee3bf89b4ccb1c899719';
const userId = '27IGtFrNFDc';

// 执行签名和转换
const result = signAndConvert(msgString, privateKey, publicKey, userId);

// 验证转换是否可逆

