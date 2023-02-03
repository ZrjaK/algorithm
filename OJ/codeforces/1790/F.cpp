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

void solve() {
    int n, c0;
    cin >> n >> c0;
    c0--;
    vi c(n);
    c[0] = c0;
    rep(i, 1, n) cin >> c[i], c[i]--;
    vvi d(n, vi());
    rep(_, 0, n-1) {
        int x, y;
        cin >> x >> y;
        x--, y--;
        d[x].pb(y), d[y].pb(x);
    }
    vi dist(n, INF);
    deque<int> q;
    int t = n - 1;
    function<void(int)> bfs = [&] (int s) {
        dist[s] = 0;
        q.pb(s);
        while (!q.empty()) {
            int i = q.front();
            q.pop_front();
            each(j, d[i]) {
                if (dist[i] + 1 < t && dist[i] + 1 < dist[j]) {
                    dist[j] = dist[i] + 1;
                    q.pb(j);
                }
            }
        }
    };
    bfs(c0);
    vi ans;
    rep(i, 1, n) {
        t = min(t, dist[c[i]]);
        ans.pb(t);
        bfs(c[i]);
    }
    rep(i, 0, n-1) cout << ans[i] << " \n"[i==n-2];
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