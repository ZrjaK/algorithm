#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
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
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 1e5 + 10;

string S;

struct matrix {
	ll m[2][2];
	matrix() { m[0][0] = m[1][1] = 1; m[1][0] = m[0][1] = 0; }
	matrix(ll mtx[][2]) {
		for(int i = 0; i < 2; i++) for(int j = 0; j < 2; j++) 
		    m[i][j] = mtx[i][j];
	}
	matrix operator*(const matrix &x) const {
		matrix ret; memset(ret.m, 0, sizeof ret.m);
		for(int i = 0; i < 2; i++) for(int j = 0; j < 2; j++) for(int k = 0; k < 2; k++) 
		    ret.m[i][j] += m[i][k] * x.m[k][j] % MOD, ret.m[i][j] %= MOD;
		return ret;
	}
};

ll A[2][2] = {{1, 1}, {0, 1}};
ll B[2][2] = {{1, 0}, {1, 1}};

struct node {
    int l, r, tag, flip;
    matrix sum[2];
} st[N << 2];

void pushup(int o) {
    st[o].sum[0] = st[o<<1|1].sum[st[o<<1|1].flip] * st[o<<1].sum[st[o<<1].flip];
    st[o].sum[1] = st[o<<1|1].sum[st[o<<1|1].flip ^ 1] * st[o<<1].sum[st[o<<1].flip ^ 1];
}

void pushdown(int o) {
    if (st[o].flip) st[o<<1].flip ^= 1, st[o<<1|1].flip ^= 1, st[o].flip = 0;
}

void build(int o, int l, int r) {
    st[o].l = l, st[o].r = r, st[o].flip = 0;
    if (l == r) {
        st[o].sum[0] = (S[l] == 'A' ? matrix(A) : matrix(B));
        st[o].sum[1] = (S[l] == 'B' ? matrix(A) : matrix(B));
        return;
    }
    int mid = l + r >> 1;
    build(o << 1, l, mid), build(o << 1 | 1, mid + 1, r);
    pushup(o);
}

void update(int o, int l, int r) {
    if (l <= st[o].l && st[o].r <= r) {
        st[o].flip ^= 1;
        return;
    }
    pushdown(o);
    if (l <= st[o<<1].r) update(o << 1, l, r);
    if (st[o<<1|1].l <= r) update(o << 1 | 1, l, r);
    pushup(o);
}

matrix query(int o, int l, int r) {
    if (l <= st[o].l && st[o].r <= r) return st[o].sum[st[o].flip];
    pushdown(o);
    matrix res;
    if (l <= st[o<<1].r) res = query(o << 1, l, r) * res;
    if (st[o<<1|1].l <= r) res = query(o << 1 | 1, l, r) * res;
    pushup(o);
    return res;
}

void Linear_Transform(ll vec[],ll mtx[][2]){
	ll ret[2]={0,0};
	for(int i=0;i<2;i++) for(int j=0;j<2;j++)
	ret[i]+=vec[j]*mtx[i][j]%MOD,ret[i]%=MOD;
	for(int i=0;i<2;i++) vec[i]=ret[i];
}

void solve() {
    int n, q;
    cin >> n >> q;
    cin >> S;
    build(1, 0, n - 1);
    rep(_, 0, q) {
        int op, l, r, a, b;
        cin >> op >> l >> r;
        l--, r--;
        if (op == 1) update(1, l, r);
        if (op == 2) {
            cin >> a >> b;
            ll vec[2]={a,b};Linear_Transform(vec, query(1, l, r).m);
            cout << vec[0] << " " << vec[1] << endl;
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
