#include <bits/stdc++.h>
using namespace std;
#define ll long long
// #define ll __int128
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
const __int128 ONE = 1;
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
// const int MOD = 1000000007;
const int MOD = 998244353;
const int N = 1e4 + 10;

ll mul[N];
ll inv[N];

void init() {
    mul[0] = 1;
    for (int i = 1; i < N; i++) {
        mul[i] = (mul[i - 1] * i) % MOD;
    }
    inv[0] = inv[1] = 1;
    for (int i = 2; i < N; i++) {
        inv[i] = (ll) (MOD - MOD / i) * inv[MOD % i] % MOD;
    }
    for (int i = 1; i < N; i++) {
        inv[i] = (inv[i - 1] * inv[i]) % MOD;
    }
}

ll C(int n, int m) {
    return n < m ? 0 : mul[n] * inv[m] % MOD * inv[n - m] % MOD;
}

ll P(int n, int m) {
    return n < m ? 0 : mul[n] * inv[n - m] % MOD;
}

ll dp1[N];
ll dp2[N];

void solve() {
	ll n;
	cin >> n;
	ll x;
	ll cnt = 0;
	ll s = 0;
	rep(i, 0, n) {
		cin >> x;
		s += x;
		if (x == -1) cnt++;
	}
	if (s <= 0) {
		cout << C(cnt+1, n-cnt) << endl;
	} else {
		dp2[0] = 1;
		rep(i, 1, n+1) {
			dp1[0] = dp2[1];
			rep(j, 1, s+1) dp1[j] = (dp2[j-1] + dp2[j+1]) % MOD;
			rep(j, 0, s+1) dp2[j] = dp1[j];
		}
		cout << dp1[s] << endl;
	}
}

signed main() {
	init();
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
