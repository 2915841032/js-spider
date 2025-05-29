function s(e) {
    return function (e) {
        for (var t = "PXhw7UT1B0a9kQDKZsjIASmOezxYG4CHo5Jyfg2b8FLpEvRr3WtVnlqMidu6cN", i = "", a = 0; a < e.length; a++) {
            var o = t.indexOf(e[a]);
            if (-1 == o)
                var s = e[a];
            else
                s = t[(o + 3) % 62];
            var n = parseInt(62 * Math.random(), 10)
                , d = parseInt(62 * Math.random(), 10);
            i += t[n] + s + t[d]
        }
        return i
    }(e + "###" + Math.round((new Date).getTime() / 1e3).toString())
}
a="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcGVuaWQiOiJvZmcwSjVSbjN2MERCd0dWZ3JOQTd1U0VjM2JjIiwiZXhwaXJlX3RpbWUiOjE3NDE0Mjg5NTZ9.BTtgSL3ni5u6qhLpjsPGLgMQ6qwh7xcaJPalQBBQSvk"
console.log(s(a));