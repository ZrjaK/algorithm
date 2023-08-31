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
using ll   =                long long;
using u32  =                unsigned int;
using u64  =                unsigned long long;
using i128 =                __int128;
using ld   =                long double;
using ui   =                unsigned int;
using ull  =                unsigned long long;
using pii  =                pair<int, int>;
using pll  =                pair<ll, ll>;
using pdd  =                pair<ld, ld>;
using vi   =                vector<int>;
using vvi  =                vector<vector<int>>;
using vll  =                vector<ll>;
using vvll =                vector<vector<ll>>;
using vpii =                vector<pii>;
using vpll =                vector<pll>;
template <class T>
constexpr T infty = 0;
template <>
constexpr int infty<int> = 1'000'000'000;
template <>
constexpr ll infty<ll> = ll(infty<int>) * infty<int> * 2;
template <>
constexpr u32 infty<u32> = infty<int>;
template <>
constexpr u64 infty<u64> = infty<ll>;
template <>
constexpr i128 infty<i128> = i128(infty<ll>) * infty<ll>;
template <>
constexpr double infty<double> = infty<ll>;
template <>
constexpr long double infty<long double> = infty<ll>;
template <class T>
using vc = vector<T>;
template <class T>
using vvc = vector<vc<T>>;
template <class T>
using vvvc = vector<vvc<T>>;
template <class T>
using vvvvc = vector<vvvc<T>>;
template <class T>
using vvvvvc = vector<vvvvc<T>>;
template <class T>
using pq = std::priority_queue<T>;
template <class T>
using pqg = std::priority_queue<T, vector<T>, greater<T>>;
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
#define FOR1(a) for (ll _ = 0; _ < ll(a); ++_)
#define FOR2(i, a) for (ll i = 0; i < ll(a); ++i)
#define FOR3(i, a, b) for (ll i = a; i < ll(b); ++i)
#define FOR4(i, a, b, c) for (ll i = a; i < ll(b); i += (c))
#define FOR1_R(a) for (ll i = (a)-1; i >= ll(0); --i)
#define FOR2_R(i, a) for (ll i = (a)-1; i >= ll(0); --i)
#define FOR3_R(i, a, b) for (ll i = (b)-1; i >= ll(a); --i)
#define overload4(a, b, c, d, e, ...) e
#define overload3(a, b, c, d, ...) d
#define FOR(...) overload4(__VA_ARGS__, FOR4, FOR3, FOR2, FOR1)(__VA_ARGS__)
#define FOR_R(...) overload3(__VA_ARGS__, FOR3_R, FOR2_R, FOR1_R)(__VA_ARGS__)
#define FOR_subset(t, s) \
  for (ll t = (s); t >= 0; t = (t == 0 ? -1 : (t - 1) & (s)))
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
#define bitcnt(x)           (__builtin_popcountll(x))
#define endl                "\n"
#define LB(c, x)            distance((c).begin(), lower_bound(all(c), (x)))
#define UB(c, x)            distance((c).begin(), upper_bound(all(c), (x)))
#define UNIQUE(x)           sort(all(x)), x.erase(unique(all(x)), x.end()), x.shrink_to_fit()
#define SORT(a)             sort(all(a))
#define REV(a)              reverse(all(a))
int popcnt(int x) { return __builtin_popcount(x); }
int popcnt(u32 x) { return __builtin_popcount(x); }
int popcnt(ll x) { return __builtin_popcountll(x); }
int popcnt(u64 x) { return __builtin_popcountll(x); }
// (0, 1, 2, 3, 4) -> (-1, 0, 1, 1, 2)
int topbit(int x) { return (x == 0 ? -1 : 31 - __builtin_clz(x)); }
int topbit(u32 x) { return (x == 0 ? -1 : 31 - __builtin_clz(x)); }
int topbit(ll x) { return (x == 0 ? -1 : 63 - __builtin_clzll(x)); }
int topbit(u64 x) { return (x == 0 ? -1 : 63 - __builtin_clzll(x)); }
// (0, 1, 2, 3, 4) -> (-1, 0, 1, 0, 2)
int lowbit(int x) { return (x == 0 ? -1 : __builtin_ctz(x)); }
int lowbit(u32 x) { return (x == 0 ? -1 : __builtin_ctz(x)); }
int lowbit(ll x) { return (x == 0 ? -1 : __builtin_ctzll(x)); }
int lowbit(u64 x) { return (x == 0 ? -1 : __builtin_ctzll(x)); }
template<class T> auto max(const T& a){ return *max_element(all(a)); }
template<class T> auto min(const T& a){ return *min_element(all(a)); }
template <typename T, typename U>
T ceil(T x, U y) {
    return (x > 0 ? (x + y - 1) / y : x / y);
}
template <typename T, typename U>
T floor(T x, U y) {
    return (x > 0 ? x / y : (x - y + 1) / y);
}
template <typename T, typename U>
pair<T, T> divmod(T x, U y) {
    T q = floor(x, y);
    return {q, x - q * y};
}
template <typename T, typename U>
T SUM(const vector<U> &A) {
    T sum = 0;
    for (auto &&a: A) sum += a;
    return sum;
}
template <typename T, typename U>
vector<T> cumsum(vector<U> &A, int off = 1) {
    int N = A.size();
    vector<T> B(N + 1);
    for (int i = 0; i < N; i++) B[i + 1] = B[i] + A[i];
    if (off == 0) B.erase(B.begin());
    return B;
}
template <typename T>
T POP(deque<T> &que) {
  T a = que.front();
  que.pop_front();
  return a;
}
template <typename T>
T POP(pq<T> &que) {
  T a = que.top();
  que.pop();
  return a;
}
template <typename T>
T POP(pqg<T> &que) {
  assert(!que.empty());
  T a = que.top();
  que.pop();
  return a;
}
template <typename T>
T POP(vc<T> &que) {
  assert(!que.empty());
  T a = que.back();
  que.pop_back();
  return a;
}
template <typename F>
ll binary_search(F check, ll ok, ll ng, bool check_ok = true) {
  if (check_ok) assert(check(ok));
  while (abs(ok - ng) > 1) {
    auto x = (ng + ok) / 2;
    tie(ok, ng) = (check(x) ? make_pair(x, ng) : make_pair(ok, x));
  }
  return ok;
}
template <typename F>
double binary_search_real(F check, double ok, double ng, int iter = 100) {
  while (iter--) {
    double x = (ok + ng) / 2;
    tie(ok, ng) = (check(x) ? make_pair(x, ng) : make_pair(ok, x));
  }
  return (ok + ng) / 2;
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
void YES(bool t = 1) { print(t ? "YES" : "NO"); }
void NO(bool t = 1) { YES(!t); }
void Yes(bool t = 1) { print(t ? "Yes" : "No"); }
void No(bool t = 1) { Yes(!t); }
void yes(bool t = 1) { print(t ? "yes" : "no"); }
void no(bool t = 1) { yes(!t); }
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

#line 2 "graph/bipartite_vertex_coloring.hpp"

#line 2 "graph/base.hpp"

template <typename T>
struct Edge {
  int frm, to;
  T cost;
  int id;
};

template <typename T = int, bool directed = false>
struct Graph {
  int N, M;
  using cost_type = T;
  using edge_type = Edge<T>;
  vector<edge_type> edges;
  vector<int> indptr;
  vector<edge_type> csr_edges;
  vc<int> vc_deg, vc_indeg, vc_outdeg;
  bool prepared;

  class OutgoingEdges {
  public:
    OutgoingEdges(const Graph* G, int l, int r) : G(G), l(l), r(r) {}

    const edge_type* begin() const {
      if (l == r) { return 0; }
      return &G->csr_edges[l];
    }

    const edge_type* end() const {
      if (l == r) { return 0; }
      return &G->csr_edges[r];
    }

  private:
    const Graph* G;
    int l, r;
  };

  bool is_prepared() { return prepared; }
  constexpr bool is_directed() { return directed; }

  Graph() : N(0), M(0), prepared(0) {}
  Graph(int N) : N(N), M(0), prepared(0) {}

  void build(int n) {
    N = n, M = 0;
    prepared = 0;
    edges.clear();
    indptr.clear();
    csr_edges.clear();
    vc_deg.clear();
    vc_indeg.clear();
    vc_outdeg.clear();
  }

  void add(int frm, int to, T cost = 1, int i = -1) {
    assert(!prepared);
    assert(0 <= frm && 0 <= to && to < N);
    if (i == -1) i = M;
    auto e = edge_type({frm, to, cost, i});
    edges.eb(e);
    ++M;
  }

  // wt, off
  void read_tree(bool wt = false, int off = 1) { read_graph(N - 1, wt, off); }

  void read_graph(int M, bool wt = false, int off = 1) {
    for (int m = 0; m < M; ++m) {
      INT(a, b);
      a -= off, b -= off;
      if (!wt) {
        add(a, b);
      } else {
        T c;
        read(c);
        add(a, b, c);
      }
    }
    build();
  }

  void build() {
    assert(!prepared);
    prepared = true;
    indptr.assign(N + 1, 0);
    for (auto&& e: edges) {
      indptr[e.frm + 1]++;
      if (!directed) indptr[e.to + 1]++;
    }
    for (int v = 0; v < N; ++v) { indptr[v + 1] += indptr[v]; }
    auto counter = indptr;
    csr_edges.resize(indptr.back() + 1);
    for (auto&& e: edges) {
      csr_edges[counter[e.frm]++] = e;
      if (!directed)
        csr_edges[counter[e.to]++] = edge_type({e.to, e.frm, e.cost, e.id});
    }
  }

  OutgoingEdges operator[](int v) const {
    assert(prepared);
    return {this, indptr[v], indptr[v + 1]};
  }

  vc<int> deg_array() {
    if (vc_deg.empty()) calc_deg();
    return vc_deg;
  }

  pair<vc<int>, vc<int>> deg_array_inout() {
    if (vc_indeg.empty()) calc_deg_inout();
    return {vc_indeg, vc_outdeg};
  }

  int deg(int v) {
    if (vc_deg.empty()) calc_deg();
    return vc_deg[v];
  }

  int in_deg(int v) {
    if (vc_indeg.empty()) calc_deg_inout();
    return vc_indeg[v];
  }

  int out_deg(int v) {
    if (vc_outdeg.empty()) calc_deg_inout();
    return vc_outdeg[v];
  }

  void debug() {
    print("Graph");
    if (!prepared) {
      print("frm to cost id");
      for (auto&& e: edges) print(e.frm, e.to, e.cost, e.id);
    } else {
      print("indptr", indptr);
      print("frm to cost id");
      FOR(v, N) for (auto&& e: (*this)[v]) print(e.frm, e.to, e.cost, e.id);
    }
  }

  vc<int> new_idx;
  vc<bool> used_e;

  // G における頂点 V[i] が、新しいグラフで i になるようにする
  // {G, es}
  pair<Graph<T, directed>, vc<int>> rearrange(vc<int> V) {
    if (len(new_idx) != N) new_idx.assign(N, -1);
    if (len(used_e) != M) used_e.assign(M, 0);
    int n = len(V);
    FOR(i, n) new_idx[V[i]] = i;
    Graph<T, directed> G(n);
    vc<int> es;
    FOR(i, n) {
      for (auto&& e: (*this)[V[i]]) {
        if (used_e[e.id]) continue;
        int a = e.frm, b = e.to;
        if (new_idx[a] != -1 && new_idx[b] != -1) {
          used_e[e.id] = 1;
          G.add(new_idx[a], new_idx[b], e.cost);
          es.eb(e.id);
        }
      }
    }
    FOR(i, n) new_idx[V[i]] = -1;
    for (auto&& eid: es) used_e[eid] = 0;
    G.build();
    return {G, es};
  }

private:
  void calc_deg() {
    assert(vc_deg.empty());
    vc_deg.resize(N);
    for (auto&& e: edges) vc_deg[e.frm]++, vc_deg[e.to]++;
  }

  void calc_deg_inout() {
    assert(vc_indeg.empty());
    vc_indeg.resize(N);
    vc_outdeg.resize(N);
    for (auto&& e: edges) { vc_indeg[e.to]++, vc_outdeg[e.frm]++; }
  }
};
#line 2 "ds/unionfind/unionfind.hpp"

struct UnionFind {
  int n, n_comp;
  vc<int> dat; // par or (-size)
  UnionFind(int n = 0) { build(n); }

  void build(int m) {
    n = m, n_comp = m;
    dat.assign(n, -1);
  }

  void reset() { build(n); }

  int operator[](int x) {
    while (dat[x] >= 0) {
      int pp = dat[dat[x]];
      if (pp < 0) { return dat[x]; }
      x = dat[x] = pp;
    }
    return x;
  }

  ll size(int x) {
    x = (*this)[x];
    return -dat[x];
  }

  bool merge(int x, int y) {
    x = (*this)[x], y = (*this)[y];
    if (x == y) return false;
    if (-dat[x] < -dat[y]) swap(x, y);
    dat[x] += dat[y], dat[y] = x, n_comp--;
    return true;
  }
};
#line 5 "graph/bipartite_vertex_coloring.hpp"

// 二部グラフでなかった場合には empty

template <typename Graph>
vc<int> bipartite_vertex_coloring(Graph& G) {
  assert(G.is_prepared());

  int n = G.N;
  UnionFind uf(2 * n);
  for (auto&& e: G.edges) {
    int u = e.frm, v = e.to;
    if (e.cost == 0) uf.merge(u, v), uf.merge(u + n, v + n);
    if (e.cost != 0) uf.merge(u + n, v), uf.merge(u, v + n);
  }

  vc<int> color(2 * n, -1);
  FOR(v, n) if (uf[v] == v && color[uf[v]] < 0) {
    color[uf[v]] = 0;
    color[uf[v + n]] = 1;
  }
  FOR(v, n) color[v] = color[uf[v]];
  color.resize(n);
  FOR(v, n) if (uf[v] == uf[v + n]) return {};
  return color;
}
#line 3 "graph/strongly_connected_component.hpp"

template <typename Graph>
pair<int, vc<int>> strongly_connected_component(Graph& G) {
  assert(G.is_directed());
  assert(G.is_prepared());
  int N = G.N;
  int C = 0;
  vc<int> comp(N);
  vc<int> low(N);
  vc<int> ord(N, -1);
  vc<int> visited;
  int now = 0;

  auto dfs = [&](auto self, int v) -> void {
    low[v] = now;
    ord[v] = now;
    ++now;
    visited.eb(v);
    for (auto&& [frm, to, cost, id]: G[v]) {
      if (ord[to] == -1) {
        self(self, to);
        chmin(low[v], low[to]);
      } else {
        chmin(low[v], ord[to]);
      }
    }
    if (low[v] == ord[v]) {
      while (1) {
        int u = visited.back();
        visited.pop_back();
        ord[u] = N;
        comp[u] = C;
        if (u == v) break;
      }
      ++C;
    }
  };
  FOR(v, N) {
    if (ord[v] == -1) dfs(dfs, v);
  }
  FOR(v, N) comp[v] = C - 1 - comp[v];
  return {C, comp};
}

template <typename GT>
Graph<int, 1> scc_dag(GT& G, int C, vc<int>& comp) {
  Graph<int, 1> DAG(C);
  vvc<int> edges(C);
  for (auto&& e: G.edges) {
    int x = comp[e.frm], y = comp[e.to];
    if (x == y) continue;
    edges[x].eb(y);
  }
  FOR(c, C) {
    UNIQUE(edges[c]);
    for (auto&& to: edges[c]) DAG.add(c, to);
  }
  DAG.build();
  return DAG;
}
#line 4 "flow/bipartite.hpp"

template <typename GT>
struct BipartiteMatching {
  int N;
  GT& G;
  vc<int> color;
  vc<int> dist, match;
  vc<int> vis;

  BipartiteMatching(GT& G) : N(G.N), G(G), dist(G.N, -1), match(G.N, -1) {
    if (N == 0) return;
    color = bipartite_vertex_coloring(G);
    assert(!color.empty());
    while (1) {
      bfs();
      vis.assign(N, false);
      int flow = 0;
      FOR(v, N) if (!color[v] && match[v] == -1 && dfs(v))++ flow;
      if (!flow) break;
    }
  }

  BipartiteMatching(GT& G, vc<int> color)
      : N(G.N), G(G), color(color), dist(G.N, -1), match(G.N, -1) {
    while (1) {
      bfs();
      vis.assign(N, false);
      int flow = 0;
      FOR(v, N) if (!color[v] && match[v] == -1 && dfs(v))++ flow;
      if (!flow) break;
    }
  }

  void bfs() {
    dist.assign(N, -1);
    queue<int> que;
    FOR(v, N) if (!color[v] && match[v] == -1) que.emplace(v), dist[v] = 0;
    while (!que.empty()) {
      int v = que.front();
      que.pop();
      for (auto&& e: G[v]) {
        dist[e.to] = 0;
        int w = match[e.to];
        if (w != -1 && dist[w] == -1) dist[w] = dist[v] + 1, que.emplace(w);
      }
    }
  }

  bool dfs(int v) {
    vis[v] = 1;
    for (auto&& e: G[v]) {
      int w = match[e.to];
      if (w == -1 || (!vis[w] && dist[w] == dist[v] + 1 && dfs(w))) {
        match[e.to] = v, match[v] = e.to;
        return true;
      }
    }
    return false;
  }

  vc<pair<int, int>> matching() {
    vc<pair<int, int>> res;
    FOR(v, N) if (v < match[v]) res.eb(v, match[v]);
    return res;
  }

  vc<int> vertex_cover() {
    vc<int> res;
    FOR(v, N) if (color[v] ^ (dist[v] == -1)) { res.eb(v); }
    return res;
  }

  vc<int> independent_set() {
    vc<int> res;
    FOR(v, N) if (!(color[v] ^ (dist[v] == -1))) { res.eb(v); }
    return res;
  }

  vc<int> edge_cover() {
    vc<bool> done(N);
    vc<int> res;
    for (auto&& e: G.edges) {
      if (done[e.frm] || done[e.to]) continue;
      if (match[e.frm] == e.to) {
        res.eb(e.id);
        done[e.frm] = done[e.to] = 1;
      }
    }
    for (auto&& e: G.edges) {
      if (!done[e.frm]) {
        res.eb(e.id);
        done[e.frm] = 1;
      }
      if (!done[e.to]) {
        res.eb(e.id);
        done[e.to] = 1;
      }
    }
    sort(all(res));
    return res;
  }

  /* Dulmage–Mendelsohn decomposition
  https://en.wikipedia.org/wiki/Dulmage%E2%80%93Mendelsohn_decomposition
  http://www.misojiro.t.u-tokyo.ac.jp/~murota/lect-ouyousurigaku/dm050410.pdf
  https://hitonanode.github.io/cplib-cpp/graph/dulmage_mendelsohn_decomposition.hpp.html
  - 最大マッチングとしてありうる iff 同じ W を持つ
  - 辺 uv が必ず使われる：同じ W を持つ辺が唯一
  - color=0 から 1 への辺：W[l] <= W[r]
  - color=0 の点が必ず使われる：W=1,2,...,K
  - color=1 の点が必ず使われる：W=0,1,...,K-1
  */
  pair<int, vc<int>> DM_decomposition() {
    // 非飽和点からの探索

    vc<int> W(N, -1);
    vc<int> que;
    auto add = [&](int v, int x) -> void {
      if (W[v] == -1) {
        W[v] = x;
        que.eb(v);
      }
    };
    FOR(v, N) if (match[v] == -1 && color[v] == 0) add(v, 0);
    FOR(v, N) if (match[v] == -1 && color[v] == 1) add(v, infty<int>);
    while (len(que)) {
      auto v = POP(que);
      if (match[v] != -1) add(match[v], W[v]);
      if (color[v] == 0 && W[v] == 0) {
        for (auto&& e: G[v]) { add(e.to, W[v]); }
      }
      if (color[v] == 1 && W[v] == infty<int>) {
        for (auto&& e: G[v]) { add(e.to, W[v]); }
      }
    }
    // 残った点からなるグラフを作って強連結成分分解

    vc<int> V;
    FOR(v, N) if (W[v] == -1) V.eb(v);
    int n = len(V);
    Graph<bool, 1> DG(n);
    FOR(i, n) {
      int v = V[i];
      if (match[v] != -1) {
        int j = LB(V, match[v]);
        DG.add(i, j);
      }
      if (color[v] == 0) {
        for (auto&& e: G[v]) {
          if (W[e.to] != -1 || e.to == match[v]) continue;
          int j = LB(V, e.to);
          DG.add(i, j);
        }
      }
    }
    DG.build();
    auto [K, comp] = strongly_connected_component(DG);
    K += 1;
    // 答

    FOR(i, n) { W[V[i]] = 1 + comp[i]; }
    FOR(v, N) if (W[v] == infty<int>) W[v] = K;
    return {K, W};
  }

  void debug() {
    print("match", match);
    print("min vertex covor", vertex_cover());
    print("max indep set", independent_set());
    print("min edge cover", edge_cover());
  }
};
#line 4 "graph/bipartite_edge_coloring.hpp"

struct RegularBipartiteColoring {
  using P = pair<int, int>;
  int N, M;
  vc<P> edges;

  vvc<int> solve(int n, int k, vc<P> G) {
    N = n;
    M = len(G);
    edges = G;
    vc<int> A(M);
    iota(all(A), 0);
    return solve_inner(M / N, A);
  }

  vvc<int> solve_inner(int k, vc<int> A) {
    return (k % 2 == 0 ? solve_even(k, A) : solve_odd(k, A));
  }

  vvc<int> solve_even(int k, vc<int> A) {
    assert(k % 2 == 0);
    if (k == 0) return {};
    // 2^m <= k < 2^{m+1}
    int m = 0;
    while (1 << (m + 1) <= k) ++m;
    vvc<int> res;
    if (k != 1 << m) {
      auto [B, C] = split(k, A);
      auto dat = solve_inner(k / 2, C);
      FOR(j, k - (1 << m)) { res.eb(dat[j]); }
      FOR(j, k - (1 << m), len(dat)) {
        for (auto&& idx: dat[j]) B.eb(idx);
      }
      k = 1 << m;
      swap(A, B);
    }
    auto dfs = [&](auto& dfs, int K, vc<int> A) -> void {
      if (K == 1) {
        res.eb(A);
        return;
      }
      auto [B, C] = split(k, A);
      dfs(dfs, K / 2, B);
      dfs(dfs, K / 2, C);
    };
    dfs(dfs, k, A);
    return res;
  }

  vvc<int> solve_odd(int k, vc<int> A) {
    assert(k % 2 == 1);
    if (k == 1) { return {A}; }
    vc<bool> match = matching(k, A);
    vc<int> B;
    B.reserve(len(A) - N);
    vc<int> es;
    FOR(i, len(A)) {
      if (match[i]) es.eb(A[i]);
      if (!match[i]) B.eb(A[i]);
    }
    vvc<int> res = solve_inner(k - 1, B);
    res.eb(es);
    return res;
  }

  vc<bool> matching(int k, vc<int> A) {
    Graph<bool, 0> G(N + N);
    vc<int> color(N + N);
    FOR(v, N) color[v] = 0;
    for (auto&& eid: A) {
      auto [a, b] = edges[eid];
      G.add(a, b);
    }
    G.build();
    BipartiteMatching<decltype(G)> BM(G);
    auto& match = BM.match;
    vc<bool> res(len(A));
    FOR(i, len(A)) {
      auto idx = A[i];
      auto [a, b] = edges[idx];
      if (match[a] == b) {
        match[a] = -1;
        res[i] = 1;
      }
    }
    return res;
  }

  pair<vc<int>, vc<int>> split(int k, vc<int> A) {
    assert(k % 2 == 0);
    // 2 つの k/2 - regular に分割する。
    int n = len(A);
    vc<bool> rest(n);
    vc<int> A0, A1;
    A0.reserve(n / 2), A1.reserve(n / 2);
    vvc<P> G(N + N);
    FOR(i, n) {
      rest[i] = 1;
      auto [a, b] = edges[A[i]];
      G[a].eb(i, b);
      G[b].eb(i, a);
    }
    auto dfs = [&](auto& dfs, int v, int color) -> void {
      while (len(G[v])) {
        auto [i, to] = POP(G[v]);
        if (!rest[i]) continue;
        rest[i] = 0;
        if (color == 0) A0.eb(A[i]);
        if (color == 1) A1.eb(A[i]);
        dfs(dfs, to, 1 ^ color);
      }
    };
    FOR(v, N) dfs(dfs, v, 0);
    return {A0, A1};
  }
};

template <typename GT>
pair<int, vc<int>> bipartite_edge_coloring(GT& G) {
  auto vcolor = bipartite_vertex_coloring<decltype(G)>(G);
  auto deg = G.deg_array();
  int D = max(deg);

  UnionFind uf(G.N);
  FOR(c, 2) {
    pqg<pair<int, int>> que;
    FOR(v, G.N) {
      if (vcolor[v] == c) que.emplace(deg[v], v);
    }
    while (len(que) > 1) {
      auto [d1, v1] = POP(que);
      auto [d2, v2] = POP(que);
      if (d1 + d2 > D) break;
      uf.merge(v1, v2);
      int r = uf[v1];
      que.emplace(d1 + d2, r);
    }
  }

  vc<int> LV, RV;
  FOR(v, G.N) if (uf[v] == v) {
    if (vcolor[v] == 0) LV.eb(v);
    if (vcolor[v] == 1) RV.eb(v);
  }
  int X = max(len(LV), len(RV));
  vc<int> degL(X), degR(X);

  vc<pair<int, int>> edges;
  for (auto&& e: G.edges) {
    int a = e.frm, b = e.to;
    a = uf[a], b = uf[b];
    a = LB(LV, a);
    b = LB(RV, b);
    degL[a]++, degR[b]++;
    edges.eb(a, X + b);
  }
  int p = 0, q = 0;
  while (p < X && q < X) {
    if (degL[p] == D) {
      ++p;
      continue;
    }
    if (degR[q] == D) {
      ++q;
      continue;
    }
    edges.eb(p, X + q);
    degL[p]++, degR[q]++;
  }
  RegularBipartiteColoring RBC;
  vvc<int> res = RBC.solve(X, D, edges);
  vc<int> ecolor(len(edges));
  FOR(i, len(res)) {
    for (auto&& j: res[i]) ecolor[j] = i;
  }
  ecolor.resize(G.M);
  return {D, ecolor};
}

void solve() {
    INT(n, m);
    VV(int, a, n, m);
    each(lst, a) each(i, lst) i--;
    Graph G(2 * n);
    rep(i, n) rep(j, m) G.add(i, a[i][j] + n);
    G.build();
    auto [nc, color] = bipartite_edge_coloring<decltype(G)>(G);
    auto ans = ndvector(n, m, 0);
    each(e, G.edges) {
        int row = e.frm, val = e.to, col = color[e.id];
        ans[row][col] = val + 1 - n;
    }
    Yes();
    each(i, ans) print(i);
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
