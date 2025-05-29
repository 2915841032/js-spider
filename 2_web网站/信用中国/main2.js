    function Nr(t) {
        return (255 & Br[t >>> 24 & 255]) << 24 | (255 & Br[t >>> 16 & 255]) << 16 | (255 & Br[t >>> 8 & 255]) << 8 | 255 & Br[255 & t]
    }
    function Or(t) {
        return t ^ Rr(t, 2) ^ Rr(t, 10) ^ Rr(t, 18) ^ Rr(t, 24)
    }
function jr(t, e, r) {
        for (var n = new Array(4), i = new Array(4), s = 0; s < 4; s++)
            i[0] = 255 & t[4 * s],
            i[1] = 255 & t[4 * s + 1],
            i[2] = 255 & t[4 * s + 2],
            i[3] = 255 & t[4 * s + 3],
            n[s] = i[0] << 24 | i[1] << 16 | i[2] << 8 | i[3];
        for (var a, o = 0; o < 32; o += 4)
            a = n[1] ^ n[2] ^ n[3] ^ r[o + 0],
            n[0] ^= Or(Nr(a)),
            a = n[2] ^ n[3] ^ n[0] ^ r[o + 1],
            n[1] ^= Or(Nr(a)),
            a = n[3] ^ n[0] ^ n[1] ^ r[o + 2],
            n[2] ^= Or(Nr(a)),
            a = n[0] ^ n[1] ^ n[2] ^ r[o + 3],
            n[3] ^= Or(Nr(a));
        for (var u = 0; u < 16; u += 4)
            e[u] = n[3 - u / 4] >>> 24 & 255,
            e[u + 1] = n[3 - u / 4] >>> 16 & 255,
            e[u + 2] = n[3 - u / 4] >>> 8 & 255,
            e[u + 3] = 255 & n[3 - u / 4]
    }
function Rr(t, e) {
        var r = 31 & e;
        return t << r | t >>> 32 - r
    }
Br=[
    214,
    144,
    233,
    254,
    204,
    225,
    61,
    183,
    22,
    182,
    20,
    194,
    40,
    251,
    44,
    5,
    43,
    103,
    154,
    118,
    42,
    190,
    4,
    195,
    170,
    68,
    19,
    38,
    73,
    134,
    6,
    153,
    156,
    66,
    80,
    244,
    145,
    239,
    152,
    122,
    51,
    84,
    11,
    67,
    237,
    207,
    172,
    98,
    228,
    179,
    28,
    169,
    201,
    8,
    232,
    149,
    128,
    223,
    148,
    250,
    117,
    143,
    63,
    166,
    71,
    7,
    167,
    252,
    243,
    115,
    23,
    186,
    131,
    89,
    60,
    25,
    230,
    133,
    79,
    168,
    104,
    107,
    129,
    178,
    113,
    100,
    218,
    139,
    248,
    235,
    15,
    75,
    112,
    86,
    157,
    53,
    30,
    36,
    14,
    94,
    99,
    88,
    209,
    162,
    37,
    34,
    124,
    59,
    1,
    33,
    120,
    135,
    212,
    0,
    70,
    87,
    159,
    211,
    39,
    82,
    76,
    54,
    2,
    231,
    160,
    196,
    200,
    158,
    234,
    191,
    138,
    210,
    64,
    199,
    56,
    181,
    163,
    247,
    242,
    206,
    249,
    97,
    21,
    161,
    224,
    174,
    93,
    164,
    155,
    52,
    26,
    85,
    173,
    147,
    50,
    48,
    245,
    140,
    177,
    227,
    29,
    246,
    226,
    46,
    130,
    102,
    202,
    96,
    192,
    41,
    35,
    171,
    13,
    83,
    78,
    111,
    213,
    219,
    55,
    69,
    222,
    253,
    142,
    47,
    3,
    255,
    106,
    114,
    109,
    108,
    91,
    81,
    141,
    27,
    175,
    146,
    187,
    221,
    188,
    127,
    17,
    217,
    92,
    65,
    31,
    16,
    90,
    216,
    10,
    193,
    49,
    136,
    165,
    205,
    123,
    189,
    45,
    116,
    208,
    18,
    184,
    229,
    180,
    176,
    137,
    105,
    151,
    74,
    12,
    150,
    119,
    126,
    101,
    185,
    241,
    9,
    197,
    110,
    198,
    132,
    24,
    240,
    125,
    236,
    58,
    220,
    77,
    32,
    121,
    238,
    95,
    62,
    215,
    203,
    57,
    72
]
function Nr(t) {
    return (255 & Br[t >>> 24 & 255]) << 24 | (255 & Br[t >>> 16 & 255]) << 16 | (255 & Br[t >>> 8 & 255]) << 8 | 255 & Br[255 & t]
}

function Hr(t) {
    return t ^ Rr(t, 13) ^ Rr(t, 23)
}

function Tr(t) {
    for (var e = [], r = 0, n = t.length; r < n; r += 2)
        e.push(parseInt(t.substr(r, 2), 16));
    return e
}

Cr = [
    462357,
    472066609,
    943670861,
    1415275113,
    1886879365,
    2358483617,
    2830087869,
    3301692121,
    3773296373,
    4228057617,
    404694573,
    876298825,
    1347903077,
    1819507329,
    2291111581,
    2762715833,
    3234320085,
    3705924337,
    4177462797,
    337322537,
    808926789,
    1280531041,
    1752135293,
    2223739545,
    2695343797,
    3166948049,
    3638552301,
    4110090761,
    269950501,
    741554753,
    1213159005,
    1684763257
]

function _r(t, e, r) {
    var n = arguments.length > 3 && void 0 !== arguments[3] ? arguments[3] : {}
        , i = n.padding
        , s = void 0 === i ? "pkcs#7" : i
        , a = n.mode
        , o = n.iv
        , u = void 0 === o ? [] : o
        , h = n.output
        , c = void 0 === h ? "string" : h;
    if ("cbc" === a && ("string" == typeof u && (u = Tr(u)),
    16 !== u.length))
        throw new Error("iv is invalid");
    if ("string" == typeof e && (e = Tr(e)),
    16 !== e.length)
        throw new Error("key is invalid");
    if (t = "string" == typeof t ? r !== 0 ? function (t) {
        for (var e = [], r = 0, n = t.length; r < n; r++) {
            var i = t.codePointAt(r);
            if (i <= 127)
                e.push(i);
            else if (i <= 2047)
                e.push(192 | i >>> 6),
                    e.push(128 | 63 & i);
            else if (i <= 55295 || i >= 57344 && i <= 65535)
                e.push(224 | i >>> 12),
                    e.push(128 | i >>> 6 & 63),
                    e.push(128 | 63 & i);
            else {
                if (!(i >= 65536 && i <= 1114111))
                    throw e.push(i),
                        new Error("input is not supported");
                r++,
                    e.push(240 | i >>> 18 & 28),
                    e.push(128 | i >>> 12 & 63),
                    e.push(128 | i >>> 6 & 63),
                    e.push(128 | 63 & i)
            }
        }
        return e
    }(t) : Tr(t) : y(t),
    ("pkcs#5" === s || "pkcs#7" === s) && r !== 0)
        for (var l = 16 - t.length % 16, f = 0; f < l; f++)
            t.push(l);
    var p = new Array(32);
    !function (t, e, r) {
        for (var n = new Array(4), i = new Array(4), s = 0; s < 4; s++)
            i[0] = 255 & t[0 + 4 * s],
                i[1] = 255 & t[1 + 4 * s],
                i[2] = 255 & t[2 + 4 * s],
                i[3] = 255 & t[3 + 4 * s],
                n[s] = i[0] << 24 | i[1] << 16 | i[2] << 8 | i[3];
        n[0] ^= 2746333894,
            n[1] ^= 1453994832,
            n[2] ^= 1736282519,
            n[3] ^= 2993693404;
        for (var a, o = 0; o < 32; o += 4)
            a = n[1] ^ n[2] ^ n[3] ^ Cr[o + 0],
                e[o + 0] = n[0] ^= Hr(Nr(a)),
                a = n[2] ^ n[3] ^ n[0] ^ Cr[o + 1],
                e[o + 1] = n[1] ^= Hr(Nr(a)),
                a = n[3] ^ n[0] ^ n[1] ^ Cr[o + 2],
                e[o + 2] = n[2] ^= Hr(Nr(a)),
                a = n[0] ^ n[1] ^ n[2] ^ Cr[o + 3],
                e[o + 3] = n[3] ^= Hr(Nr(a));
        if (r === 0)
            for (var u, h = 0; h < 16; h++)
                u = e[h],
                    e[h] = e[31 - h],
                    e[31 - h] = u
    }(e, p, r);
    for (var d = [], g = u, v = t.length, m = 0; v >= 16;) {
        var x = t.slice(m, m + 16)
            , S = new Array(16);
        if ("cbc" === a)
            for (var w = 0; w < 16; w++)
                r !== 0 && (x[w] ^= g[w]);
        jr(x, S, p);
        for (var E = 0; E < 16; E++)
            "cbc" === a && r === 0 && (S[E] ^= g[E]),
                d[m + E] = S[E];
        "cbc" === a && (g = r !== 0 ? S : x),
            v -= 16,
            m += 16
    }
    if (("pkcs#5" === s || "pkcs#7" === s) && r === 0) {
        for (var b = d.length, F = d[b - 1], A = 1; A <= F; A++)
            if (d[b - A] !== F)
                throw new Error("padding is invalid");
        d.splice(b - F, F)
    }
    return "array" !== c ? r !== 0 ? d.map((function (t) {
            return 1 === (t = t.toString(16)).length ? "0" + t : t
        }
    )).join("") : function (t) {
        for (var e = [], r = 0, n = t.length; r < n; r++)
            t[r] >= 240 && t[r] <= 247 ? (e.push(String.fromCodePoint(((7 & t[r]) << 18) + ((63 & t[r + 1]) << 12) + ((63 & t[r + 2]) << 6) + (63 & t[r + 3]))),
                r += 3) : t[r] >= 224 && t[r] <= 239 ? (e.push(String.fromCodePoint(((15 & t[r]) << 12) + ((63 & t[r + 1]) << 6) + (63 & t[r + 2]))),
                r += 2) : t[r] >= 192 && t[r] <= 223 ? (e.push(String.fromCodePoint(((31 & t[r]) << 6) + (63 & t[r + 1]))),
                r++) : e.push(String.fromCodePoint(t[r]));
        return e.join("")
    }(d) : d
}


console.log(_r("param=&page=1&size=10", "dbb78b8b64d640bb130255c69e959973", {
    "output": "string"
}));