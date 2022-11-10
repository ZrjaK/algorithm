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
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 1e5 + 10;

bool isprime(ll n) {
	if (n <= 1) return false;
	elif (n == 2) return true;
	elif (n % 2 == 0) return false;
	ll A[7] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022};
	ll s = 0, d = n-1;
	while (d % 2 == 0) s++, d >>= 1;
	each(a, A) {
		if (a % n == 0) return true;
		ll x = pow(a, d, n);
		if (x != 1) {
			bool f = true;
			rep(i, 0, s) {
				if (x == n-1) { f = false; break; }
				x = ONE * x * x % n;
			}
			if (f) return false; 
		}
	}
	return true;
}

ll pollard(ll n) {
	if (n % 2 == 0) return 2;
	if (isprime(n)) return n;
	auto f = [&] (ll x) { return (ONE * x * x % n + 1) % n;};
	ll step = 0;
	while(1) {
		step++;
		ll x = step;
		ll y = f(x);
		while(1) {
			ll p = gcd(y - x + n, n);
			if (p == 0 || p == n) break;
			if (p != 1) return p;
			x = f(x);
			y = f(f(y));
		}
	}
}

vll primefact(ll n) {
	if (n == 1) return vll{};
	ll p = pollard(n);
	if (p == n) { return vll{p}; }
	vll left = primefact(p), right = primefact(n / p);
	left.insert(left.end(), all(right));
	sort(all(left));
	return left;
}

void solve() {
	ll n;
	cin >> n;
	if (isprime(n)) { cout << "Prime" << endl; return; }
	vll pfact = primefact(n);
	cout << *(pfact.end()-1) << endl;

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
