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
template <class T>
using pq = priority_queue<T>;
template <class T>
using pqg = priority_queue<T, vector<T>, greater<T> >;
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
const int N = 2e5 + 10;

struct e {
    int u, v, w;
    bool operator<(const e& o) const { 
        return w < o.w;
    }
} h[N];

void solve() {
    int n, m;
    cin >> n >> m;
    int u, v, w;
    rep(i, 0, m) {
        cin >> u >> v >> w;
        u--, v--;
        h[i] = {u, v, w};
    }
    sort(h, h + m);
    function<int(int x)> check = [&] (int x) {
        vi d[n];
        rep(i, 0, x) {
            u = h[i].u, v = h[i].v;
            d[u].pb(v);
            d[v].pb(u);
        }
        rep(i, x, m) {
            u = h[i].u, v = h[i].v;
            d[u].pb(v);
        }
        int index = 0, scc_cnt = 0;
        vi dfn(n, 0), low(n, 0), sccno(n, 0);
        stack<int> q;
        function<void(int)> tarjan = [&] (int i) {
            dfn[i] = low[i] = ++index;
            q.push(i);
            each(j, d[i]) {
                if (!dfn[j]) {
                    tarjan(j);
                    low[i] = min(low[i], low[j]);
                } elif (!sccno[j]) {
                    low[i] = min(low[i], dfn[j]);
                }
            }
            if(low[i] == dfn[i]) {
                scc_cnt++;
                while (1) {
                    x = q.top(), q.pop();
                    sccno[x] = scc_cnt;
                    if(x == i) break;
                }
            }
        };
        rep(i, 0, n) if (!dfn[i]) tarjan(i);
        vi vis(n, 0);
        function<void(int)> dfs = [&] (int i) {
            vis[i] = 1;
            each(j, d[i]) if (!vis[j]) dfs(j);
        };
        rep(i, 0, n) if (sccno[i] == scc_cnt) {
            dfs(i);
            break;
        }
        rep(i, 0, n) if (!vis[i]) return 0;
        return 1;
    };
    int l = -1, r = m + 1;
    while (l + 1 < r) {
        int mid = l + r >> 1;
        if (check(mid)) r = mid;
        else l = mid;
    }
    if (r == 0) cout << 0 << endl;
    elif (r == m + 1) cout << -1 << endl;
    else cout << h[r-1].w << endl;
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
