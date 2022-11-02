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
	return x * pow(y, mod-2, mod) % mod;
}
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 1e3 + 10;

int n, a[N], b[N];
int dp[N][6*N+1];

void solve() {
	cin >> n;
	int s = 0;
	rep(i, 0, n) cin >> a[i] >> b[i], s += a[i] + b[i];
	rep(i, 0, n) rep(j, 0, 6*n+1) dp[i][j] = INF;
	dp[0][a[0]] = 0, dp[0][b[0]] = 1;
	rep(i, 1, n) rep(j, 0, 6*n+1) {
		if (j-a[i] >= 0) dp[i][j] = min(dp[i][j], dp[i-1][j-a[i]]);
		if (j-b[i] >= 0) dp[i][j] = min(dp[i][j], dp[i-1][j-b[i]] + 1);
	}
	int ans = INF, mins = INF;
	rep(j, 0, 6*n+1) {
		if (dp[n-1][j] != INF) {
			if (abs(j-(s-j)) < mins) mins = abs(j-(s-j)), ans = dp[n-1][j];
			elif (abs(j-(s-j)) == mins) ans = min(ans, dp[n-1][j]);
		}
	}
	cout << ans << endl;
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
