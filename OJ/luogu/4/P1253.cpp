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
#define mst(x, a) memset(x,a,sizeof(x))
#ifndef lowbit
#define lowbit(x) (x & (-x))
#endif
#define bitcnt(x) (__builtin_popcountll(x))
#define _up(x) (int)ceil(1.0*x)
#define _down(x) (int)floor(1.0*x)
template <class T>
using pq = priority_queue<T>;
template <class T>
using pqg = priority_queue<T, vector<T>, greater<T>>;
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
const int N = 2e6 + 10;



class SegmentTree {
public:
	struct STNode {
		STNode () : left(nullptr), right(nullptr), val(0), lazy(0), mlazy(LINF) {}
		STNode* left;
		STNode* right;
		ll val;
		ll lazy;
		ll mlazy;
	};
	STNode* root;
	SegmentTree() { root = new STNode(); }
	~SegmentTree() {}

	void assign(STNode* node, int l, int r, int start, int end, ll x) {
		if (l == start && r == end) {
			node->val = 0;
			node->lazy = 0;
			node->mlazy = x;
			return;
		}
		pushdown(node);
		int mid = l+r>>1;
		if (end <= mid) {
			assign(node->left, l, mid, start, end, x);
		} elif (start > mid) {
			assign(node->right, mid+1, r, start, end, x);
		} else {
			assign(node->left, l, mid, start, mid , x);
			assign(node->right, mid+1, r, mid+1, end, x);
		}
		pushup(node, mid-l+1, r-mid);
	}

	void add(STNode* node, int l, int r, int start, int end, ll x){
		if (l == start && r == end) {
			node->lazy += x;
			return;
		}
		pushdown(node);
		int mid = l+r>>1;
		if (end <= mid) {
			add(node->left, l, mid, start, end, x);
		} elif (start > mid) {
			add(node->right, mid+1, r, start, end, x);
		} else {
			add(node->left, l, mid, start, mid , x);
			add(node->right, mid+1, r, mid+1, end, x);
		}
		pushup(node, mid-l+1, r-mid);
	}

	ll query(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->val + node->lazy + (node->mlazy == LINF ? 0 : node->mlazy);
		}
		pushdown(node);
		int mid = l+r>>1;
		ll res;
		if (end <= mid) {
			res = query(node->left, l, mid, start, end);
		} elif (start > mid) {
			res = query(node->right, mid+1, r, start, end);
		} else {
			res = max(query(node->left, l, mid, start, mid),
			query(node->right, mid+1, r, mid+1, end));
		}
		pushup(node, mid-l+1, r-mid);
		return res;
	}

	void pushdown(STNode* node) {
		if (node->left == nullptr) {
			node->left = new STNode();
		}
		if (node->right == nullptr) {
			node->right = new STNode();
		}
		if (node->mlazy != LINF) {
			node->left->lazy = 0;
			node->right->lazy = 0;
			node->left->val = 0;
			node->right->val = 0;
			node->left->mlazy = node->mlazy;
			node->right->mlazy = node->mlazy;
			node->mlazy = LINF;
		}
		if (node->lazy != 0) {
			node->left->lazy += node->lazy;
			node->right->lazy += node->lazy;
			node->lazy = 0;
		}
	}

	void pushup(STNode* node, int ln, int rn) {
		node->val = max(node->left->val + node->left->lazy + (node->left->mlazy == LINF ? 0 : node->left->mlazy),
						node->right->val + node->right->lazy + (node->right->mlazy == LINF ? 0 : node->right->mlazy));

	}
};

SegmentTree st;
void solve() {
	int n, q;
	cin >> n >> q;
	ll x;
	rep(i, 1, n+1) cin >> x, st.assign(st.root, 1, n, i, i, x);
	int op, l, r;
	rep(i, 0, q) {
		cin >> op >> l >> r;
		if (op == 1) cin >> x, st.assign(st.root, 1, n, l, r, x);
		if (op == 2) cin >> x, st.add(st.root, 1, n, l, r, x);
		if (op == 3) cout << st.query(st.root, 1, n, l, r) << "\n";
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
