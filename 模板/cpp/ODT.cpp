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
const int N = 2e5 + 10;

class ODT {
public:
    struct node {
    int l, r;
    mutable ll val;
    bool operator<(const node &a)const {return l < a.l;}
    node(int L, int R, ll Val) : l(L), r(R), val(Val){}
    node(int L): l(L) {}
    };

    set<node> s;
    using si = set<node>::iterator;
    ODT() { s.insert(node(0, 1e9, 0)); }
    ~ODT() {}

    si split(int pos){
        si it = s.lower_bound(node(pos));
        if(it != s.end() && it->l == pos) return it;
        --it;
        int l = it->l, r = it->r;
        ll val = it->val;
        s.erase(it);
        s.insert(node(l, pos-1, val));
        return s.insert(node(pos, r, val)).first;
    }

    void assign(int l,int r,ll val){
        si itr=split(r+1),itl=split(l);
        s.erase(itl,itr);
        s.insert(node(l,r,val));
    }
};

void solve() {
	int n;
	cin >> n;
	rep(i, 0, n) {
	}

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
