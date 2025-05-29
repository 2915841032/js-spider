function ank(e) {
    var t = (1 * e + 1111111111111).toString().split("")
        , n = parseInt(10 * Math.random(), 10)
        , r = parseInt(10 * Math.random(), 10)
        , o = parseInt(10 * Math.random(), 10);
    return t.concat([n, r, o]).join("")
}

function comb(e, t) {
    var n = "".concat(e, "|").concat(t);
    return btoa(n)
}

function get_id() {
    var e = (new Date).getTime()
    v = e
    t = "-b31e-4547-9299-b6d07b7631aba2c903cc";
    e =ank(e)
    bb=comb(t, e)
    return {v,bb}
}

console.log(get_id())