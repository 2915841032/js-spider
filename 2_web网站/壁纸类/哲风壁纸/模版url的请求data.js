const Ot = require("crypto-js")

function s(W) {
    const me = Ot.enc.Utf8.parse("68zhehao2O776519")
        , Ee = Ot.enc.Utf8.parse("aa176b7519e84710")
        , Ye = Ot.AES.encrypt(W, me, {
        iv: Ee,
        padding: Ot.pad.Pkcs7
    }).ciphertext.toString();
    return Ot.enc.Base64.stringify(Ot.enc.Hex.parse(Ye))
}

// token_ = "ack:_1748874819403167438407858758"
// P = {
//     wtId: "16534772556287360"
// }
// G = "https://x.haowallpaper.com/link/common/file/getFileImg"


function lank(token_, P,G) {
    let Fe = s(JSON.stringify({
        wtId: P.wtId,
        token: token_,
        soType: 1
    }));
    G = `${G}/${P.wtId}.png?data=${encodeURIComponent(encodeURIComponent(Fe))}`;
    res_ = s(JSON.stringify(G))
    // console.log(res_)
    return {'G': G, 'res_': res_}
}

// console.log(lank(token_, P, G));
function w(W) {
        if (Object.prototype.toString.call(W) !== "[object String]")
            return W;
        let me = null;
        try {
            const Ee = Ot.enc.Base64.parse(W).toString(Ot.enc.Hex)
              , je = Ot.enc.Utf8.parse("68zhehao2O776519")
              , Ye = Ot.enc.Utf8.parse("aa176b7519e84710")
              , Ct = Ot.lib.CipherParams.create({
                ciphertext: Ot.enc.Hex.parse(Ee)
            })
              , Lt = Ot.AES.decrypt(Ct, je, {
                iv: Ye,
                padding: Ot.pad.Pkcs7
            });
            me = Ot.enc.Utf8.stringify(Lt).replace(/\0.*$/g, "")
        } catch (Ee) {
            console.warn("jm:" + Ee)
        }
        return me
    }
// data1="PNBcAHDZJhUf9oiQJfNGWrxmv9yb1CWg7hfUvRaPsl1vnuaeXBDsTs3bM1QHb3TTT1hp9k13p+h8LdMHlq57hPblxOpanDHs4pZe/nfvTVek2ISF0smLEwROzsdhwfTwo3SsKx7AqIvw1qDy2NaosY19zP7NbereVKU2NPXvyH+kCRtd0Ugn8Zs4dmN3MHrH8XNiq842TcJfUmh4cTI4nFTob1cIwCkL5b/XiYyMegV9m5dVeWBOT3Pui18ADcFib/Y/JuKQQLK3qKNoKs6UFOeaUUUpD1KTptkKQ7VqNTW+/tCRZvB/D97EHK/woR92ZcESvSyanbFAwg7RORJQbw=="
// console.log(w(data1))