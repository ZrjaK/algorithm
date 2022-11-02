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
const int N = 5e3 + 10;

vector<pll> d[N];
deque<int> q;
ll n, m;
ll vis[N];
ll cnt[N];
ll dist[N];

bool spfa(int s) {
	q.pb(s);
	vis[s] = 1, cnt[s]++, dist[s] = 0;
	while (!q.empty()) {
		ll u = q.front();
		q.pop_front();
		vis[u] = 0;
		for(auto& [v, w] : d[u]) {
			if (dist[u] + w < dist[v]) {
				dist[v] = dist[u] + w;
				if (vis[v] == 0) {
					q.pb(v);
					vis[v] = 1, cnt[v]++;
					if (cnt[v] > n) return true;
				}
			}
		}
	}
	return false;
}

void solve() {
	rep(i, 0, N) d[i].clear();
	q.clear();
	mst(vis, 0);
	mst(cnt, 0);
	rep(i, 0, N) dist[i] = LINF;
	cin >> n >> m;
	ll u, v, w;
	rep(i, 0, m) {
		cin >> u >> v >> w;
		d[v].pb({u, w});
	}
	rep(i, 1, n+1) d[0].pb({i, 0});
	if (spfa(0)) { cout << "NO" << endl; return; }
	rep(i, 1, n+1) cout << dist[i] << " ";
	cout << endl;
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
