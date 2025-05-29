CryptoJS=require('crypto-js')

function encrypt() {
    // 时间的时分秒格式化
    var timeString = getFormatDate();
    function getFormatDate() {
        var date = new Date();
        var year = date.getFullYear();
        var mon = date.getMonth() + 1;
        var day = date.getDate();
        var hour = date.getHours();
        var minute = date.getMinutes();
        var second = date.getSeconds();
        if (mon.toString().length === 1) {
            mon = "0" + mon;
        }
        return year + '' + mon + '' + day + '' + hour + '' + minute + '' + second;
    }
    city='changshaxian'
    // var timeString = year + '' + mon + '' + day + '' + hour + '' + minute + '' + second;
    var data = city + '_' + timeString;
    // var data = "changshaxian_20250225205859";
    console.log(data);
    let key = CryptoJS["enc"]["Utf8"]["parse"]("5ha5Z7cZ3WNbD3rA");
    let iv = CryptoJS['enc']['Utf8']["parse"]("AYk98XaiBwCi0Dst");
    let encryptData = CryptoJS['AES']["encrypt"](data, key, {
        'mode': CryptoJS['mode']['CBC'],
        'iv': iv,
        'padding': CryptoJS["pad"]["Pkcs7"]
    });
    return encryptData["toString"]();
}

console.log(encrypt())