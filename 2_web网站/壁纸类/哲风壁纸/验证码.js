const Ot = require("crypto-js")
currentSlide="204"
c2=2.829581993569132

function _(W) {
        const me = Ot.enc.Utf8.parse("68zhehao2O776519")
          , Ee = Ot.enc.Utf8.parse("aa176b7519e84710")
          , Ye = Ot.AES.encrypt(W, me, {
            iv: Ee,
            padding: Ot.pad.Pkcs7
        }).ciphertext.toString();
        return Ot.enc.Base64.stringify(Ot.enc.Hex.parse(Ye))
    }
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
// console.log(_(JSON.stringify(Math.round(currentSlide * c2))));
data="PNBcAHDZJhUf9oiQJfNGWrxmv9yb1CWg7hfUvRaPsl1vnuaeXBDsTs3bM1QHb3TT68vnJePrNi9C6e7rdpPkgsnGywCJi9pD3N1urwbS2HIVyViTpLY4LmPH4eQWIw/bJiu3K8Wwd45+5GH2C/IfPRQ9FFda5+YG83ZVJ0AbX/7GoufxdFo1u2mw9t8h0qenZOxNjOpmby2vKz4K+vPxU8TiCuO+OrrLLlsj0d3WLi630tFS4cN16UVzkAtWHPZB/QH0GSJtN/erV1SxTjfz21S1TIiuOdEDR29ZaAA9bwx84tfMzLMpY/s0Dl+bPKNaOlNMognBnkREYXARNowOKShvgw3EAMo/FgZKG7ZjJJOEU91cxvmIrr0U/YM7QQsNd9Rlk2X2zD7T34+MDGD+wQ=="
console.log(w(data));