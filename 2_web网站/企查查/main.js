var crypto = require('crypto-js')

dd = function (text, key) {
    return crypto.HmacSHA512(text, key).toString()
}

cc = function () {
    o = {
        "n": 20,
        "codes": {
            "0": "W",
            "1": "l",
            "2": "k",
            "3": "B",
            "4": "Q",
            "5": "g",
            "6": "f",
            "7": "i",
            "8": "i",
            "9": "r",
            "10": "v",
            "11": "6",
            "12": "A",
            "13": "K",
            "14": "N",
            "15": "k",
            "16": "4",
            "17": "L",
            "18": "1",
            "19": "8"
        }
    }
    for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
        var a = t[i].charCodeAt() % o.n;
        n += o.codes[a]
    }
    return n
}


a = function (t, e) {
    var e = e
        , t = t.toLowerCase()
        , n = JSON.stringify(e).toLowerCase();
    return (0,
        dd)(t + n, (0,
        cc)(t)).toLowerCase().substr(8, 20)
}


// 值

bc = function () {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ""
        , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , i = JSON.stringify(e).toLowerCase();
    return (0,
        dd)(n + "pathString" + i + t, (0,
        cc)(n))
};

function get_data(e) {
    t = "/api/search/searchmulti"
    key = (0, a)(t, e)
    val = (0, bc)(t, e, 'a68a7d288406f345768fdf4c3ef01ced')
    return {'key': key, 'val': val}
}

e = {
    "searchKey": "小米",
    "pageIndex": 1,
    "pageSize": 20
};
console.log(get_data(e));


