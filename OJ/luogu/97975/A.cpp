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

struct UnionFind {
    vi parent, size;
	int part;
	UnionFind (int n) : part(n) {
        parent = vi(n), size = vi(n);
		rep(i, 0, n) parent[i] = i, size[i] = 1;
	};
	~UnionFind() {}

	int find(int i) {
		if (parent[i] != i) {
			parent[i] = find(parent[i]);
		}
		return parent[i];
	}

	void _union(int i, int j) {
		int x = find(i), y = find(j);
		if (x != y) {
			size[y] += size[x];
			parent[x] = parent[y];
			part -= 1;
		}
	}
};


void solve() {
    int n, L, R;
    cin >> n >> L >> R;
    vector<vector<pii>> d(n, vector<pii>());
    rep(i, 0, n-1) {
        int op, u, v, w;
        cin >> op >> u >> v;
        u--, v--;
        if (op == 0) {
            d[u].pb({v, INF});
            d[v].pb({u, INF});
        } else {
            cin >> w;
            d[u].pb({v, w});
            d[v].pb({u, w});
        }
    }
    UnionFind dsu(n);
    rep(i, 0, n) {
        for (auto [j, w] : d[i]) {
            if (w != INF) dsu._union(i, j);
        }
    }
    function<pii(int, int)> dfs = [&] (int i, int fa) {
        int l = L, r = R;
        for (auto [j, w] : d[i]) {
            if (j == fa) continue;
            if (w != INF) {
                auto [lll, rrr] = dfs(j, i);
                l = max(l, w - rrr);
                r = min(r,  w - lll);
            }
        }
        return pii{l, r};
    };
    vll cnt(n, -1);
    ll ans = 1;
    rep(i, 0, n) if(cnt[dsu.find(i)] == -1) {
        auto [l, r] = dfs(dsu.find(i), -1);
        cnt[dsu.find(i)] = max(0, r - l + 1);
        ans = ans * cnt[dsu.find(i)] % MOD;
    }
    cout << ans << endl;
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
