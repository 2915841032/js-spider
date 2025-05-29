function main23() {
    document={}
    location={reload:function (){}}
    var s = {},
        u, c, U, r, i, l = 0,
        a, e = eval,
        w = String.fromCharCode,
        sucuri_cloudproxy_js = '',
        S =
            'ZT0iYnN1Ii5zbGljZSgwLDEpICsgImZmIi5jaGFyQXQoMCkgKyAiYnN1Ii5zbGljZSgwLDEpICsgU3RyaW5nLmZyb21DaGFyQ29kZSg5NykgKyBTdHJpbmcuZnJvbUNoYXJDb2RlKDU3KSArICcxJyArICAgJycgKyJhIiArICdLMicuc2xpY2UoMSwyKSsgJycgKyJic2VjIi5zdWJzdHIoMCwxKSArICAnJyArJzRxRzUnLnN1YnN0cigzLCAxKSArJ0cyJy5zbGljZSgxLDIpKyJhc2VjIi5zdWJzdHIoMCwxKSArICAnJyArJycrU3RyaW5nLmZyb21DaGFyQ29kZSg0OSkgKyAnVjInLnNsaWNlKDEsMikrICcnICsnJysiYXN1Y3VyIi5jaGFyQXQoMCkrIiIgKyJmIiArICIzc3UiLnNsaWNlKDAsMSkgKyAnVjAnLnNsaWNlKDEsMikrJ01kSGInLnN1YnN0cigzLCAxKSArIiIgKydTMycuc2xpY2UoMSwyKSsiYyIuc2xpY2UoMCwxKSArICAnJyArJycrU3RyaW5nLmZyb21DaGFyQ29kZSg5NykgKyAnTjcnLnNsaWNlKDEsMikrJ2EnICsgICdZZScuc2xpY2UoMSwyKStTdHJpbmcuZnJvbUNoYXJDb2RlKDB4MzkpICsgIiIgKyc1JyArICAnMScgKyAgJzs4Jy5zbGljZSgxLDIpKyJmIiArICAnJyArImQiLnNsaWNlKDAsMSkgKyAgJycgKycnKydkWTMnLmNoYXJBdCgyKSsnJztkb2N1bWVudC5jb29raWU9J3MnKydzdWN1dScuY2hhckF0KDQpKyAnYycrJ3VzdWN1Jy5jaGFyQXQoMCkgICsncicrJ2knKydfJysnJysnYycrJ2wnKydvJy5jaGFyQXQoMCkrJ3VzdScuY2hhckF0KDApICsnZCcrJycrJ3N1Y3VwJy5jaGFyQXQoNCkrICdzcicuY2hhckF0KDEpKydvJysnJysneCcrJycrJ3lzdWN1Jy5jaGFyQXQoMCkgICsnc3VfJy5jaGFyQXQoMikrJ3N1Y3VyaXUnLmNoYXJBdCg2KSsndScrJycrJ2lzdWN1Jy5jaGFyQXQoMCkgICsnc3VkJy5jaGFyQXQoMikrJ3N1Y3VyXycuY2hhckF0KDUpICsgJ2InLmNoYXJBdCgwKSsnYicrJzQnKydjc3VjdScuY2hhckF0KDApICArJzNzdWN1cmknLmNoYXJBdCgwKSArICc5cycuY2hhckF0KDApKyc2c3VjdXJpJy5jaGFyQXQoMCkgKyAnNCcrJ2UnKyI9IiArIGUgKyAnO3BhdGg9LzttYXgtYWdlPTg2NDAwJzsgbG9jYXRpb24ucmVsb2FkKCk7';
    L = S.length;
    U = 0;
    r = '';
    var A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
    for (u = 0; u < 64; u++) {
        s[A.charAt(u)] = u;
    }
    for (i = 0; i < L; i++) {
        c = s[S.charAt(i)];
        U = (U << 6) + c;
        l += 6;
        while (l >= 8) {
            ((a = (U >>> (l -= 8)) & 0xff) || (i < (L - 2))) && (r += w(a));
        }
    }
    e(r);
    return document.cookie
}
main23()
console.log(document.cookie);