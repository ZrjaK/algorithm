#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
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
        if (y & 1) res = res * cur % mod;
        cur = ONE * cur * cur % mod;
        y >>= 1;
    }
    return res % mod;
}
ll probabilityMod(ll x, ll y, ll mod) {
    return x * pow(y, mod-2, mod) % mod;
}
template <class T> ostream &operator<<(ostream &os, const vector<T> &v) {
    for(auto it = begin(v); it != end(v); ++it) {
        if(it == begin(v)) os << *it;
        else os << " " << *it;
    }
    return os;
}
template <class T, class S> ostream &operator<<(ostream &os, const pair<T, S> &p) {
    os << p.first << " " << p.second;
    return os;
}
vvi getGraph(int n, int m, bool directed = false) {
    vvi res(n);
    rep(_, 0, m) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        res[u].emplace_back(v);
        if(!directed) res[v].emplace_back(u);
    }
    return res;
}
vector<vector<pii>> getWeightedGraph(int n, int m, bool directed = false) {
    vector<vector<pii>> res(n);
    rep(_, 0, m) {
        int u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        res[u].emplace_back(v, w);
        if(!directed) res[v].emplace_back(u, w);
    }
    return res;
}
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
// const int N = 1e6 + 10;

const int logN = 32;
struct Linear_Basis {
	ll b[logN];
	// 初始化
	Linear_Basis() {
		memset(b, 0, sizeof b);
	}
	// 插入 x
	bool insert(ll x) {
		for (int i = logN - 1; i >= 0; i--) {
			if (x >> i & 1) {
				if (!b[i]) {
					b[i] = x;
					return true;
				} else {
					x ^= b[i];
				}
			}
		}
		return false;
	}
	// x 与线性基异或的最大值，x=0 时表示线性基能表示出的最大值
	ll qrymx(ll x = 0) {
		for (int i = logN - 1; i >= 0; i--) {
			x = max(x, x ^ b[i]);
		}
		return x;
	}
	void join(Linear_Basis t) {
		for (int i = logN - 1; i >= 0; i--) {
			insert(t.b[i]);
		}
	}
};

void solve() {
    int n;
    cin >> n;
    vll a(n);
    each(i, a) cin >> i;
    vvi d = getGraph(n, n-1);
    int q;
    cin >> q;
    vector<vector<pii>> Q(n);
    rep(i, 0, q) {
        int r, v;
        cin >> r >> v;
        r--, v--;
        Q[r].pb({v, i});
    }
    vector<Linear_Basis> LB(n);
    auto dfs1 = [&] (auto dfs1, int i, int fa) -> void {
        LB[i].insert(a[i]);
        each(j, d[i]) {
            if (j == fa) continue;
            dfs1(dfs1, j, i);
            LB[i].join(LB[j]);
        }
    };
    dfs1(dfs1, 0, -1);
    vll ans(q);
    auto dfs2 = [&] (auto dfs2, int i, int fa) -> void {
        for (auto [j, idx] : Q[i]) {
            ans[idx] = LB[j].qrymx();
        }
        int m = len(d[i]);
        vector<Linear_Basis> pre(m), suf(m);
        rep(j, 0, m) {
            pre[j] = LB[d[i][j]];
            if (j) pre[j].join(pre[j-1]);
        }
        per(j, m-1, -1) {
            suf[j] = LB[d[i][j]];
            if (j != m - 1) suf[j].join(suf[j+1]);
        }
        rep(j, 0, m) {
            int nxt = d[i][j];
            if (nxt == fa) continue;
            LB[i] = Linear_Basis();
            LB[i].insert(a[i]);
            if (j) LB[i].join(pre[j-1]);
            if (j != m - 1) LB[i].join(suf[j+1]);
            auto t = LB[nxt];
            LB[nxt].join(LB[i]);
            dfs2(dfs2, nxt, i);
            LB[nxt] = t;
        }
    };
    dfs2(dfs2, 0, -1);
    each(i, ans) cout << i << endl;

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
