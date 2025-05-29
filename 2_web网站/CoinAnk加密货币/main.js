const sb = "101";
function lb() {
    let e = "a2c903cc-b31e-c547-d299-b6d07b7631ab"
      , t = function(e) {
        return e.substring(0, 8)
    }(e);
    e = function(e, t) {
        return e.replace(t, "").concat(t)
    }(e, t);
    let n = function() {
        let e = Date.now();
        return String(1 * e + 1111111111111)
    }();
    n = function(e) {
        return e.concat("347")
    }(n);
    let i = function(e, t) {
        let n = e.concat("|").concat(t);
        return n
    }(e, n);
    return function(e) {
        return "undefined" == typeof window ? Buffer.from(e).toString("base64") : window.btoa(e)
    }(i)
}

console.log(lb() )