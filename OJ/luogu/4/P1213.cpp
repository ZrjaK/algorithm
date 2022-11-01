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

ll d[9][9] = {0, 1, 3, 4, -1, -1, -1, -1, -1,
				0, 1, 2, -1, -1, -1, -1, -1, -1,
				1, 2, 4, 5, -1, -1, -1, -1, -1,
				0, 3, 6, -1, -1, -1, -1, -1, -1,
				1, 3, 4, 5, 7, -1, -1, -1, -1,
				2, 5, 8, -1, -1, -1, -1, -1, -1,
				3, 4, 6, 7, -1, -1, -1, -1, -1,
				6, 7, 8, -1, -1, -1, -1, -1, -1,
				4, 5, 7, 8, -1, -1, -1, -1, -1};
ll h[9];

void solve() {
	ll x;
	rep(i, 0, 3) rep(j, 0, 3) cin >> x, h[i*3+j] = x % 12;
	deque<pair<string, ll> > q;
	ll t = 0;
	rep(i, 0, 9) t *= 10, t += h[i];
	q.eb(mp("", t));
	unordered_set<ll> v;
	while (!q.empty()) {
		auto c = q.front();
		q.pop_front();
		string s = c.fi;
		ll t = c.se;
		if (t == 0) {
			rep(i, 0, len(s)) cout << s[i] << " ";
			cout << endl;
			return;
		}
		if (v.find(t) != v.end()) continue;
		v.insert(t);
		ll cc[9];
		per(i, 8, -1) cc[i] = t % 10, t /= 10;
		rep(i, 0, 9) {
			ll f[9];
			rep(j, 0, 9) f[j] = cc[j];
			each(j, d[i]) if (j != -1) f[j] = (f[j] + 3) % 12;
			t = 0;
			rep(j, 0, 9) t *= 10, t += f[j];
			q.pb(mp(s + to_string(i+1), t));
		}

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