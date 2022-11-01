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
const int N = 1e6 + 10;

ll r, c, n, sx, sy;
string arr[50][50];
ll memo[1000][50][50];
vector<pll> h;

ll check(ll i, ll x, ll y) {
	if (i == -1) return x == sx && y == sy;
	if (memo[i][x][y] != -1) return memo[i][x][y];
	ll dx = h[i].fi, dy = h[i].se, tx = x, ty = y;
	ll res = 0;
	while (0<=tx-dx && tx-dx<r && 0<=ty-dy && ty-dy<c && arr[tx-dx][ty-dy] != "X") {
		tx -= dx;
		ty -= dy;
		res += check(i-1, tx, ty);
	}
	memo[i][x][y] = res;
	return res;
}

void solve() {
	mst(memo, -1);
	cin >> r >> c;
	string t;
	rep(i, 0, r) {
		cin >> t;
		rep(j, 0, c) arr[i][j] = t[j];
	}
	cin >> n;
	rep(i, 0, n) {
		cin >> t;
		if (t[0] == 'S') h.pb({1, 0});
		if (t[0] == 'N') h.pb({-1, 0});
		if (t[0] == 'E') h.pb({0, 1});
		if (t[0] == 'W') h.pb({0, -1});
	}
	rep(i, 0, r) rep(j, 0, c) if (arr[i][j] == "*")
		arr[i][j] = '.', sx = i, sy = j;
	rep(i, 0, r) rep(j, 0, c) if (arr[i][j] != "X" && check(n-1, i, j)) arr[i][j] = "*";
	rep(i, 0, r) {
		rep(j, 0, c) cout << arr[i][j];
		cout << endl;
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
