
// uuid 开始
function T() {
}

function R(t, e) {
    return Math.floor(Math.random() * (e - t + 1)) + t
}

T.maxFromBits = function (t) {
    return Math.pow(2, t)
}
    ,
    T.limitUI04 = T.maxFromBits(4),
    T.limitUI06 = T.maxFromBits(6),
    T.limitUI08 = T.maxFromBits(8),
    T.limitUI12 = T.maxFromBits(12),
    T.limitUI14 = T.maxFromBits(14),
    T.limitUI16 = T.maxFromBits(16),
    T.limitUI32 = T.maxFromBits(32),
    T.limitUI40 = T.maxFromBits(40),
    T.limitUI48 = T.maxFromBits(48),
    T.randomUI04 = function () {
        return R(0, T.limitUI04 - 1)
    }
    ,
    T.randomUI06 = function () {
        return R(0, T.limitUI06 - 1)
    }
    ,
    T.randomUI08 = function () {
        return R(0, T.limitUI08 - 1)
    }
    ,
    T.randomUI12 = function () {
        return R(0, T.limitUI12 - 1)
    }
    ,
    T.randomUI14 = function () {
        return R(0, T.limitUI14 - 1)
    }
    ,
    T.randomUI16 = function () {
        return R(0, T.limitUI16 - 1)
    }
    ,
    T.randomUI32 = function () {
        return R(0, T.limitUI32 - 1)
    }
    ,
    T.randomUI40 = function () {
        return (0 | Math.random() * (1 << 30)) + (0 | 1024 * Math.random()) * (1 << 30)
    }
    ,
    T.randomUI48 = function () {
        return (0 | Math.random() * (1 << 30)) + (0 | Math.random() * (1 << 18)) * (1 << 30)
    }
    ,
    T.paddedString = function (t, e, r) {
        r = r || "0";
        for (var n = e - (t = String(t)).length; n > 0; n >>>= 1,
            r += r)
            1 & n && (t = r + t);
        return t
    }
    ,
    T.prototype.fromParts = function (t, e, r, n, i, s) {
        return this.version = r >> 12 & 15,
            this.hex = T.paddedString(t.toString(16), 8) + "-" + T.paddedString(e.toString(16), 4) + "-" + T.paddedString(r.toString(16), 4) + "-" + T.paddedString(n.toString(16), 2) + T.paddedString(i.toString(16), 2) + "-" + T.paddedString(s.toString(16), 12),
            this
    }
    ,
    T.prototype.toString = function () {
        return this.hex
    }
    ,
    T.prototype.toURN = function () {
        return "urn:uuid:" + this.hex
    }
    ,
    T.prototype.toBytes = function () {
        for (var t = this.hex.split("-"), e = [], r = 0, n = 0; n < t.length; n++)
            for (var i = 0; i < t[n].length; i += 2)
                e[r++] = parseInt(t[n].substr(i, 2), 16);
        return e
    }
    ,
    T.prototype.equals = function (t) {
        return t instanceof UUID && this.hex === t.hex
    }
    ,
    T.getTimeFieldValues = function (t) {
        var e = t - Date.UTC(1582, 9, 15)
            , r = e / 4294967296 * 1e4 & 268435455;
        return {
            low: 1e4 * (268435455 & e) % 4294967296,
            mid: 65535 & r,
            hi: r >>> 16,
            timestamp: e
        }
    }
    ,
    T._create4 = function () {
        return (new T).fromParts(T.randomUI32(), T.randomUI16(), 16384 | T.randomUI12(), 128 | T.randomUI06(), T.randomUI08(), T.randomUI48())
    }
T._create1 = function () {
    var t = (new Date).getTime()
        , e = T.randomUI14()
        , r = 1099511627776 * (1 | T.randomUI08()) + T.randomUI40()
        , n = T.randomUI04()
        , i = 0;
    t != i ? (t < i && e++,
        i = t,
        n = T.randomUI04()) : Math.random() < 1 / 4 && n < 9984 ? n += 1 + T.randomUI04() : e++;
    var s = T.getTimeFieldValues(i)
        , a = s.low + n
        , o = 4095 & s.hi | 4096
        , u = (e &= 16383) >>> 8 | 128
        , h = 255 & e;
    return (new T).fromParts(a, s.mid, o, u, h, r)
}
    ,

    T.create = function (t) {
        return (new T).fromParts(T.randomUI32(), T.randomUI16(), 16384 | T.randomUI12(), 128 | T.randomUI06(), T.randomUI08(), T.randomUI48())
    }

function uuid() {
    return T.create().toString().replace(/-/g, "")
}

console.log(uuid())

// uuid结束

//queryContent开始


var appSignPrivateKey = "xxx";
var appSignPublicKey = "xxx";
var n = {
    version: "1.0",
    appId: 'xxxx',
    signType: 'SM2',
    encryptType: 'SM4',
    nonceStr: uuid(),
    timestamp: H.timeStamp()
};
var i = `param=&page=${page}&size=10`;
var page = 1
encryptKey = "dbb78b8b64d640bb130255c69e959973"
n.queryContent = ls.sm4.encrypt(i, encryptKey)
n.sign = Zi(o = ls.sm2.signature(a, appSignPrivateKey, appSignPublicKey, n.appId));