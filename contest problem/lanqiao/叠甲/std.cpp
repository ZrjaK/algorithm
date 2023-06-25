#include <bits/stdc++.h>

using namespace std;

template <class S,
          S (*op)(S, S),
          S (*e)()>
struct segtree {
  public:
    segtree() : segtree(0) {}
    segtree(int n) : segtree(std::vector<S>(n, e())) {}
    segtree(const std::vector<S>& v) : _n(int(v.size())) {
        log = 0;
        while ((1 << log) < _n) ++log;
        size = 1 << log;
        d = std::vector<S>(2 * size, e());
        for (int i = 0; i < _n; i++) d[size + i] = v[i];
        for (int i = size - 1; i >= 1; i--) {
            update(i);
        }
    }

    void set(int p, S x) {
        assert(0 <= p && p < _n);
        p += size;
        d[p] = x;
        for (int i = 1; i <= log; i++) update(p >> i);
    }

    S all_prod() { return d[1]; }

  private:
    int _n, size, log;
    std::vector<S> d;

    void update(int k) { d[k] = op(d[2 * k], d[2 * k + 1]); }
};

const int MOD = 1e9 + 7;

struct Info {
    long long a[2][2];
    Info () {
        memset(a, 0, sizeof(a));
        a[0][0] = a[1][1] = 1;
    }

    Info (int x, int f) {
        memset(a, 0, sizeof(a));
        if (f == 0) a[0][0] = x, a[1][0] = a[1][1] = 1;
        else a[0][0] = a[0][1] = 1, a[1][1] = x;
    }
};

Info op(Info a, Info b) {
    Info c;
    memset(c.a, 0, sizeof(c.a));
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                c.a[i][k] = (c.a[i][k] + a.a[i][j] * b.a[j][k]) % MOD;
            }
        }
    }
    return c;
}

Info e() {
    return Info();
}

void solve() {
    long long n, A, B, k1, k2;
    cin >> n >> A >> B >> k1 >> k2;
    string s;
    cin >> s;
    segtree<Info, op, e> seg(n);
    for (int i = 0; i < n; i++) {
        if (s[i] == '0') seg.set(i, Info(k1, 0));
        else seg.set(i, Info(k2, 1));
    }
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int x;
        cin >> x;
        x--;
        if (s[x] == '1') {
            s[x] = '0';
            seg.set(x, Info(k1, 0));
        } else {
            s[x] = '1';
            seg.set(x, Info(k2, 1));
        }
        Info res = seg.all_prod();
        long long a = (res.a[0][0] * A % MOD + res.a[1][0] * B % MOD) % MOD;
        long long b = (res.a[0][1] * A % MOD + res.a[1][1] * B % MOD) % MOD;
        cout << a << " " << b << "\n";
    }
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
