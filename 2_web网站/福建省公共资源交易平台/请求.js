const CryptoJS = require('crypto-js')
time = {
  "ts": 1681095241276,
  "pageNo": 3,
  "pageSize": 20,
  "total": 3762,
  "AREACODE": "",
  "M_PROJECT_TYPE": "",
  "KIND": "GCJS",
  "GGTYPE": "1",
  "PROTYPE": "",
  "timeType": "6",
  "BeginTime": "2022-10-10 00:00:00",
  "EndTime": "2023-04-10 23:59:59",
  "createTime": []
}
function u(t, e) {
  return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}
function l(t) {
  for (var e = Object.keys(t).sort(u), n = "", a = 0; a < e.length; a++)
    if (void 0 !== t[e[a]])
      if (t[e[a]] && t[e[a]]instanceof Object || t[e[a]]instanceof Array) {
        var i = JSON.stringify(t[e[a]]);
        n += e[a] + i
      } else
        n += e[a] + t[e[a]];
  return n
}
function createOutputMethod(t) {
  return CryptoJS.MD5(t).toString()
}
function d(t) {
  var e ='"createTime"'
  for (e in t)
    "" !== t[e] && void 0 !== t[e] || delete t[e];
  var n = 'B3978D054A72A7002063637CCDF6B2E5' + l(t);
  return createOutputMethod(n)
}


console.log(d(time))