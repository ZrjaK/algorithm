#ifdef ONLINE_JUDGE
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#include <bits/stdc++.h>
#include <ext/rope>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/hash_policy.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/trie_policy.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;
template <class T> using Tree = tree<T, null_type, less_equal<T>, rb_tree_tag,tree_order_statistics_node_update>;
using Trie = trie<string, null_type, trie_string_access_traits<>, pat_trie_tag, trie_prefix_search_node_update>;
// template <class T> using heapq = __gnu_pbds::priority_queue<T, greater<T>, pairing_heap_tag>;
template <class T> using heapq = std::priority_queue<T, vector<T>, greater<T>>;
#define ll long long
#define i128 __int128
#define ld long double
#define ui unsigned int
#define ull unsigned long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define vi vector<int>
#define vvi vector<vector<int>>
#define vll vector<ll>
#define vvll vector<vector<ll>>
#define vpii vector<pii>
#define vpll vector<pll>
#define lb lower_bound
#define ub upper_bound
#define pb push_back
#define pf push_front
#define eb emplace_back
#define fi first
#define se second
#define rep(i, a, b) for(int i = a; i < b; ++i)
#define per(i, a, b) for(int i = a; i > b; --i)
#define each(x, v) for(auto& x: v)
#define len(x) (int)x.size()
#define elif else if
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define mst(x, a) memset(x, a, sizeof(x))
#define lowbit(x) (x & (-x))
#define bitcnt(x) (__builtin_popcountll(x))
#define endl "\n"
#define MIN(v) *min_element(all(v))
#define MAX(v) *max_element(all(v))
#define UNIQUE(x) sort(all(x)), x.erase(unique(all(x)), x.end()), x.shrink_to_fit()
template <class T> long long SUM(const vector<T> &A) {
    long long sum = 0;
    for (auto &&a: A) sum += a;
    return sum;
}
template <class T> vector<long long> cumsum(vector<T> &A, int off = 1) {
    int N = A.size();
    vector<long long> B(N + 1);
    for (int i = 0; i < N; i++) B[i + 1] = B[i] + A[i];
    if (off == 0) B.erase(B.begin());
    return B;
}
template <class T, class S> inline bool chmax(T &a, const S &b) {
    return (a < b ? a = b, 1 : 0);
}
template <class T, class S> inline bool chmin(T &a, const S &b) {
    return (a > b ? a = b, 1 : 0);
}
mt19937 rng( chrono::steady_clock::now().time_since_epoch().count() );
#define Ran(a, b) rng() % ( (b) - (a) + 1 ) + (a)
struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }

    size_t operator()(pair<uint64_t,uint64_t> x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x.first + FIXED_RANDOM) ^ (splitmix64(x.second + FIXED_RANDOM) >> 1);
    }
};
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
template <class T> ostream &operator<<(ostream &os, const vector<T> &v) {
    for(auto it = begin(v); it != end(v); ++it) {
        if(it == begin(v)) os << *it;
        else os << " " << *it;
    }
    return os;
}
template <class T> ostream &operator<<(ostream &os, const set<T> &v) {
    for(auto it = begin(v); it != end(v); ++it) {
        if(it == begin(v)) os << *it;
        else os << " " << *it;
    }
    return os;
}
template <class T> ostream &operator<<(ostream &os, const multiset<T> &v) {
    for(auto it = begin(v); it != end(v); ++it) {
        if(it == begin(v)) os << *it;
        else os << " " << *it;
    }
    return os;
}
template <class T> ostream &operator<<(ostream &os, const Tree<T> &v) {
    for(auto it = begin(v); it != end(v); ++it) {
        if(it == begin(v)) os << *it;
        else os << " " << *it;
    }
    return os;
}
template <class T, class S> ostream &operator<<(ostream &os, const pair<T, S> &p) {
    os << p.first << " " << p.second;
    return os;
}
inline void print() { std::cout << '\n'; }
template <typename Head, typename... Tail>
inline void print(const Head& head, const Tail &...tails) {
    std::cout << head;
    if (sizeof...(tails)) std::cout << ' ';
    print(tails...);
}
template <typename Iterable>
auto print_all(const Iterable& v, std::string sep = " ", std::string end = "\n") -> decltype(std::cout << *v.begin(), void()) {
    for (auto it = v.begin(); it != v.end();) {
        std::cout << *it;
        if (++it != v.end()) std::cout << sep;
    }
    std::cout << end;
}
ll gcd(ll x, ll y) {
    if(!x) return y;
    if(!y) return x;
    int t = __builtin_ctzll(x | y);
    x >>= __builtin_ctzll(x);
    do {
        y >>= __builtin_ctzll(y);
        if (x > y) swap(x, y);
        y -= x;
    } while (y);
    return x << t;
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
        if (y & 1) res = res * cur % mod;
        cur = ONE * cur * cur % mod;
        y >>= 1;
    }
    return res % mod;
}
ll probabilityMod(ll x, ll y, ll mod) {
    return x * pow(y, mod-2, mod) % mod;
}
vvi getGraph(int n, int m, bool directed = false) {
    vvi res(n);
    rep(_, 0, m) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        res[u].emplace_back(v);
        if(!directed) res[v].emplace_back(u);
    }
    return res;
}
vector<vpii> getWeightedGraph(int n, int m, bool directed = false) {
    vector<vpii> res(n);
    rep(_, 0, m) {
        int u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        res[u].emplace_back(v, w);
        if(!directed) res[v].emplace_back(u, w);
    }
    return res;
}
template <class... Args> auto ndvector(size_t n, Args &&...args) {
    if constexpr (sizeof...(args) == 1) {
        return vector(n, args...);
    } else {
        return vector(n, ndvector(args...));
    }
}
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 1e6 + 10;

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
    int L, R;
	SegmentTree(int _L, int _R) : L(_L), R(_R) { root = new STNode(); }
	~SegmentTree() {}

    void assign(int start, int end, ll x) {
        assert(L <= start && start <= end && end <= R);
        _assign(root, L, R, start, end, x);
    }

	void _assign(STNode* node, int l, int r, int start, int end, ll x) {
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
			_assign(node->left, l, mid, start, end, x);
		} elif (start > mid) {
			_assign(node->right, mid+1, r, start, end, x);
		} else {
			_assign(node->left, l, mid, start, mid , x);
			_assign(node->right, mid+1, r, mid+1, end, x);
		}
		pushup(node, mid-l+1, r-mid);
	}

    void add(int start, int end, ll x) {
        assert(L <= start && start <= end && end <= R);
        _add(root, L, R, start, end, x);
    }

	void _add(STNode* node, int l, int r, int start, int end, ll x){
		if (l == start && r == end) {
			node->lazy += x;
			return;
		}
		pushdown(node);
		int mid = l+r>>1;
		if (end <= mid) {
			_add(node->left, l, mid, start, end, x);
		} elif (start > mid) {
			_add(node->right, mid+1, r, start, end, x);
		} else {
			_add(node->left, l, mid, start, mid , x);
			_add(node->right, mid+1, r, mid+1, end, x);
		}
		pushup(node, mid-l+1, r-mid);
	}

    ll querySum(int start, int end) {
        assert(L <= start && start <= end && end <= R);
        return _querySum(root, L, R, start, end);
    }

	ll _querySum(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->val + node->lazy * (r-l+1) + \
				(node->mlazy == LINF ? 0 : node->mlazy * (r-l+1));
		}
		pushdown(node);
		int mid = l+r>>1;
		ll res;
		if (end <= mid) {
			res = _querySum(node->left, l, mid, start, end);
		} elif (start > mid) {
			res = _querySum(node->right, mid+1, r, start, end);
		} else {
			res = _querySum(node->left, l, mid, start, mid) +
			_querySum(node->right, mid+1, r, mid+1, end);
		}
		pushup(node, mid-l+1, r-mid);
		return res;
	}

    ll queryMax(int start, int end) {
        assert(L <= start && start <= end && end <= R);
        return _queryMax(root, L, R, start, end);
    }

	ll _queryMax(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->maxval + node->lazy + \
				(node->mlazy == LINF ? 0 : node->mlazy);
		}
		pushdown(node);
		int mid = l+r>>1;
		ll res;
		if (end <= mid) {
			res = _queryMax(node->left, l, mid, start, end);
		} elif (start > mid) {
			res = _queryMax(node->right, mid+1, r, start, end);
		} else {
			res = max(_queryMax(node->left, l, mid, start, mid),
			_queryMax(node->right, mid+1, r, mid+1, end));
		}
		pushup(node, mid-l+1, r-mid);
		return res;
	}

    ll queryMin(int start, int end) {
        assert(L <= start && start <= end && end <= R);
        return _queryMin(root, L, R, start, end);
    }

	ll _queryMin(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->minval + node->lazy + \
				(node->mlazy == LINF ? 0 : node->mlazy);
		}
		pushdown(node);
		int mid = l+r>>1;
		ll res;
		if (end <= mid) {
			res = _queryMin(node->left, l, mid, start, end);
		} elif (start > mid) {
			res = _queryMin(node->right, mid+1, r, start, end);
		} else {
			res = min(_queryMin(node->left, l, mid, start, mid),
			_queryMin(node->right, mid+1, r, mid+1, end));
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

void solve() {
    size_t n;
    cin >> n;
    SegmentTree st1(-INF, INF);
    st1.assign(-INF, INF, -INF);
    SegmentTree st2(-INF, INF);
    st2.assign(-INF, INF, INF);
    vll X;
    rep(_, 0, n) {
        int x, y;
        cin >> x >> y;
        st1.assign(x, x, max(st1.queryMax(x, x), y));
        st2.assign(x, x, min(st2.queryMin(x, x), y));
        X.pb(x);
    }
    int q;
    cin >> q;
    rep(_, 0, q) {
        ll a, b;
        cin >> a >> b;
        a--, b--;
        a = X[a];
        b = X[b];
        if (a > b) {
            print(0);
            continue;
        }
        ll mx = st1.queryMax(a, b);
        ll mn = st2.queryMin(a, b);
        print((mx - mn) * (b - a));
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
