function jlk() {
        var t;
        function e(t, e, r) {
            null != t && ("number" == typeof t ? this.fromNumber(t, e, r) : null == e && "string" != typeof t ? this.fromString(t, 256) : this.fromString(t, e))
        }
        function r() {
            return new e(null)
        }
        var n = "undefined" != typeof navigator;
        n && "Microsoft Internet Explorer" == navigator.appName ? (e.prototype.am = function(t, e, r, n, i, s) {
            for (var a = 32767 & e, o = e >> 15; --s >= 0; ) {
                var u = 32767 & this[t]
                  , h = this[t++] >> 15
                  , c = o * u + h * a;
                i = ((u = a * u + ((32767 & c) << 15) + r[n] + (1073741823 & i)) >>> 30) + (c >>> 15) + o * h + (i >>> 30),
                r[n++] = 1073741823 & u
            }
            return i
        }
        ,
        t = 30) : n && "Netscape" != navigator.appName ? (e.prototype.am = function(t, e, r, n, i, s) {
            for (; --s >= 0; ) {
                var a = e * this[t++] + r[n] + i;
                i = Math.floor(a / 67108864),
                r[n++] = 67108863 & a
            }
            return i
        }
        ,
        t = 26) : (e.prototype.am = function(t, e, r, n, i, s) {
            for (var a = 16383 & e, o = e >> 14; --s >= 0; ) {
                var u = 16383 & this[t]
                  , h = this[t++] >> 14
                  , c = o * u + h * a;
                i = ((u = a * u + ((16383 & c) << 14) + r[n] + i) >> 28) + (c >> 14) + o * h,
                r[n++] = 268435455 & u
            }
            return i
        }
        ,
        t = 28),
        e.prototype.DB = t,
        e.prototype.DM = (1 << t) - 1,
        e.prototype.DV = 1 << t,
        e.prototype.FV = Math.pow(2, 52),
        e.prototype.F1 = 52 - t,
        e.prototype.F2 = 2 * t - 52;
        var i, s, a = "0123456789abcdefghijklmnopqrstuvwxyz", o = new Array;
        for (i = "0".charCodeAt(0),
        s = 0; s <= 9; ++s)
            o[i++] = s;
        for (i = "a".charCodeAt(0),
        s = 10; s < 36; ++s)
            o[i++] = s;
        for (i = "A".charCodeAt(0),
        s = 10; s < 36; ++s)
            o[i++] = s;
        function u(t) {
            return a.charAt(t)
        }
        function h(t, e) {
            var r = o[t.charCodeAt(e)];
            return null == r ? -1 : r
        }
        function c(t) {
            var e = r();
            return e.fromInt(t),
            e
        }
        function l(t) {
            var e, r = 1;
            return 0 != (e = t >>> 16) && (t = e,
            r += 16),
            0 != (e = t >> 8) && (t = e,
            r += 8),
            0 != (e = t >> 4) && (t = e,
            r += 4),
            0 != (e = t >> 2) && (t = e,
            r += 2),
            0 != (e = t >> 1) && (t = e,
            r += 1),
            r
        }
        function f(t) {
            this.m = t
        }
        function p(t) {
            this.m = t,
            this.mp = t.invDigit(),
            this.mpl = 32767 & this.mp,
            this.mph = this.mp >> 15,
            this.um = (1 << t.DB - 15) - 1,
            this.mt2 = 2 * t.t
        }
        function d(t, e) {
            return t & e
        }
        function g(t, e) {
            return t | e
        }
        function v(t, e) {
            return t ^ e
        }
        function y(t, e) {
            return t & ~e
        }
        function m(t) {
            if (0 == t)
                return -1;
            var e = 0;
            return 0 == (65535 & t) && (t >>= 16,
            e += 16),
            0 == (255 & t) && (t >>= 8,
            e += 8),
            0 == (15 & t) && (t >>= 4,
            e += 4),
            0 == (3 & t) && (t >>= 2,
            e += 2),
            0 == (1 & t) && ++e,
            e
        }
        function x(t) {
            for (var e = 0; 0 != t; )
                t &= t - 1,
                ++e;
            return e
        }
        function S() {}
        function w(t) {
            return t
        }
        function E(t) {
            this.r2 = r(),
            this.q3 = r(),
            e.ONE.dlShiftTo(2 * t.t, this.r2),
            this.mu = this.r2.divide(t),
            this.m = t
        }
        f.prototype.convert = function(t) {
            return t.s < 0 || t.compareTo(this.m) >= 0 ? t.mod(this.m) : t
        }
        ,
        f.prototype.revert = function(t) {
            return t
        }
        ,
        f.prototype.reduce = function(t) {
            t.divRemTo(this.m, null, t)
        }
        ,
        f.prototype.mulTo = function(t, e, r) {
            t.multiplyTo(e, r),
            this.reduce(r)
        }
        ,
        f.prototype.sqrTo = function(t, e) {
            t.squareTo(e),
            this.reduce(e)
        }
        ,
        p.prototype.convert = function(t) {
            var n = r();
            return t.abs().dlShiftTo(this.m.t, n),
            n.divRemTo(this.m, null, n),
            t.s < 0 && n.compareTo(e.ZERO) > 0 && this.m.subTo(n, n),
            n
        }
        ,
        p.prototype.revert = function(t) {
            var e = r();
            return t.copyTo(e),
            this.reduce(e),
            e
        }
        ,
        p.prototype.reduce = function(t) {
            for (; t.t <= this.mt2; )
                t[t.t++] = 0;
            for (var e = 0; e < this.m.t; ++e) {
                var r = 32767 & t[e]
                  , n = r * this.mpl + ((r * this.mph + (t[e] >> 15) * this.mpl & this.um) << 15) & t.DM;
                for (t[r = e + this.m.t] += this.m.am(0, n, t, e, 0, this.m.t); t[r] >= t.DV; )
                    t[r] -= t.DV,
                    t[++r]++
            }
            t.clamp(),
            t.drShiftTo(this.m.t, t),
            t.compareTo(this.m) >= 0 && t.subTo(this.m, t)
        }
        ,
        p.prototype.mulTo = function(t, e, r) {
            t.multiplyTo(e, r),
            this.reduce(r)
        }
        ,
        p.prototype.sqrTo = function(t, e) {
            t.squareTo(e),
            this.reduce(e)
        }
        ,
        e.prototype.copyTo = function(t) {
            for (var e = this.t - 1; e >= 0; --e)
                t[e] = this[e];
            t.t = this.t,
            t.s = this.s
        }
        ,
        e.prototype.fromInt = function(t) {
            this.t = 1,
            this.s = t < 0 ? -1 : 0,
            t > 0 ? this[0] = t : t < -1 ? this[0] = t + this.DV : this.t = 0
        }
        ,
        e.prototype.fromString = function(t, r) {
            var n;
            if (16 == r)
                n = 4;
            else if (8 == r)
                n = 3;
            else if (256 == r)
                n = 8;
            else if (2 == r)
                n = 1;
            else if (32 == r)
                n = 5;
            else {
                if (4 != r)
                    return void this.fromRadix(t, r);
                n = 2
            }
            this.t = 0,
            this.s = 0;
            for (var i = t.length, s = !1, a = 0; --i >= 0; ) {
                var o = 8 == n ? 255 & t[i] : h(t, i);
                o < 0 ? "-" == t.charAt(i) && (s = !0) : (s = !1,
                0 == a ? this[this.t++] = o : a + n > this.DB ? (this[this.t - 1] |= (o & (1 << this.DB - a) - 1) << a,
                this[this.t++] = o >> this.DB - a) : this[this.t - 1] |= o << a,
                (a += n) >= this.DB && (a -= this.DB))
            }
            8 == n && 0 != (128 & t[0]) && (this.s = -1,
            a > 0 && (this[this.t - 1] |= (1 << this.DB - a) - 1 << a)),
            this.clamp(),
            s && e.ZERO.subTo(this, this)
        }
        ,
        e.prototype.clamp = function() {
            for (var t = this.s & this.DM; this.t > 0 && this[this.t - 1] == t; )
                --this.t
        }
        ,
        e.prototype.dlShiftTo = function(t, e) {
            var r;
            for (r = this.t - 1; r >= 0; --r)
                e[r + t] = this[r];
            for (r = t - 1; r >= 0; --r)
                e[r] = 0;
            e.t = this.t + t,
            e.s = this.s
        }
        ,
        e.prototype.drShiftTo = function(t, e) {
            for (var r = t; r < this.t; ++r)
                e[r - t] = this[r];
            e.t = Math.max(this.t - t, 0),
            e.s = this.s
        }
        ,
        e.prototype.lShiftTo = function(t, e) {
            var r, n = t % this.DB, i = this.DB - n, s = (1 << i) - 1, a = Math.floor(t / this.DB), o = this.s << n & this.DM;
            for (r = this.t - 1; r >= 0; --r)
                e[r + a + 1] = this[r] >> i | o,
                o = (this[r] & s) << n;
            for (r = a - 1; r >= 0; --r)
                e[r] = 0;
            e[a] = o,
            e.t = this.t + a + 1,
            e.s = this.s,
            e.clamp()
        }
        ,
        e.prototype.rShiftTo = function(t, e) {
            e.s = this.s;
            var r = Math.floor(t / this.DB);
            if (r >= this.t)
                e.t = 0;
            else {
                var n = t % this.DB
                  , i = this.DB - n
                  , s = (1 << n) - 1;
                e[0] = this[r] >> n;
                for (var a = r + 1; a < this.t; ++a)
                    e[a - r - 1] |= (this[a] & s) << i,
                    e[a - r] = this[a] >> n;
                n > 0 && (e[this.t - r - 1] |= (this.s & s) << i),
                e.t = this.t - r,
                e.clamp()
            }
        }
        ,
        e.prototype.subTo = function(t, e) {
            for (var r = 0, n = 0, i = Math.min(t.t, this.t); r < i; )
                n += this[r] - t[r],
                e[r++] = n & this.DM,
                n >>= this.DB;
            if (t.t < this.t) {
                for (n -= t.s; r < this.t; )
                    n += this[r],
                    e[r++] = n & this.DM,
                    n >>= this.DB;
                n += this.s
            } else {
                for (n += this.s; r < t.t; )
                    n -= t[r],
                    e[r++] = n & this.DM,
                    n >>= this.DB;
                n -= t.s
            }
            e.s = n < 0 ? -1 : 0,
            n < -1 ? e[r++] = this.DV + n : n > 0 && (e[r++] = n),
            e.t = r,
            e.clamp()
        }
        ,
        e.prototype.multiplyTo = function(t, r) {
            var n = this.abs()
              , i = t.abs()
              , s = n.t;
            for (r.t = s + i.t; --s >= 0; )
                r[s] = 0;
            for (s = 0; s < i.t; ++s)
                r[s + n.t] = n.am(0, i[s], r, s, 0, n.t);
            r.s = 0,
            r.clamp(),
            this.s != t.s && e.ZERO.subTo(r, r)
        }
        ,
        e.prototype.squareTo = function(t) {
            for (var e = this.abs(), r = t.t = 2 * e.t; --r >= 0; )
                t[r] = 0;
            for (r = 0; r < e.t - 1; ++r) {
                var n = e.am(r, e[r], t, 2 * r, 0, 1);
                (t[r + e.t] += e.am(r + 1, 2 * e[r], t, 2 * r + 1, n, e.t - r - 1)) >= e.DV && (t[r + e.t] -= e.DV,
                t[r + e.t + 1] = 1)
            }
            t.t > 0 && (t[t.t - 1] += e.am(r, e[r], t, 2 * r, 0, 1)),
            t.s = 0,
            t.clamp()
        }
        ,
        e.prototype.divRemTo = function(t, n, i) {
            var s = t.abs();
            if (!(s.t <= 0)) {
                var a = this.abs();
                if (a.t < s.t)
                    return null != n && n.fromInt(0),
                    void (null != i && this.copyTo(i));
                null == i && (i = r());
                var o = r()
                  , u = this.s
                  , h = t.s
                  , c = this.DB - l(s[s.t - 1]);
                c > 0 ? (s.lShiftTo(c, o),
                a.lShiftTo(c, i)) : (s.copyTo(o),
                a.copyTo(i));
                var f = o.t
                  , p = o[f - 1];
                if (0 != p) {
                    var d = p * (1 << this.F1) + (f > 1 ? o[f - 2] >> this.F2 : 0)
                      , g = this.FV / d
                      , v = (1 << this.F1) / d
                      , y = 1 << this.F2
                      , m = i.t
                      , x = m - f
                      , S = null == n ? r() : n;
                    for (o.dlShiftTo(x, S),
                    i.compareTo(S) >= 0 && (i[i.t++] = 1,
                    i.subTo(S, i)),
                    e.ONE.dlShiftTo(f, S),
                    S.subTo(o, o); o.t < f; )
                        o[o.t++] = 0;
                    for (; --x >= 0; ) {
                        var w = i[--m] == p ? this.DM : Math.floor(i[m] * g + (i[m - 1] + y) * v);
                        if ((i[m] += o.am(0, w, i, x, 0, f)) < w)
                            for (o.dlShiftTo(x, S),
                            i.subTo(S, i); i[m] < --w; )
                                i.subTo(S, i)
                    }
                    null != n && (i.drShiftTo(f, n),
                    u != h && e.ZERO.subTo(n, n)),
                    i.t = f,
                    i.clamp(),
                    c > 0 && i.rShiftTo(c, i),
                    u < 0 && e.ZERO.subTo(i, i)
                }
            }
        }
        ,
        e.prototype.invDigit = function() {
            if (this.t < 1)
                return 0;
            var t = this[0];
            if (0 == (1 & t))
                return 0;
            var e = 3 & t;
            return (e = (e = (e = (e = e * (2 - (15 & t) * e) & 15) * (2 - (255 & t) * e) & 255) * (2 - ((65535 & t) * e & 65535)) & 65535) * (2 - t * e % this.DV) % this.DV) > 0 ? this.DV - e : -e
        }
        ,
        e.prototype.isEven = function() {
            return 0 == (this.t > 0 ? 1 & this[0] : this.s)
        }
        ,
        e.prototype.exp = function(t, n) {
            if (t > 4294967295 || t < 1)
                return e.ONE;
            var i = r()
              , s = r()
              , a = n.convert(this)
              , o = l(t) - 1;
            for (a.copyTo(i); --o >= 0; )
                if (n.sqrTo(i, s),
                (t & 1 << o) > 0)
                    n.mulTo(s, a, i);
                else {
                    var u = i;
                    i = s,
                    s = u
                }
            return n.revert(i)
        }
        ,
        e.prototype.toString = function(t) {
            if (this.s < 0)
                return "-" + this.negate().toString(t);
            var e;
            if (16 == t)
                e = 4;
            else if (8 == t)
                e = 3;
            else if (2 == t)
                e = 1;
            else if (32 == t)
                e = 5;
            else {
                if (4 != t)
                    return this.toRadix(t);
                e = 2
            }
            var r, n = (1 << e) - 1, i = !1, s = "", a = this.t, o = this.DB - a * this.DB % e;
            if (a-- > 0)
                for (o < this.DB && (r = this[a] >> o) > 0 && (i = !0,
                s = u(r)); a >= 0; )
                    o < e ? (r = (this[a] & (1 << o) - 1) << e - o,
                    r |= this[--a] >> (o += this.DB - e)) : (r = this[a] >> (o -= e) & n,
                    o <= 0 && (o += this.DB,
                    --a)),
                    r > 0 && (i = !0),
                    i && (s += u(r));
            return i ? s : "0"
        }
        ,
        e.prototype.negate = function() {
            var t = r();
            return e.ZERO.subTo(this, t),
            t
        }
        ,
        e.prototype.abs = function() {
            return this.s < 0 ? this.negate() : this
        }
        ,
        e.prototype.compareTo = function(t) {
            var e = this.s - t.s;
            if (0 != e)
                return e;
            var r = this.t;
            if (0 != (e = r - t.t))
                return this.s < 0 ? -e : e;
            for (; --r >= 0; )
                if (0 != (e = this[r] - t[r]))
                    return e;
            return 0
        }
        ,
        e.prototype.bitLength = function() {
            return this.t <= 0 ? 0 : this.DB * (this.t - 1) + l(this[this.t - 1] ^ this.s & this.DM)
        }
        ,
        e.prototype.mod = function(t) {
            var n = r();
            return this.abs().divRemTo(t, null, n),
            this.s < 0 && n.compareTo(e.ZERO) > 0 && t.subTo(n, n),
            n
        }
        ,
        e.prototype.modPowInt = function(t, e) {
            var r;
            return r = t < 256 || e.isEven() ? new f(e) : new p(e),
            this.exp(t, r)
        }
        ,
        e.ZERO = c(0),
        e.ONE = c(1),
        S.prototype.convert = w,
        S.prototype.revert = w,
        S.prototype.mulTo = function(t, e, r) {
            t.multiplyTo(e, r)
        }
        ,
        S.prototype.sqrTo = function(t, e) {
            t.squareTo(e)
        }
        ,
        E.prototype.convert = function(t) {
            if (t.s < 0 || t.t > 2 * this.m.t)
                return t.mod(this.m);
            if (t.compareTo(this.m) < 0)
                return t;
            var e = r();
            return t.copyTo(e),
            this.reduce(e),
            e
        }
        ,
        E.prototype.revert = function(t) {
            return t
        }
        ,
        E.prototype.reduce = function(t) {
            for (t.drShiftTo(this.m.t - 1, this.r2),
            t.t > this.m.t + 1 && (t.t = this.m.t + 1,
            t.clamp()),
            this.mu.multiplyUpperTo(this.r2, this.m.t + 1, this.q3),
            this.m.multiplyLowerTo(this.q3, this.m.t + 1, this.r2); t.compareTo(this.r2) < 0; )
                t.dAddOffset(1, this.m.t + 1);
            for (t.subTo(this.r2, t); t.compareTo(this.m) >= 0; )
                t.subTo(this.m, t)
        }
        ,
        E.prototype.mulTo = function(t, e, r) {
            t.multiplyTo(e, r),
            this.reduce(r)
        }
        ,
        E.prototype.sqrTo = function(t, e) {
            t.squareTo(e),
            this.reduce(e)
        }
        ;
        var b, F, A, P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997], D = (1 << 26) / P[P.length - 1];
        function I() {
            var t;
            t = (new Date).getTime(),
            F[A++] ^= 255 & t,
            F[A++] ^= t >> 8 & 255,
            F[A++] ^= t >> 16 & 255,
            F[A++] ^= t >> 24 & 255,
            A >= H && (A -= H)
        }
        if (e.prototype.chunkSize = function(t) {
            return Math.floor(Math.LN2 * this.DB / Math.log(t))
        }
        ,
        e.prototype.toRadix = function(t) {
            if (null == t && (t = 10),
            0 == this.signum() || t < 2 || t > 36)
                return "0";
            var e = this.chunkSize(t)
              , n = Math.pow(t, e)
              , i = c(n)
              , s = r()
              , a = r()
              , o = "";
            for (this.divRemTo(i, s, a); s.signum() > 0; )
                o = (n + a.intValue()).toString(t).substr(1) + o,
                s.divRemTo(i, s, a);
            return a.intValue().toString(t) + o
        }
        ,
        e.prototype.fromRadix = function(t, r) {
            this.fromInt(0),
            null == r && (r = 10);
            for (var n = this.chunkSize(r), i = Math.pow(r, n), s = !1, a = 0, o = 0, u = 0; u < t.length; ++u) {
                var c = h(t, u);
                c < 0 ? "-" == t.charAt(u) && 0 == this.signum() && (s = !0) : (o = r * o + c,
                ++a >= n && (this.dMultiply(i),
                this.dAddOffset(o, 0),
                a = 0,
                o = 0))
            }
            a > 0 && (this.dMultiply(Math.pow(r, a)),
            this.dAddOffset(o, 0)),
            s && e.ZERO.subTo(this, this)
        }
        ,
        e.prototype.fromNumber = function(t, r, n) {
            if ("number" == typeof r)
                if (t < 2)
                    this.fromInt(1);
                else
                    for (this.fromNumber(t, n),
                    this.testBit(t - 1) || this.bitwiseTo(e.ONE.shiftLeft(t - 1), g, this),
                    this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(r); )
                        this.dAddOffset(2, 0),
                        this.bitLength() > t && this.subTo(e.ONE.shiftLeft(t - 1), this);
            else {
                var i = new Array
                  , s = 7 & t;
                i.length = 1 + (t >> 3),
                r.nextBytes(i),
                s > 0 ? i[0] &= (1 << s) - 1 : i[0] = 0,
                this.fromString(i, 256)
            }
        }
        ,
        e.prototype.bitwiseTo = function(t, e, r) {
            var n, i, s = Math.min(t.t, this.t);
            for (n = 0; n < s; ++n)
                r[n] = e(this[n], t[n]);
            if (t.t < this.t) {
                for (i = t.s & this.DM,
                n = s; n < this.t; ++n)
                    r[n] = e(this[n], i);
                r.t = this.t
            } else {
                for (i = this.s & this.DM,
                n = s; n < t.t; ++n)
                    r[n] = e(i, t[n]);
                r.t = t.t
            }
            r.s = e(this.s, t.s),
            r.clamp()
        }
        ,
        e.prototype.changeBit = function(t, r) {
            var n = e.ONE.shiftLeft(t);
            return this.bitwiseTo(n, r, n),
            n
        }
        ,
        e.prototype.addTo = function(t, e) {
            for (var r = 0, n = 0, i = Math.min(t.t, this.t); r < i; )
                n += this[r] + t[r],
                e[r++] = n & this.DM,
                n >>= this.DB;
            if (t.t < this.t) {
                for (n += t.s; r < this.t; )
                    n += this[r],
                    e[r++] = n & this.DM,
                    n >>= this.DB;
                n += this.s
            } else {
                for (n += this.s; r < t.t; )
                    n += t[r],
                    e[r++] = n & this.DM,
                    n >>= this.DB;
                n += t.s
            }
            e.s = n < 0 ? -1 : 0,
            n > 0 ? e[r++] = n : n < -1 && (e[r++] = this.DV + n),
            e.t = r,
            e.clamp()
        }
        ,
        e.prototype.dMultiply = function(t) {
            this[this.t] = this.am(0, t - 1, this, 0, 0, this.t),
            ++this.t,
            this.clamp()
        }
        ,
        e.prototype.dAddOffset = function(t, e) {
            if (0 != t) {
                for (; this.t <= e; )
                    this[this.t++] = 0;
                for (this[e] += t; this[e] >= this.DV; )
                    this[e] -= this.DV,
                    ++e >= this.t && (this[this.t++] = 0),
                    ++this[e]
            }
        }
        ,
        e.prototype.multiplyLowerTo = function(t, e, r) {
            var n, i = Math.min(this.t + t.t, e);
            for (r.s = 0,
            r.t = i; i > 0; )
                r[--i] = 0;
            for (n = r.t - this.t; i < n; ++i)
                r[i + this.t] = this.am(0, t[i], r, i, 0, this.t);
            for (n = Math.min(t.t, e); i < n; ++i)
                this.am(0, t[i], r, i, 0, e - i);
            r.clamp()
        }
        ,
        e.prototype.multiplyUpperTo = function(t, e, r) {
            --e;
            var n = r.t = this.t + t.t - e;
            for (r.s = 0; --n >= 0; )
                r[n] = 0;
            for (n = Math.max(e - this.t, 0); n < t.t; ++n)
                r[this.t + n - e] = this.am(e - n, t[n], r, 0, 0, this.t + n - e);
            r.clamp(),
            r.drShiftTo(1, r)
        }
        ,
        e.prototype.modInt = function(t) {
            if (t <= 0)
                return 0;
            var e = this.DV % t
              , r = this.s < 0 ? t - 1 : 0;
            if (this.t > 0)
                if (0 == e)
                    r = this[0] % t;
                else
                    for (var n = this.t - 1; n >= 0; --n)
                        r = (e * r + this[n]) % t;
            return r
        }
        ,
        e.prototype.millerRabin = function(t) {
            var n = this.subtract(e.ONE)
              , i = n.getLowestSetBit();
            if (i <= 0)
                return !1;
            var s = n.shiftRight(i);
            (t = t + 1 >> 1) > P.length && (t = P.length);
            for (var a = r(), o = 0; o < t; ++o) {
                a.fromInt(P[Math.floor(Math.random() * P.length)]);
                var u = a.modPow(s, this);
                if (0 != u.compareTo(e.ONE) && 0 != u.compareTo(n)) {
                    for (var h = 1; h++ < i && 0 != u.compareTo(n); )
                        if (0 == (u = u.modPowInt(2, this)).compareTo(e.ONE))
                            return !1;
                    if (0 != u.compareTo(n))
                        return !1
                }
            }
            return !0
        }
        ,
        e.prototype.clone = function() {
            var t = r();
            return this.copyTo(t),
            t
        }
        ,
        e.prototype.intValue = function() {
            if (this.s < 0) {
                if (1 == this.t)
                    return this[0] - this.DV;
                if (0 == this.t)
                    return -1
            } else {
                if (1 == this.t)
                    return this[0];
                if (0 == this.t)
                    return 0
            }
            return (this[1] & (1 << 32 - this.DB) - 1) << this.DB | this[0]
        }
        ,
        e.prototype.byteValue = function() {
            return 0 == this.t ? this.s : this[0] << 24 >> 24
        }
        ,
        e.prototype.shortValue = function() {
            return 0 == this.t ? this.s : this[0] << 16 >> 16
        }
        ,
        e.prototype.signum = function() {
            return this.s < 0 ? -1 : this.t <= 0 || 1 == this.t && this[0] <= 0 ? 0 : 1
        }
        ,
        e.prototype.toByteArray = function() {
            var t = this.t
              , e = new Array;
            e[0] = this.s;
            var r, n = this.DB - t * this.DB % 8, i = 0;
            if (t-- > 0)
                for (n < this.DB && (r = this[t] >> n) != (this.s & this.DM) >> n && (e[i++] = r | this.s << this.DB - n); t >= 0; )
                    n < 8 ? (r = (this[t] & (1 << n) - 1) << 8 - n,
                    r |= this[--t] >> (n += this.DB - 8)) : (r = this[t] >> (n -= 8) & 255,
                    n <= 0 && (n += this.DB,
                    --t)),
                    0 != (128 & r) && (r |= -256),
                    0 == i && (128 & this.s) != (128 & r) && ++i,
                    (i > 0 || r != this.s) && (e[i++] = r);
            return e
        }
        ,
        e.prototype.equals = function(t) {
            return 0 == this.compareTo(t)
        }
        ,
        e.prototype.min = function(t) {
            return this.compareTo(t) < 0 ? this : t
        }
        ,
        e.prototype.max = function(t) {
            return this.compareTo(t) > 0 ? this : t
        }
        ,
        e.prototype.and = function(t) {
            var e = r();
            return this.bitwiseTo(t, d, e),
            e
        }
        ,
        e.prototype.or = function(t) {
            var e = r();
            return this.bitwiseTo(t, g, e),
            e
        }
        ,
        e.prototype.xor = function(t) {
            var e = r();
            return this.bitwiseTo(t, v, e),
            e
        }
        ,
        e.prototype.andNot = function(t) {
            var e = r();
            return this.bitwiseTo(t, y, e),
            e
        }
        ,
        e.prototype.not = function() {
            for (var t = r(), e = 0; e < this.t; ++e)
                t[e] = this.DM & ~this[e];
            return t.t = this.t,
            t.s = ~this.s,
            t
        }
        ,
        e.prototype.shiftLeft = function(t) {
            var e = r();
            return t < 0 ? this.rShiftTo(-t, e) : this.lShiftTo(t, e),
            e
        }
        ,
        e.prototype.shiftRight = function(t) {
            var e = r();
            return t < 0 ? this.lShiftTo(-t, e) : this.rShiftTo(t, e),
            e
        }
        ,
        e.prototype.getLowestSetBit = function() {
            for (var t = 0; t < this.t; ++t)
                if (0 != this[t])
                    return t * this.DB + m(this[t]);
            return this.s < 0 ? this.t * this.DB : -1
        }
        ,
        e.prototype.bitCount = function() {
            for (var t = 0, e = this.s & this.DM, r = 0; r < this.t; ++r)
                t += x(this[r] ^ e);
            return t
        }
        ,
        e.prototype.testBit = function(t) {
            var e = Math.floor(t / this.DB);
            return e >= this.t ? 0 != this.s : 0 != (this[e] & 1 << t % this.DB)
        }
        ,
        e.prototype.setBit = function(t) {
            return this.changeBit(t, g)
        }
        ,
        e.prototype.clearBit = function(t) {
            return this.changeBit(t, y)
        }
        ,
        e.prototype.flipBit = function(t) {
            return this.changeBit(t, v)
        }
        ,
        e.prototype.add = function(t) {
            var e = r();
            return this.addTo(t, e),
            e
        }
        ,
        e.prototype.subtract = function(t) {
            var e = r();
            return this.subTo(t, e),
            e
        }
        ,
        e.prototype.multiply = function(t) {
            var e = r();
            return this.multiplyTo(t, e),
            e
        }
        ,
        e.prototype.divide = function(t) {
            var e = r();
            return this.divRemTo(t, e, null),
            e
        }
        ,
        e.prototype.remainder = function(t) {
            var e = r();
            return this.divRemTo(t, null, e),
            e
        }
        ,
        e.prototype.divideAndRemainder = function(t) {
            var e = r()
              , n = r();
            return this.divRemTo(t, e, n),
            new Array(e,n)
        }
        ,
        e.prototype.modPow = function(t, e) {
            var n, i, s = t.bitLength(), a = c(1);
            if (s <= 0)
                return a;
            n = s < 18 ? 1 : s < 48 ? 3 : s < 144 ? 4 : s < 768 ? 5 : 6,
            i = s < 8 ? new f(e) : e.isEven() ? new E(e) : new p(e);
            var o = new Array
              , u = 3
              , h = n - 1
              , d = (1 << n) - 1;
            if (o[1] = i.convert(this),
            n > 1) {
                var g = r();
                for (i.sqrTo(o[1], g); u <= d; )
                    o[u] = r(),
                    i.mulTo(g, o[u - 2], o[u]),
                    u += 2
            }
            var v, y, m = t.t - 1, x = !0, S = r();
            for (s = l(t[m]) - 1; m >= 0; ) {
                for (s >= h ? v = t[m] >> s - h & d : (v = (t[m] & (1 << s + 1) - 1) << h - s,
                m > 0 && (v |= t[m - 1] >> this.DB + s - h)),
                u = n; 0 == (1 & v); )
                    v >>= 1,
                    --u;
                if ((s -= u) < 0 && (s += this.DB,
                --m),
                x)
                    o[v].copyTo(a),
                    x = !1;
                else {
                    for (; u > 1; )
                        i.sqrTo(a, S),
                        i.sqrTo(S, a),
                        u -= 2;
                    u > 0 ? i.sqrTo(a, S) : (y = a,
                    a = S,
                    S = y),
                    i.mulTo(S, o[v], a)
                }
                for (; m >= 0 && 0 == (t[m] & 1 << s); )
                    i.sqrTo(a, S),
                    y = a,
                    a = S,
                    S = y,
                    --s < 0 && (s = this.DB - 1,
                    --m)
            }
            return i.revert(a)
        }
        ,
        e.prototype.modInverse = function(t) {
            var r = t.isEven();
            if (this.isEven() && r || 0 == t.signum())
                return e.ZERO;
            for (var n = t.clone(), i = this.clone(), s = c(1), a = c(0), o = c(0), u = c(1); 0 != n.signum(); ) {
                for (; n.isEven(); )
                    n.rShiftTo(1, n),
                    r ? (s.isEven() && a.isEven() || (s.addTo(this, s),
                    a.subTo(t, a)),
                    s.rShiftTo(1, s)) : a.isEven() || a.subTo(t, a),
                    a.rShiftTo(1, a);
                for (; i.isEven(); )
                    i.rShiftTo(1, i),
                    r ? (o.isEven() && u.isEven() || (o.addTo(this, o),
                    u.subTo(t, u)),
                    o.rShiftTo(1, o)) : u.isEven() || u.subTo(t, u),
                    u.rShiftTo(1, u);
                n.compareTo(i) >= 0 ? (n.subTo(i, n),
                r && s.subTo(o, s),
                a.subTo(u, a)) : (i.subTo(n, i),
                r && o.subTo(s, o),
                u.subTo(a, u))
            }
            return 0 != i.compareTo(e.ONE) ? e.ZERO : u.compareTo(t) >= 0 ? u.subtract(t) : u.signum() < 0 ? (u.addTo(t, u),
            u.signum() < 0 ? u.add(t) : u) : u
        }
        ,
        e.prototype.pow = function(t) {
            return this.exp(t, new S)
        }
        ,
        e.prototype.gcd = function(t) {
            var e = this.s < 0 ? this.negate() : this.clone()
              , r = t.s < 0 ? t.negate() : t.clone();
            if (e.compareTo(r) < 0) {
                var n = e;
                e = r,
                r = n
            }
            var i = e.getLowestSetBit()
              , s = r.getLowestSetBit();
            if (s < 0)
                return e;
            for (i < s && (s = i),
            s > 0 && (e.rShiftTo(s, e),
            r.rShiftTo(s, r)); e.signum() > 0; )
                (i = e.getLowestSetBit()) > 0 && e.rShiftTo(i, e),
                (i = r.getLowestSetBit()) > 0 && r.rShiftTo(i, r),
                e.compareTo(r) >= 0 ? (e.subTo(r, e),
                e.rShiftTo(1, e)) : (r.subTo(e, r),
                r.rShiftTo(1, r));
            return s > 0 && r.lShiftTo(s, r),
            r
        }
        ,
        e.prototype.isProbablePrime = function(t) {
            var e, r = this.abs();
            if (1 == r.t && r[0] <= P[P.length - 1]) {
                for (e = 0; e < P.length; ++e)
                    if (r[0] == P[e])
                        return !0;
                return !1
            }
            if (r.isEven())
                return !1;
            for (e = 1; e < P.length; ) {
                for (var n = P[e], i = e + 1; i < P.length && n < D; )
                    n *= P[i++];
                for (n = r.modInt(n); e < i; )
                    if (n % P[e++] == 0)
                        return !1
            }
            return r.millerRabin(t)
        }
        ,
        e.prototype.square = function() {
            var t = r();
            return this.squareTo(t),
            t
        }
        ,
        e.prototype.Barrett = E,
        null == F) {
            var B;
            if (F = new Array,
            A = 0,
            "undefined" != typeof window && window.crypto)
                if (window.crypto.getRandomValues) {
                    var C = new Uint8Array(32);
                    for (window.crypto.getRandomValues(C),
                    B = 0; B < 32; ++B)
                        F[A++] = C[B]
                } else if ("Netscape" == navigator.appName && navigator.appVersion < "5") {
                    var T = window.crypto.random(32);
                    for (B = 0; B < T.length; ++B)
                        F[A++] = 255 & T.charCodeAt(B)
                }
            for (; A < H; )
                B = Math.floor(65536 * Math.random()),
                F[A++] = B >>> 8,
                F[A++] = 255 & B;
            A = 0,
            I()
        }
        function R() {
            if (null == b) {
                for (I(),
                (b = new O).init(F),
                A = 0; A < F.length; ++A)
                    F[A] = 0;
                A = 0
            }
            return b.next()
        }
        function N() {}
        function O() {
            this.i = 0,
            this.j = 0,
            this.S = new Array
        }
        N.prototype.nextBytes = function(t) {
            var e;
            for (e = 0; e < t.length; ++e)
                t[e] = R()
        }
        ,
        O.prototype.init = function(t) {
            var e, r, n;
            for (e = 0; e < 256; ++e)
                this.S[e] = e;
            for (r = 0,
            e = 0; e < 256; ++e)
                r = r + this.S[e] + t[e % t.length] & 255,
                n = this.S[e],
                this.S[e] = this.S[r],
                this.S[r] = n;
            this.i = 0,
            this.j = 0
        }
        ,
        O.prototype.next = function() {
            var t;
            return this.i = this.i + 1 & 255,
            this.j = this.j + this.S[this.i] & 255,
            t = this.S[this.i],
            this.S[this.i] = this.S[this.j],
            this.S[this.j] = t,
            this.S[t + this.S[this.i] & 255]
        }
        ;
        var H = 256;
        be={}
        be.exports = {
            default: e,
            BigInteger: e,
            SecureRandom: N
        }
    }

Xe={
    "0": 164970787,
    "1": 197083283,
    "2": 101002067,
    "3": 234271260,
    "4": 268399107,
    "5": 268435455,
    "6": 268435455,
    "7": 268435455,
    "8": 268435454,
    "9": 15,
    "t": 10,
    "s": 0
}
kl=jlk()
ze={}
function generateKeyPairHex(t, e, r) {
    var n = (t ? new Ke(t, e, r) : new kl.e(256, ze)).mod(Xe.subtract(Ke.ONE)).add(Ke.ONE)
        , i = $e(n.toString(16), 64)
        , s = Je.multiply(n);
    return {
        privateKey: i,
        publicKey: "04" + $e(s.getX().toBigInteger().toString(16), 64) + $e(s.getY().toBigInteger().toString(16), 64)
    }
}
generateKeyPairHex()
