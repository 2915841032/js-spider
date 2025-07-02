function uuidV4() {
    var e = (new Date).getTime()
        , t = "undefined" !== typeof performance && performance.now && 1e3 * performance.now() || 0;
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (function (r) {
            var n = 16 * Math.random();
            return e > 0 ? (n = Math.floor((e + n) % 16),
                e = Math.floor(e / 16)) : (n = Math.floor((t + n) % 16),
                t = Math.floor(t / 16)),
                ("x" === r ? n : n / 4 + 8).toString(16)
        }
    ))
}

console.log(uuidV4())