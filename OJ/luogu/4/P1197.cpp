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
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 1e6 + 10;

int n, m;
vi d[N];
vi h;
int parent[N], _size[N];
int part;

void uf_init(int n) {
    part = n;
    rep(i, 0, n) parent[i] = i, _size[i] = 1;
}

int find(int i) {
    if (parent[i] != i) parent[i] = find(parent[i]);
    return parent[i];
}

void _union(int i, int j) {
    int x = find(i), y = find(j);
    if (x != y) {
        _size[y] += _size[x];
        parent[x] = parent[y];
        part -= 1;
    }
}

void solve() {
	cin >> n >> m;
	int x, y, k;
	rep(i, 0, m) cin >> x >> y, d[x].pb(y), d[y].pb(x);
	cin >> k;
	rep(i, 0, k) cin >> x, h.pb(x);
	unordered_set<int> s(all(h));
	uf_init(n);
	rep(i, 0, n) if (s.find(i) == s.end()) each(j, d[i]) if (s.find(j) == s.end()) _union(i, j);
	vi ans;
	per(i, len(h)-1, -1) {
		ans.pb(part-i-1);
		each(j, d[h[i]]) if (s.find(j) == s.end()) _union(h[i], j);
		s.erase(h[i]);
	}
	ans.pb(part);
	reverse(all(ans));
	each(i, ans) cout << i << endl;
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
