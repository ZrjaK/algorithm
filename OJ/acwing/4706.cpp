#include <bits/stdc++.h>
using namespace std;
#define ll long long
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
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define rep(i, a, b) for(int i = a; i < b; ++i)
#define per(i, a, b) for(int i = a; i > b; --i)
#define each(x, v) for(auto& x: v)
#define len(x) x.size()
#define elif else if
#define all(x) begin(x), end(x)
#define mst(x, a) memset(x, a, sizeof(x))
#ifndef lowbit
#define lowbit(x) (x & (-x))
#endif
#define bitcnt(x) (__builtin_popcountll(x))
#define _up(x) (int)ceil(1.0*x)
#define _down(x) (int)floor(1.0*x)
#define endl "\n"
template <class T>
using pq = priority_queue<T>;
template <class T>
using pqg = priority_queue<T, vector<T>, greater<T> >;
ll gcd(ll x, ll y) { return !y ? x : gcd(y, x%y); }
ll lcm(ll x, ll y) { return x * y / gcd(x, y); }
ll max(ll x, ll y) { return x > y ? x : y; }
ll min(ll x, ll y) { return x < y ? x : y; }
ll Mod(ll x, int mod) { return (x % mod + mod) % mod; }
ll pow(ll x, ll y, ll mod){
	ll res = 1, cur = x;
	while (y) {
		if (y & 1)	res = res*cur % mod;
		cur = cur * cur % mod;
		y >>= 1;
	}
	return res % mod;
}
ll probabilityMod(ll x, ll y, ll mod) {
	return x * pow(y % mod, mod-2, mod) % mod;
}
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 2e5 + 10;

int n;
vector<pii> d[N];
ll dp[N][2];

void dfs(int i, int fa) {
	vector<pii> h;
	for(auto& [j, w]: d[i]) {
		if (j == fa) continue;
		dfs(j, i);
		h.pb({j, w});
	}
	if (len(h) == 0) dp[i][0] = dp[i][1] = 0;
	elif (len(h) == 1) {int j = h[0].fi, w = h[0].se; dp[i][0] = w + dp[j][0];}
	else {
		ll t = 0;
		for(auto& [j, w]: h) t += dp[j][1] + w * 2;
		for(auto& [j, w]: h) dp[i][0] = min(dp[i][0], t - dp[j][1] - w + dp[j][0]);
	}
	ll t = 0;
	for(auto& [j, w]: h) t += dp[j][1] + w * 2;
	dp[i][1] = t;
}

void solve() {
	cin >> n;
	rep(i, 1, n+1) rep(j, 0, 2) dp[i][j] = LINF;
	int x, y, w;
	rep(i, 0, n-1) cin >> x >> y >> w, d[x].pb({y, w}), d[y].pb({x, w});
	dfs(1, -1);
	cout << dp[1][0] << endl;

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
