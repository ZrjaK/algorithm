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
#define for_subset(t, s) for(ll t = s; t >= 0; t = (t == 0 ? -1 : (t - 1) & s))
#define each(x, v) for(auto& x: v)
#define len(x) x.size()
#define elif else if
#define all(x) begin(x), end(x)
#define mst(x, a) memset(x, a, sizeof(x))
#define MIN(v) *min_element(all(v))
#define MAX(v) *max_element(all(v))
#ifndef lowbit
#define lowbit(x) (x & (-x))
#endif
#define bitcnt(x) (__builtin_popcountll(x))
#define _up(x) (int)ceil(1.0*x)
#define _down(x) (int)floor(1.0*x)
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
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 2e5 + 10;

ld d1, c, d2, p;
int n;
ld h[10][2];
unordered_map<ld, ld> memo[10];

ld dfs(int i, ld rest) {
	if (rest < 0) return INF;
	if (i == n+1) return 0;
	if (memo[i].find(rest) != memo[i].end()) return memo[i][rest];
	ld j = max(rest, (h[i+1][0]-h[i][0]) / d2);
	if (j > c) return INF;
	ld res = INF;
	while (j <= c) {
		res = min(res, (j-rest) * h[i][1] + dfs(i+1, j-(h[i+1][0]-h[i][0])/d2));
		j += 0.03;
	}
	memo[i][rest] = res;
	return res;
}

void solve() {
	mst(h, 0);
	rep(i, 0, 10) memo[i].clear();
	cin >> d1 >> c >> d2 >> p >> n;
	ld x, y;
	h[0][1] = p;
	rep(i, 1, n+1) {
		cin >> x >> y;
		h[i][0] = x;
		h[i][1] = y;
	}
	h[n+1][0] = d1;
	ld res = dfs(0, 0);
	if (res != INF) cout << fixed << setprecision(2) << res;
	else cout << "No Solution";
	cout << endl;
}

signed main() {
    int t = 1;
	// cin >> t;
    while (t--) {
        solve();
    }
	return 0;
}
