#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define i128 __int128
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
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define mst(x, a) memset(x, a, sizeof(x))
#ifndef lowbit
#define lowbit(x) (x & (-x))
#endif
#define bitcnt(x) (__builtin_popcountll(x))
#define _up(x) (int)ceil(1.0*x)
#define _down(x) (int)floor(1.0*x)
// #define endl "\n"
mt19937 rng( chrono::steady_clock::now().time_since_epoch().count() );
#define Ran(a, b) rng() % ( (b) - (a) + 1 ) + (a)
template <class T>
using pq = priority_queue<T>;
template <class T>
using pqg = priority_queue<T, vector<T>, greater<T> >;
const i128 ONE = 1;
istream &operator>>(istream &in, i128 &x) {
    string s;
    in >> s;
    bool minus = false;
    if (s[0] == '-') {
        minus = true;
        s.erase(s.begin());
    }
    x = 0;
    for (auto i : s) {
        x *= 10;
        x += i - '0';
    }
    if (minus) x = -x;
    return in;
}
ostream &operator<<(ostream &out, i128 x) {
    string s;
    bool minus = false;
    if (x < 0) {
        minus = true;
        x = -x;
    }
    while (x) {
        s.push_back(x % 10 + '0');
        x /= 10;
    }
    if (s.empty()) s = "0";
    if (minus) out << '-';
    reverse(s.begin(), s.end());
    out << s;
    return out;
}
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
ll exgcd(ll a, ll b, ll &x, ll &y) {
    if(!b) return x = 1, y = 0, a;
    ll d = exgcd(b, a % b, x, y);
    ll t = x;
    x = y;
    y = t - a / b * x;
    return d;
}
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
const int N = 2e5 + 10;

class SegmentTree {
public:
	struct STNode {
		STNode () : left(nullptr), right(nullptr), val(0), maxval(0), minval(0), lazy(0), mlazy(LINF) {}
		STNode* left;
		STNode* right;
		ll val;
		ll maxval;
		ll minval;
		ll lazy;
		ll mlazy;
	};
	STNode* root;
	SegmentTree() { root = new STNode(); }
	~SegmentTree() {}

	void assign(STNode* node, int l, int r, int start, int end, ll x) {
		if (l == start && r == end) {
			node->val = 0;
			node->maxval = 0;
			node->minval = 0;
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

	ll querySum(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->val + node->lazy * (r-l+1) + \
				(node->mlazy == LINF ? 0 : node->mlazy * (r-l+1));
		}
		pushdown(node);
		int mid = l+r>>1;
		ll res;
		if (end <= mid) {
			res = querySum(node->left, l, mid, start, end);
		} elif (start > mid) {
			res = querySum(node->right, mid+1, r, start, end);
		} else {
			res = querySum(node->left, l, mid, start, mid) +
			querySum(node->right, mid+1, r, mid+1, end);
		}
		pushup(node, mid-l+1, r-mid);
		return res;
	}

	ll queryMax(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->maxval + node->lazy + \
				(node->mlazy == LINF ? 0 : node->mlazy);
		}
		pushdown(node);
		int mid = l+r>>1;
		ll res;
		if (end <= mid) {
			res = queryMax(node->left, l, mid, start, end);
		} elif (start > mid) {
			res = queryMax(node->right, mid+1, r, start, end);
		} else {
			res = max(queryMax(node->left, l, mid, start, mid),
			queryMax(node->right, mid+1, r, mid+1, end));
		}
		pushup(node, mid-l+1, r-mid);
		return res;
	}

	ll queryMin(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->minval + node->lazy + \
				(node->mlazy == LINF ? 0 : node->mlazy);
		}
		pushdown(node);
		int mid = l+r>>1;
		ll res;
		if (end <= mid) {
			res = queryMin(node->left, l, mid, start, end);
		} elif (start > mid) {
			res = queryMin(node->right, mid+1, r, start, end);
		} else {
			res = min(queryMin(node->left, l, mid, start, mid),
			queryMin(node->right, mid+1, r, mid+1, end));
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
			node->left->val = 0;
			node->left->maxval = 0;
			node->left->minval = 0;
		
			node->right->lazy = 0;
			node->right->val = 0;
			node->right->maxval = 0;
			node->right->minval = 0;
			
			node->left->mlazy = node->mlazy;
			node->right->mlazy = node->mlazy;
			node->mlazy = LINF;
		}
		if (node->lazy) {
			node->left->lazy += node->lazy;
			node->right->lazy += node->lazy;
			node->lazy = 0;
		}
	}

	void pushup(STNode* node, int ln, int rn) {
		node->val = node->left->val + node->left->lazy * ln + \
					(node->left->mlazy == LINF ? 0 : node->left->mlazy * ln) + \ 
					node->right->val + node->right->lazy * rn + \
					(node->right->mlazy == LINF ? 0 : node->right->mlazy * rn);

		node->maxval = max(node->left->maxval + node->left->lazy + \
						(node->left->mlazy == LINF ? 0 : node->left->mlazy),
						node->right->maxval + node->right->lazy + \
						(node->right->mlazy == LINF ? 0 : node->right->mlazy));

		node->minval = min(node->left->minval + node->left->lazy + \
						(node->left->mlazy == LINF ? 0 : node->left->mlazy),
						node->right->minval + node->right->lazy + \
						(node->right->mlazy == LINF ? 0 : node->right->mlazy));

	}
};

SegmentTree st;
int memo[N];

int ask(int l, int r) {
    if(memo[r] != -1) return memo[r] + st.querySum(st.root, 0, N, r, r);
    cout << "? " << l << " " << r << endl;
    cin >> memo[r];
    st.assign(st.root, 0, N, r, r, 0);
    return memo[r];
}

void solve() {
    mst(memo, -1);
    int n, t, k;
    cin >> n >> t;
    rep(_, 0, t) {
        cin >> k;
        int l = 0, r = n + 1;
        while(l + 1 < r) {
            int mid = l + r >> 1;
            int res = ask(1, mid);
            if(res <= mid - k) r = mid;
            else l = mid;
        }
        cout << "! " << r << endl;
        st.add(st.root, 0, N, r, N, 1);
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
