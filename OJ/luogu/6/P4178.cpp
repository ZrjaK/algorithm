// #ifdef ONLINE_JUDGE
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
// #endif
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
#define rep_subset(t, s)    for (int t = (s); t >= 0; t = (t == 0 ? -1 : (t - 1) & (s)))
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
#define sum(...)            accumulate(all(__VA_ARGS__), 0LL)
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
const int N = 1e6 + 10;

template <typename T = int, bool directed = false>
struct Graph {
    int n;
    using cost_type = T;
    using edge_type = tuple<int, int, cost_type, int>;
    vector<vector<pair<int, cost_type>>> g;

    vector<edge_type> edges;
    constexpr bool is_directed() { return directed; }

    Graph(int _n) : n(_n), g(_n) {}

    void add(int u, int v, cost_type cost, int i = -1) {
        assert(0 <= u && u < n && 0 <= v && v < n);
        edges.emplace_back(u, v, cost, i);
    }

    void read_tree() { read_graph(n - 1); }

    void read_graph(int m) {
        for (int i = 0; i < m; i++) {
            int a, b; cin >> a >> b;
            a--, b--;
            T cost; cin >> cost;
            add(a, b, cost, i);
        }
        build();
    }
    
    void build() {
        for (auto&& [u, v, cost, i] : edges) {
            g[u].emplace_back(v, cost);
            if (!directed) g[v].emplace_back(u, cost);
        }
    }

    vector<pair<int, cost_type>> operator[] (int i) {
        return g[i];
    }
};


template <typename GT>
pair<int, int> find_centroids(GT& G) {
    int n = G.n;
    vector<int> parent(n, -1);
    vector<int> sz(n);
    vector<int> q = {0};
    for (int i = 0; i < q.size(); i++) {
        int u = q[i];
        for (auto&& [v, w]: G[u])
        if (v != parent[u]) {
            parent[v] = u;
            q.emplace_back(v);
        }
    }
    for (int i = n - 1; i >= 0; i--) {
        int v = q[i];
        sz[v] += 1;
        int p = parent[v];
        if (p != -1) sz[p] += sz[v];
    }

    int m = n / 2;
    auto check = [&](int u) -> bool {
        if (n - sz[u] > m) return false;
        for (auto&& [v, w]: G[u]) {
            if (v != parent[u] && sz[v] > m) return false;
        }
        return true;
    };
    pair<int, int> ans = {-1, -1};
    for (int i = 0; i < n; i++) if (check(i)) {
        if (ans.first != -1) {
            ans.second = i;
        } else {
            ans.first = i;
        }
    }
    return ans;
}

template <typename GT>
struct Centroid_Decomposition {
    using edge_type = typename GT::edge_type;
    GT& G;
    int n;
    vector<int> sz;
    vector<int> parent;
    vector<int> cdep; // depth in centroid tree

    bool calculated;

    Centroid_Decomposition(GT& G)
        : G(G), n(G.n), sz(G.n), parent(G.n), cdep(G.n, -1) {
        calculated = 0;
        build();
    }

private:
  int find(int u) {
    vector<int> q = {u};
    parent[u] = -1;
    int p = 0;
    while (p < q.size()) {
      int u = q[p++];
      sz[u] = 0;
      for (auto&& [v, w] : G[u]) {
        if (v == parent[u] || cdep[v] != -1) continue;
        parent[v] = u;
        q.emplace_back(v);
      }
    }
    while (q.size()) {
        int u = q.back();
        q.pop_back();
        sz[u] += 1;
        if (p - sz[u] <= p / 2) return u;
        sz[parent[u]] += sz[u];
    }
    return -1;
  }
  void build() {
    assert(!calculated);
    calculated = 1;

    vector<pair<int, int>> st;
    st.emplace_back(0, 0);
    while (!st.empty()) {
        auto [lv, v] = st.back();
        st.pop_back();
        auto c = find(v);
        cdep[c] = lv;
        for (auto&& [to, w] : G[c]) {
            if (cdep[to] == -1) { st.emplace_back(lv + 1, to); }
        }
    }
  }

public:
  // vector of pairs (v, path data v)

  template <typename E, typename F>
  vector<vector<pair<int, E>>> collect(int root, E root_val, F f) {
    vector<vector<pair<int, E>>> res = {{{root, root_val}}};
    for (auto&& [nxt, w] : G[root]) {
      if (cdep[nxt] < cdep[root]) continue;
      vector<pair<int, E>> dat;
      int p = 0;
      dat.eb(nxt, f(root_val, tuple<int, int, E>{root, nxt, w}));
      parent[nxt] = root;
      while (p < len(dat)) {
        auto [u, val] = dat[p++];
        for (auto&& [v, w] : G[u]) {
          if (v == parent[u]) continue;
          if (cdep[v] < cdep[root]) continue;
          parent[v] = u;
          dat.emplace_back(v, f(val, tuple<int, int, E>{u, v, w}));
        }
      }
      res.emplace_back(dat);
      res[0].insert(res[0].end(), dat.begin(), dat.end());
    }
    return res;
  }

  vector<vector<pair<int, int>>> collect_dist(int root) {
    auto f = [&](int x, auto e) -> int { return x + 1; };
    return collect(root, 0, f);
  }

  // (V, H), (V[i] in G) = (i in H).

  // 0,1,2... is a dfs order in H.

  pair<vector<int>, Graph<typename GT::cost_type, true>> get_subgraph(int root) {
    static vector<int> conv;
    while (len(conv) < n) conv.emplace_back(-1);

    vector<int> q;
    using cost_type = typename GT::cost_type;
    vector<tuple<int, int, cost_type>> edges;

    auto dfs = [&](auto& dfs, int u, int p) -> void {
      conv[u] = len(q);
      q.emplace_back(u);
      for (auto&& [v, cost] : G[u]) {
        if (v == p) continue;
        if (cdep[v] < cdep[root]) continue;
        dfs(dfs, v, u);
        edges.emplace_back(conv[u], conv[v], cost);
      }
    };
    dfs(dfs, root, -1);
    int n = len(q);
    Graph<typename GT::cost_type, true> H(n);
    for (auto&& [a, b, c]: edges) H.add(a, b, c);
    H.build();
    for (auto&& v: q) conv[v] = -1;
    return {q, H};
  }
};

void solve() {
    INT(n);
    Graph<int> G(n);
    G.read_tree();
    Centroid_Decomposition cd(G);
    auto f = [&] (int x, auto e) -> int {
        return get<2>(e) + x;
    };
    auto h = ndvector(n, decltype(cd.collect(0, 0, f))());
    rep(i, n) h[i] = cd.collect(i, 0, f);
    INT(k);
    ll ans = 0;
    rep(i, n) {
        Tree<int> S;
        S.insert(0);
        rep(j, 1, len(h[i])) {
            each(x, h[i][j]) ans += S.order_of_key(k - x.se + 1);
            each(x, h[i][j]) S.insert(x.se);
        }
    }
    print(ans);
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
