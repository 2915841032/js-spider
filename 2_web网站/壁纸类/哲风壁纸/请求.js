const Ot = require("crypto-js")

function _(W) {
        const me = Ot.enc.Utf8.parse("68zhehao2O776519")
          , Ee = Ot.enc.Utf8.parse("aa176b7519e84710")
          , Ye = Ot.AES.encrypt(W, me, {
            iv: Ee,
            padding: Ot.pad.Pkcs7
        }).ciphertext.toString();
        return Ot.enc.Base64.stringify(Ot.enc.Hex.parse(Ye))
    }
data = '{"page":"8","sortType":3,"isSel":"true","rows":9,"isFavorites":false,"wpType":1}'
data = '{"wtId":"16893381053500800","token":"ack:_1748874819403167438407858758","soType":1}'
// data = 'https://haowallpaper.com/homeViewLook/16683512067640704'
console.log(_(data))


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

data1="PNBcAHDZJhUf9oiQJfNGWrxmv9yb1CWg7hfUvRaPsl1vnuaeXBDsTs3bM1QHb3TTT1hp9k13p+h8LdMHlq57hPblxOpanDHs4pZe/nfvTVek2ISF0smLEwROzsdhwfTwo3SsKx7AqIvw1qDy2NaosY19zP7NbereVKU2NPXvyH+kCRtd0Ugn8Zs4dmN3MHrH8XNiq842TcJfUmh4cTI4nFTob1cIwCkL5b/XiYyMegV9m5dVeWBOT3Pui18ADcFib/Y/JuKQQLK3qKNoKs6UFOeaUUUpD1KTptkKQ7VqNTW+/tCRZvB/D97EHK/woR92ZcESvSyanbFAwg7RORJQbw=="
// data1="PNBcAHDZJhUf9oiQJfNGWrxmv9yb1CWg7hfUvRaPsl1vnuaeXBDsTs3bM1QHb3TTyFAT7K4z8OjZHNIDkYz5WCM8TyijWcEfq7sSCVWGSdmXbUAkqxE6uoHwxaSsncZ96ycf4yL0ejiY+9s+XK3gryDupldCj69u+J7qIFsJnntlpN22Li/7+9VyFiF/pkBN8LjzXujyt5Cl78QWNTwyHAorbIkAsbCud8J40rIPHcaISW/wJ6mryVQ0EaSJPqs1AnxSXHajwCDAmGXSUn+hM5MMORl81ouyl7gDmMGLxm7rEresdpizdDgmxonX/Xe+"
// data1="x9lnvf3SGlS4zvFPpRhsdnB08uNWkUootx70a3346uiRtDt%252FLbifjtBqG6FA6LlU%252B%252BNIWevFthRVvGrvjapTIQQkN9ylH0C%252BT3vID%252Bo73SARq9kMlduF8SzELE1a%252B8JA"
// console.log(w(data1))