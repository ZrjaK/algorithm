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
#define i128 size_t
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
template <class T, class S> T SUM(const vector<S> &A) {
    T sum = 0;
    for (auto &&a: A) sum += a;
    return sum;
}
template <class T, class S> vector<T> cumsum(vector<S> &A, int off = 1) {
    int N = A.size();
    vector<T> B(N + 1);
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

struct JumpOnTree {
    int n, logn, root = 0;
    vi depth;
    vvi edges, parent;
    JumpOnTree (vvi &e): edges(e), n(len(e)) {
        logn = n > 1 ? __lg(n - 1) + 1 : 0;
        depth = vi(n, -1), depth[root] = 0;
        parent = vvi(logn, vi(n, -1));
        dfs(), doubling();
    };
    JumpOnTree (vvi &e, int rt): edges(e), n(len(e)) {
        root = rt;
        logn = n > 1 ? __lg(n - 1) + 1 : 0;
        depth = vi(n, -1), depth[root] = 0;
        parent = vvi(logn, vi(n, -1));
        dfs(), doubling();
    };
    void dfs() {
        vi q = {root};
        while (!q.empty()) {
            int u = q.back();
            q.pop_back();
            each(v, edges[u]) if (depth[v] == -1) {
                depth[v] = depth[u] + 1;
                parent[0][v] = u;
                q.pb(v);
            }
        }
    }

    void doubling() {
        rep(i, 1, logn) rep(u, 0, n) {
            int p = parent[i - 1][u];
            if (p != -1) parent[i][u] = parent[i - 1][p];
        }
    }

    int lca(int u, int v) {
        int du = depth[u], dv = depth[v];
        if (du > dv) swap(du, dv), swap(u, v);
        int d = dv - du;
        for(int d = dv - du, i = 0; d > 0; d >>= 1, i++) {
            if (d & 1) v = parent[i][v];
        }
        if (u == v) return u;
        int lgn = du > 1 ? __lg(du - 1) + 1 : 0;
        per(i, lgn, -1) {
            int pu = parent[i][u];
            int pv = parent[i][v];
            if (pu != pv) u = pu, v = pv;
        }
        return parent[0][u];
    }

    int jump(int u, int v, int k) {
        if (!k) return u;
        int p = lca(u, v);
        int d1 = depth[u] - depth[p], d2 = depth[v] - depth[p];
        if (d1 + d2 < k) return -1;
        int d;
        if (k <= d1) d = k;
        else u = v, d = d1 + d2 - k;
        for(int i = 0; d > 0; d >>= 1, i++) {
            if (d & 1) u = parent[i][u];
        }
        return u;
    }

    int dist(int u, int v) {
        return depth[u] + depth[v] - 2 * depth[lca(u, v)];
    }
};

gp_hash_table<int, ll, custom_hash> memo[N];


void solve() {
    int n, q;
    cin >> n >> q;
    vll a(n);
    each(i, a) cin >> i;
    vvi d(n);
    vi pa(n, -1);
    rep(i, 1, n) {
        int x;
        cin >> x;
        x--;
        d[x].pb(i);
        d[i].pb(x);
        pa[i] = x;
    }
    vll h(n);
    auto dfs1 = [&] (auto dfs1, int i, int fa) -> void {
        h[i] += a[i] * a[i];
        each(j, d[i]) {
            if (j == fa) continue;
            h[j] += h[i];
            dfs1(dfs1, j, i);
        }
    };
    dfs1(dfs1, 0, -1);
    int sq = sqrt(n);
    JumpOnTree tree(d, 0);
    auto calc = [&] (auto calc, int x, int y, int dep) -> ll {
        if (x == y) return h[x];
        if (memo[x].find(y) != memo[x].end()) return memo[x][y];
        ll res = a[x] * a[y] + calc(calc, pa[x], pa[y], dep-1);
        if (dep > sq) memo[x][y] = memo[y][x] = res;
        return res;
    };
    rep(_, 0, q) {
        int x, y;
        cin >> x >> y;
        x--, y--;
        int L = tree.lca(x, y);
        int d = tree.dist(L, x);
        if (d > sq) {
            cout << calc(calc, x, y, d) << endl;
        }
        else {
            ll ans = 0;
            while (x != y) {
                ans += a[x] * a[y];
                x = pa[x];
                y = pa[y];
            }
            if (x != -1) ans += h[x];
            cout << ans << endl;
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
