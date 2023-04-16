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
#define ll                  long long
#define i128                __int128
#define ld                  long double
#define ui                  unsigned int
#define ull                 unsigned long long
#define pii                 pair<int, int>
#define pll                 pair<ll, ll>
#define pdd                 pair<ld, ld>
#define vi                  vector<int>
#define vvi                 vector<vector<int>>
#define vll                 vector<ll>
#define vvll                vector<vector<ll>>
#define vpii                vector<pii>
#define vpll                vector<pll>
#define lb                  lower_bound
#define ub                  upper_bound
#define pb                  push_back
#define pf                  push_front
#define eb                  emplace_back
#define fi                  first
#define se                  second
#define overload4(_1, _2, _3, _4, name, ...) name
#define overload3(_1, _2, _3, name, ...) name
#define rep1(n)             for(int i = 0; i < n; ++i)
#define rep2(i, n)          for(int i = 0; i < n; ++i)
#define rep3(i, a, b)       for(int i = a; i < b; ++i)
#define rep4(i, a, b, c)    for(int i = a; i < b; i += c)
#define rep(...)            overload4(__VA_ARGS__, rep4, rep3, rep2, rep1) (__VA_ARGS__)
#define rrep1(n)            for(int i = n; i--; )
#define rrep2(i, n)         for(int i = n; i--; )
#define rrep3(i, a, b)      for(int i = a; i > b; i--)
#define rrep4(i, a, b, c)   for(int i = a; i > b; i -= c)
#define rrep(...)           overload4(__VA_ARGS__, rrep4, rrep3, rrep2, rrep1) (__VA_ARGS__)
#define each1(i, a)         for(auto&& i : a)
#define each2(x, y, a)      for(auto&& [x, y] : a)
#define each3(x, y, z, a)   for(auto&& [x, y, z] : a)
#define each(...)           overload4(__VA_ARGS__, each3, each2, each1) (__VA_ARGS__)
#define FOR_subset(t, s)    for (int t = (s); t >= 0; t = (t == 0 ? -1 : (t - 1) & (s)))
#define len(x)              (int)x.size()
#define elif                else if
#define all1(i)             begin(i), end(i)
#define all2(i, a)          begin(i), begin(i) + a
#define all3(i, a, b)       begin(i) + a, begin(i) + b
#define all(...)            overload3(__VA_ARGS__, all3, all2, all1) (__VA_ARGS__)
#define rall1(i)            rbegin(i), rend(i)
#define rall2(i, a)         rbegin(i), rbegin(i) + a
#define rall3(i, a, b)      rbegin(i) + a, rbegin(i) + b
#define rall(...)           overload3(__VA_ARGS__, rall3, rall2, rall1) (__VA_ARGS__)
#define mst(x, a)           memset(x, a, sizeof(x))
#define lowbit(x)           (x & (-x))
#define bitcnt(x)           (__builtin_popcountll(x))
#define endl                "\n"
#define LB(c, x)            distance((c).begin(), lower_bound(all(c), (x)))
#define UB(c, x)            distance((c).begin(), upper_bound(all(c), (x)))
#define UNIQUE(x)           sort(all(x)), x.erase(unique(all(x)), x.end()), x.shrink_to_fit()
#define SUM(...)            accumulate(all(__VA_ARGS__), 0LL)
#define SORT(a)             sort(all(a))
#define REV(a)              reverse(all(a))
template<class T> auto max(const T& a){ return *max_element(all(a)); }
template<class T> auto min(const T& a){ return *min_element(all(a)); }
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
template <class T> istream &operator>>(istream &in, vector<T> &v) {
    for(auto& x : v) cin >> x;
    return in;
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
template <class T, class S> istream &operator>>(istream &in, pair<T, S> &p) {
    cin >> p.first >> p.second;
    return in;
}
template <class T, class S> ostream &operator<<(ostream &os, const pair<T, S> &p) {
    os << p.first << " " << p.second;
    return os;
}
template <class T, size_t size> istream &operator>>(istream &in, array<T, size> &v) {
    for(auto& x : v) cin >> x;
    return in;
}
template <class T, size_t size> ostream &operator<<(ostream &os, const array<T, size> &v) {
    for(int i = 0; i < size; i++) {
        if(i == 0) os << v[i];
        else os << " " << v[i];
    }
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
void read() {}
template <class Head, class... Tail>
void read(Head &head, Tail &... tail) {
    cin >> head;
    read(tail...);
}
#define INT(...)   \
    int __VA_ARGS__; \
    read(__VA_ARGS__)
#define LL(...)   \
    ll __VA_ARGS__; \
    read(__VA_ARGS__)
#define STR(...)      \
    string __VA_ARGS__; \
    read(__VA_ARGS__)
#define CHAR(...)   \
    char __VA_ARGS__; \
    read(__VA_ARGS__)
#define DBL(...)      \
    double __VA_ARGS__; \
    read(__VA_ARGS__)
#define VEC(type, name, size) \
    vector<type> name(size);    \
    read(name)
#define VV(type, name, h, w)                     \
    vector<vector<type>> name(h, vector<type>(w)); \
    read(name)
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
const int N = 1e5 + 10;

typedef long long LL;
const int p = 1e9 + 7;
int tot, num;
int n, m, r,t,cases=0;

int w[N], a[N], sum1[N * 4], sum2[N * 4], sum3[N * 4], lazy_mul[N * 4], lazy_add[N * 4]; // w[i]=j表示时间戳为i的点的值为j，a[]输入每个节点的值，dat线段树每个点权值，lazy线段树每个点的懒标记
vector<int> mp[N];


void solve(int rt,int len,int a,int b){   //a为add b为mul
    lazy_mul[rt] = 1ll*lazy_mul[rt] * b % p;
    lazy_add[rt] = 1ll*lazy_add[rt] * b % p;
    lazy_add[rt] = ((lazy_add[rt] + a) % p + p) % p;
    if(b!=1){   //先乘后加
        sum1[rt] = 1ll*sum1[rt] * b % p;
        sum2[rt] = (1ll*sum2[rt] * b % p) * b % p;
        sum3[rt] = ((1ll*sum3[rt] * b % p) * b % p) * b % p;
    }
    if(a!=0){
        int a2 = 1ll*a * a % p, a3 = 1ll*a2 * a % p;
        sum3[rt] = ((sum3[rt] + (LL)len * a3 % p) + p) % p;
        sum3[rt] = ((sum3[rt] + 3ll * (LL)sum2[rt] % p * a % p) + p) % p;
        sum3[rt] = ((sum3[rt] + 3ll * (LL)sum1[rt] % p * a2 % p) + p) % p;
        sum2[rt] = ((sum2[rt] + 2ll * (LL)sum1[rt] % p * a % p) + p) % p;
        sum2[rt] = ((sum2[rt] + (LL)len * a2 % p) + p) % p;
        sum1[rt] = ((sum1[rt] + (LL)len * a % p) + p) % p;
    }
}

void pushup(int rt) {
    sum1[rt] = (sum1[rt << 1] + sum1[rt << 1 | 1]) % p;
    sum2[rt] = (sum2[rt << 1] + sum2[rt << 1 | 1]) % p;
    sum3[rt] = (sum3[rt << 1] + sum3[rt << 1 | 1]) % p;
}   

// 建线段树，rt为根，l为rt点管辖的左边界， r为rt点管辖的有边界
void build(int rt, int l, int r)
{
    lazy_add[rt] = 0;
    lazy_mul[rt] = 1;
    if(l==r)
    {
        int temp = a[l];
        sum1[rt] = temp;
        sum2[rt] = (1ll*sum1[rt] * sum1[rt]) % p;
        sum3[rt] = (1ll*sum1[rt] * sum2[rt]) % p;
        return ; 
    }
    int mid=(l + r)>>1; 
    build(rt << 1, l, mid); 
    build(rt << 1 | 1, mid+1, r); 
    pushup(rt);
}

// 下传
void pushdown(int rt, int l, int r)
{
    int mid = (l + r) >> 1;
    solve(rt << 1, mid - l + 1, lazy_add[rt], lazy_mul[rt]);
    solve(rt << 1 | 1, r - mid, lazy_add[rt], lazy_mul[rt]);
    lazy_add[rt] = 0;
    lazy_mul[rt] = 1;
}

// rt为根，l为rt点管辖的左边界， r为rt点管辖的有边界， L为需要修改的左区间，R为需要修改的右区间
void modify(int rt, int l, int r, int L, int R, int a,int b)
{
    if(L <= l && r <= R)
    {
        solve(rt, r - l + 1, a, b);
        return ; 
    } 
    pushdown(rt, l, r); 
    int mid = (l + r)>>1; 
    if(L <= mid) modify(rt << 1, l, mid, L, R, a,b); 
    if(mid < R) modify(rt << 1 | 1, mid + 1, r, L, R, a,b); 
    pushup(rt);
}

// rt为根，l为rt点管辖的左边界， r为rt点管辖的有边界， L为需要查询的左区间，R为查询的右区间,k代表查询的是k次方和
int query(int rt, int l, int r, int L, int R,int k)
{
    if(L <= l && r <= R)
    {
        if(k==1)
            return sum1[rt];
        if(k==2)
            return sum2[rt];
        if(k==3)
            return sum3[rt];
    }
    pushdown(rt, l, r); 
    int mid = (l + r)>>1; 
    int ans = 0; 
    if(L <= mid) ans += query(rt << 1, l, mid, L, R,k), ans %= p; 
    if(mid < R) ans += query(rt << 1 | 1, mid + 1, r, L, R,k), ans %= p;
    pushup(rt);
    return ans; 
}

struct HLD {
    int n;
    std::vector<int> siz, top, dep, parent, in, out, seq;
    std::vector<std::vector<int>> adj;
    int cur;
    
    HLD() {}
    HLD(int n) {
        init(n);
    }
    void init(int n) {
        this->n = n;
        siz.resize(n);
        top.resize(n);
        dep.resize(n);
        parent.resize(n);
        in.resize(n);
        out.resize(n);
        seq.resize(n);
        cur = 0;
        adj.assign(n, {});
    }
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    void work(int root = 0) {
        top[root] = root;
        dep[root] = 0;
        parent[root] = -1;
        dfs1(root);
        dfs2(root);
    }
    void dfs1(int u) {
        if (parent[u] != -1) {
            adj[u].erase(std::find(adj[u].begin(), adj[u].end(), parent[u]));
        }
        
        siz[u] = 1;
        for (auto &v : adj[u]) {
            parent[v] = u;
            dep[v] = dep[u] + 1;
            dfs1(v);
            siz[u] += siz[v];
            if (siz[v] > siz[adj[u][0]]) {
                std::swap(v, adj[u][0]);
            }
        }
    }
    void dfs2(int u) {
        in[u] = cur++;
        seq[in[u]] = u;
        for (auto v : adj[u]) {
            top[v] = v == adj[u][0] ? top[u] : v;
            dfs2(v);
        }
        out[u] = cur;
    }
    int lca(int u, int v) {
        while (top[u] != top[v]) {
            if (dep[top[u]] > dep[top[v]]) {
                u = parent[top[u]];
            } else {
                v = parent[top[v]];
            }
        }
        return dep[u] < dep[v] ? u : v;
    }
    
    int dist(int u, int v) {
        return dep[u] + dep[v] - 2 * dep[lca(u, v)];
    }
    
    int jump(int u, int k) {
        if (dep[u] < k) {
            return -1;
        }
        
        int d = dep[u] - k;
        
        while (dep[top[u]] > d) {
            u = parent[top[u]];
        }
        
        return seq[in[u] - dep[u] + d];
    }
    
    bool isAncester(int u, int v) {
        return in[u] <= in[v] && in[v] < out[u];
    }
    
    int rootedChild(int u, int v) {
        if (u == v) {
            return u;
        }
        if (!isAncester(u, v)) {
            return parent[u];
        }
        auto it = std::upper_bound(adj[u].begin(), adj[u].end(), v, [&](int x, int y) {
            return in[x] < in[y];
        }) - 1;
        return *it;
    }
    
    int rootedSize(int u, int v) {
        if (u == v) {
            return n;
        }
        if (!isAncester(v, u)) {
            return siz[v];
        }
        return n - siz[rootedChild(v, u)];
    }
    
    int rootedLca(int a, int b, int c) {
        return lca(a, b) ^ lca(b, c) ^ lca(c, a);
    }
};

void solve() {
    INT(n, m);
    vvi d(n);
    vi a(n);
    HLD hld(n);
    vector<array<int, 3>> E;
    rep(n-1) {
        INT(x, y, z);
        x--, y--;
        E.pb({x, y, z});
        hld.addEdge(x, y);
    }
    hld.work();
    auto& dep = hld.dep;
    auto& parent = hld.parent;
    auto& top = hld.top;
    auto& in = hld.in;
    auto& out = hld.out;
    each(x, y, z, E) {
        if (dep[x] > dep[y]) swap(x, y);
        modify(1, 1, n, in[y], in[y], z, 1);
    }
    rep(m) {
        INT(op, x, y);
        x--, y--;
        if (op == 1) {
            ll res = 0;
            while (top[x] != top[y]) {
                if (dep[top[x]] < dep[top[y]]) swap(x, y);
                res += query(1, 1, n, in[top[x]], in[x], 2);
                res %= p;
                x = parent[top[x]];
            }
            if (dep[x] > dep[y]) swap(x, y);
            if (in[x] + 1 <= in[y])
                res += query(1, 1, n, in[x] + 1, in[y], 2);
            print(res % p);

        }
        if (op == 2) {
            INT(z);
            while (top[x] != top[y]) {
                if (dep[top[x]] < dep[top[y]]) swap(x, y);
                modify(1, 1, n, in[top[x]], in[x], z, 1);
                x = parent[top[x]];
            }
            if (dep[x] > dep[y]) swap(x, y);
            if (in[x] + 1 <= in[y])
                modify(1, 1, n, in[x] + 1, in[y], z, 1);

        }
        if (op == 3) {
            INT(z);
            while (top[x] != top[y]) {
                if (dep[top[x]] < dep[top[y]]) swap(x, y);
                modify(1, 1, n, in[top[x]], in[x], z, 0);
                x = parent[top[x]];
            }
            if (dep[x] > dep[y]) swap(x, y);
            if (in[x] + 1 <= in[y])
                modify(1, 1, n, in[x] + 1, in[y], z, 0);
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
