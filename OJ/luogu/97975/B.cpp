// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define i128 __int128
#define ld long double
#define ui unsigned int
#define ull unsigned long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define vi vector<int>
#define vvi vector<vector<int> >
#define vll vector<ll>
#define vvll vector<vector<ll> >
#define lb lower_bound
#define ub upper_bound
#define pb push_back
#define pf push_front
#define ppf pop_front
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define rep(i, a, b) for(ll i = a; i < b; ++i)
#define per(i, a, b) for(ll i = a; i > b; --i)
#define each(x, v) for(auto& x: v)
#define len(x) x.size()
#define elif else if
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define mst(x, a) memset(x, a, sizeof(x))
#ifndef lowbit
#define lowbit(x) (x & (-x))
#endif
#define bitcnt(x) (__builtin_popcountll(x))
#define _up(x) (int)ceil(1.0*x)
#define _down(x) (int)floor(1.0*x)
#define endl "\n"
mt19937 rng( chrono::steady_clock::now().time_since_epoch().count() );
#define Ran(a, b) rng() % ( (b) - (a) + 1 ) + (a)
const i128 ONE = 1;
istream &operator>>(istream &in, i128 &x) {
    string s;
    in >> s;
    bool minus = false;
    if (s[0] == '-') {
        minus = true;
        s.erase(s.begin());
    }
    x = 0;
    for (auto i : s) {
        x *= 10;
        x += i - '0';
    }
    if (minus) x = -x;
    return in;
}
ostream &operator<<(ostream &out, i128 x) {
    string s;
    bool minus = false;
    if (x < 0) {
        minus = true;
        x = -x;
    }
    while (x) {
        s.push_back(x % 10 + '0');
        x /= 10;
    }
    if (s.empty()) s = "0";
    if (minus) out << '-';
    reverse(s.begin(), s.end());
    out << s;
    return out;
}
ll gcd(ll x,ll y) {
	if(!x) return y;
	if(!y) return x;
	int t = __builtin_ctzll(x | y);
	x >>= __builtin_ctzll(x);
	do {
		y >>= __builtin_ctzll(y);
		if(x > y) swap(x, y);
		y -= x;
	} while(y);
	return x<<t;
}
ll lcm(ll x, ll y) { return x * y / gcd(x, y); }
ll exgcd(ll a, ll b, ll &x, ll &y) {
    if(!b) return x = 1, y = 0, a;
    ll d = exgcd(b, a % b, x, y);
    ll t = x;
    x = y;
    y = t - a / b * x;
    return d;
}
ll max(ll x, ll y) { return x > y ? x : y; }
ll min(ll x, ll y) { return x < y ? x : y; }
ll Mod(ll x, int mod) { return (x % mod + mod) % mod; }
ll pow(ll x, ll y, ll mod){
	ll res = 1, cur = x;
	while (y) {
		if (y & 1)	res = res * cur % mod;
		cur = ONE * cur * cur % mod;
		y >>= 1;
	}
	return res % mod;
}
ll probabilityMod(ll x, ll y, ll mod) {
	return x * pow(y, mod-2, mod) % mod;
}
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 1e6 + 10;

struct JumpOnTree {
    int n, logn, root = 0;
    vi depth;
    vvi edges, parent;
    JumpOnTree (vvi &e): edges(e), n(len(e)) {
        logn = n > 1 ? __lg(n - 1) + 1 : 0;
        depth = vi(n, -1), depth[root] = 0;
        parent = vvi(logn, vi(n, -1));
        dfs(), doubling();
    };
    JumpOnTree (vvi &e, int rt): edges(e), n(len(e)) {
        root = rt;
        logn = n > 1 ? __lg(n - 1) + 1 : 0;
        depth = vi(n, -1), depth[root] = 0;
        parent = vvi(logn, vi(n, -1));
        dfs(), doubling();
    };
    void dfs() {
        vi q = {root};
        while (!q.empty()) {
            int u = q.back();
            q.pop_back();
            each(v, edges[u]) if (depth[v] == -1) {
                depth[v] = depth[u] + 1;
                parent[0][v] = u;
                q.pb(v);
            }
        }
    }

    void doubling() {
        rep(i, 1, logn) rep(u, 0, n) {
            int p = parent[i - 1][u];
            if (p != -1) parent[i][u] = parent[i - 1][p];
        }
    }

    int lca(int u, int v) {
        int du = depth[u], dv = depth[v];
        if (du > dv) swap(du, dv), swap(u, v);
        int d = dv - du;
        for(int d = dv - du, i = 0; d > 0; d >>= 1, i++) {
            if (d & 1) v = parent[i][v];
        }
        if (u == v) return u;
        int lgn = du > 1 ? __lg(du - 1) + 1 : 0;
        per(i, lgn, -1) {
            int pu = parent[i][u];
            int pv = parent[i][v];
            if (pu != pv) u = pu, v = pv;
        }
        return parent[0][u];
    }

    int jump(int u, int v, int k) {
        if (!k) return u;
        int p = lca(u, v);
        int d1 = depth[u] - depth[p], d2 = depth[v] - depth[p];
        if (d1 + d2 < k) return -1;
        int d;
        if (k <= d1) d = k;
        else u = v, d = d1 + d2 - k;
        for(int i = 0; d > 0; d >>= 1, i++) {
            if (d & 1) u = parent[i][u];
        }
        return u;
    }

    int dist(int u, int v) {
        return depth[u] + depth[v] - 2 * depth[lca(u, v)];
    }
};

void solve() {
    int n, q;
    cin >> n >> q;
    vi a(n);
    each(i, a) cin >> i;
    vvi d(n, vi());
    map<pii, ld> m;
    rep(_, 0, n-1) {
        int x, y;
        ld w;
        cin >> x >> y >> w;
        x--, y--;
        d[x].pb(y), d[y].pb(x);
        m[{x, y}] = w;
        m[{y, x}] = w;
    }
    JumpOnTree tree(d);
    rep(_, 0, q) {
        int x, y;
        cin >> x >> y;
        x--, y--;
        ld t = a[x];
        while(x != y) {
            int nxt = tree.jump(x, y, 1);
            t *= m[{x, nxt}];
            x = nxt;
        }
        if (int(t) == t) cout << "Yes" << endl;
        else cout << "No" << endl;
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