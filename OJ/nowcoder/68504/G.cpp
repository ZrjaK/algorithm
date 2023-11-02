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
template <class T> using pbds_set = tree<T, null_type, less_equal<T>, rb_tree_tag,tree_order_statistics_node_update>;
using Trie = trie<string, null_type, trie_string_access_traits<>, pat_trie_tag, trie_prefix_search_node_update>;
// template <class T> using heapq = __gnu_pbds::priority_queue<T, greater<T>, pairing_heap_tag>;
template <class T> using heapq = std::priority_queue<T, vector<T>, greater<T>>;
using ll   =                long long;
using u32  =                unsigned int;
using u64  =                unsigned long long;
using i128 =                __int128;
using u128 =                __uint128_t;
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
#define vv(type, name, h, ...) \
  vector<vector<type>> name(h, vector<type>(__VA_ARGS__))
#define vvv(type, name, h, w, ...)   \
  vector<vector<vector<type>>> name( \
      h, vector<vector<type>>(w, vector<type>(__VA_ARGS__)))
#define vvvv(type, name, a, b, c, ...)       \
  vector<vector<vector<vector<type>>>> name( \
      a, vector<vector<vector<type>>>(       \
             b, vector<vector<type>>(c, vector<type>(__VA_ARGS__))))
#define lb                  lower_bound
#define ub                  upper_bound
#define pb                  push_back
#define pf                  push_front
#define eb                  emplace_back
#define fi                  first
#define se                  second
#define overload4(_1, _2, _3, _4, name, ...) name
#define overload3(_1, _2, _3, name, ...) name
#define rep1(n)             for(ll _ = 0; _ < n; ++_)
#define rep2(i, n)          for(ll i = 0; i < n; ++i)
#define rep3(i, a, b)       for(ll i = a; i < b; ++i)
#define rep4(i, a, b, c)    for(int i = a; i < b; i += c)
#define rep(...)            overload4(__VA_ARGS__, rep4, rep3, rep2, rep1) (__VA_ARGS__)
#define rrep1(n)            for(ll i = n; i--; )
#define rrep2(i, n)         for(ll i = n; i--; )
#define rrep3(i, a, b)      for(ll i = a; i > b; i--)
#define rrep4(i, a, b, c)   for(ll i = a; i > b; i -= c)
#define rrep(...)           overload4(__VA_ARGS__, rrep4, rrep3, rrep2, rrep1) (__VA_ARGS__)
#define each1(i, a)         for(auto&& i : a)
#define each2(x, y, a)      for(auto&& [x, y] : a)
#define each3(x, y, z, a)   for(auto&& [x, y, z] : a)
#define each(...)           overload4(__VA_ARGS__, each3, each2, each1) (__VA_ARGS__)
#define FOR1(a)             for (ll _ = 0; _ < ll(a); ++_)
#define FOR2(i, a)          for (ll i = 0; i < ll(a); ++i)
#define FOR3(i, a, b)       for (ll i = a; i < ll(b); ++i)
#define FOR4(i, a, b, c)    for (ll i = a; i < ll(b); i += (c))
#define FOR1_R(a)           for (ll i = (a)-1; i >= ll(0); --i)
#define FOR2_R(i, a)        for (ll i = (a)-1; i >= ll(0); --i)
#define FOR3_R(i, a, b)     for (ll i = (b)-1; i >= ll(a); --i)
#define FOR(...)            overload4(__VA_ARGS__, FOR4, FOR3, FOR2, FOR1) (__VA_ARGS__)
#define FOR_R(...)          overload3(__VA_ARGS__, FOR3_R, FOR2_R, FOR1_R) (__VA_ARGS__)
#define FOR_subset(t, s)    for (ll t = (s); t >= 0; t = (t == 0 ? -1 : (t - 1) & (s)))
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
#define MIN(v)              *min_element(all(v))
#define MAX(v)              *max_element(all(v))
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
vector<int> argsort(const vector<T> &A) {
  vector<int> ids(len(A));
  iota(all(ids), 0);
  sort(all(ids),
       [&](int i, int j) { return (A[i] == A[j] ? i < j : A[i] < A[j]); });
  return ids;
}
template <typename T>
vc<T> rearrange(const vc<T> &A, const vc<int> &I) {
  vc<T> B(len(I));
  FOR(i, len(I)) B[i] = A[I[i]];
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
    (check(x) ? ok : ng) = x;
  }
  return ok;
}
template <typename F>
double binary_search_real(F check, double ok, double ng, int iter = 100) {
  while (iter--) {
    double x = (ok + ng) / 2;
    (check(x) ? ok : ng) = x;
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
template <class T> ostream &operator<<(ostream &os, const pbds_set<T> &v) {
    for(auto it = begin(v); it != end(v); ++it) {
        if(it == begin(v)) os << *it;
        else os << " " << *it;
    }
    return os;
}
template <class T, class S> istream &operator>>(istream &in, pair<T, S> &p) {
    in >> p.first >> p.second;
    return in;
}
template <class T, class S> ostream &operator<<(ostream &os, const pair<T, S> &p) {
    os << p.first << " " << p.second;
    return os;
}
template <class T, size_t size> istream &operator>>(istream &in, array<T, size> &v) {
    for(auto& x : v) in >> x;
    return in;
}
template <class T, size_t size> ostream &operator<<(ostream &os, const array<T, size> &v) {
    for(int i = 0; i < size; i++) {
        if(i == 0) os << v[i];
        else os << " " << v[i];
    }
    return os;
}
template <class T> istream &operator>>(istream &in, vector<T> &v) {
    for(auto& x : v) in >> x;
    return in;
}
template <class T> ostream &operator<<(ostream &os, const vector<T> &v) {
    for(auto it = begin(v); it != end(v); ++it) {
        if(it == begin(v)) os << *it;
        else os << " " << *it;
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
const int N = 2e5 + 10;

#line 2 "graph/base.hpp"

template <typename T>
struct Edge {
  int frm, to;
  T cost;
  int id;
};

template <typename T = int, bool directed = false>
struct Graph {
  static constexpr bool is_directed = directed;
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
#line 2 "graph/centroid.hpp"

// (v,w) or (v,-1)

template <typename GT>
pair<int, int> find_centroids(GT& G) {
  static_assert(!GT::is_directed);
  int N = G.N;
  vc<int> par(N, -1);
  vc<int> V(N);
  vc<int> sz(N);
  int l = 0, r = 0;
  V[r++] = 0;
  while (l < r) {
    int v = V[l++];
    for (auto&& e: G[v])
      if (e.to != par[v]) {
        par[e.to] = v;
        V[r++] = e.to;
      }
  }
  FOR_R(i, N) {
    int v = V[i];
    sz[v] += 1;
    int p = par[v];
    if (p != -1) sz[p] += sz[v];
  }

  int M = N / 2;
  auto check = [&](int v) -> bool {
    if (N - sz[v] > M) return false;
    for (auto&& e: G[v]) {
      if (e.to != par[v] && sz[e.to] > M) return false;
    }
    return true;
  };
  pair<int, int> ANS = {-1, -1};
  FOR(v, N) if (check(v)) {
    if (ANS.fi != -1) {
      ANS.se = v;
    } else {
      ANS.fi = v;
    }
  }
  return ANS;
}

template <typename GT>
struct Centroid_Decomposition {
  using edge_type = typename GT::edge_type;
  GT& G;
  int N;
  vc<int> sz;
  vc<int> par;
  vector<int> cdep; // depth in centroid tree

  bool calculated;

  Centroid_Decomposition(GT& G)
      : G(G), N(G.N), sz(G.N), par(G.N), cdep(G.N, -1) {
    calculated = 0;
    build();
  }

private:
  int find(int v) {
    vc<int> V = {v};
    par[v] = -1;
    int p = 0;
    while (p < len(V)) {
      int v = V[p++];
      sz[v] = 0;
      for (auto&& e: G[v]) {
        if (e.to == par[v] || cdep[e.to] != -1) continue;
        par[e.to] = v;
        V.eb(e.to);
      }
    }
    while (len(V)) {
      int v = V.back();
      V.pop_back();
      sz[v] += 1;
      if (p - sz[v] <= p / 2) return v;
      sz[par[v]] += sz[v];
    }
    return -1;
  }
  void build() {
    assert(G.is_prepared());
    assert(!calculated);
    calculated = 1;

    vc<pair<int, int>> st;
    st.eb(0, 0);
    while (!st.empty()) {
      auto [lv, v] = st.back();
      st.pop_back();
      auto c = find(v);
      cdep[c] = lv;
      for (auto&& e: G[c]) {
        if (cdep[e.to] == -1) { st.eb(lv + 1, e.to); }
      }
    }
  }

public:
  // V, dat, indptr

  template <typename T, typename F>
  tuple<vc<int>, vc<T>, vc<int>> collect_path_data(int root, T root_val, F f) {
    vc<int> V = {root};
    vc<T> dp = {root_val};
    vc<int> indptr = {0, 1};
    for (auto&& e: G[root]) {
      int nxt = e.to;
      if (cdep[nxt] < cdep[root]) continue;
      int p = len(V);
      V.eb(nxt);
      dp.eb(f(root_val, e));
      par[nxt] = root;
      while (p < len(V)) {
        int v = V[p];
        T val = dp[p];
        p++;
        for (auto&& e: G[v]) {
          if (e.to == par[v]) continue;
          if (cdep[e.to] < cdep[root]) continue;
          par[e.to] = v;
          V.eb(e.to);
          dp.eb(f(val, e));
        }
      }
      indptr.eb(len(V));
    }
    return {V, dp, indptr};
  }

  // V, dist, indptr

  tuple<vc<int>, vc<int>, vc<int>> collect_dist(int root) {
    auto f = [&](int x, auto e) -> int { return x + 1; };
    return collect_path_data(root, 0, f);
  }

  // (V, H, indptr), (V[i] in G) = (i in H).

  // 0,1,2... is a dfs order in H.

  tuple<vc<int>, Graph<typename GT::cost_type, true>, vc<int>> get_subgraph(
      int root) {
    static vc<int> conv;
    while (len(conv) < N) conv.eb(-1);

    vc<int> V = {root};
    vc<int> indptr = {0, 1};
    conv[root] = 0;
    using cost_type = typename GT::cost_type;
    vc<tuple<int, int, cost_type>> edges;

    auto dfs = [&](auto& dfs, int v, int p) -> void {
      conv[v] = len(V);
      V.eb(v);
      for (auto&& e: G[v]) {
        int to = e.to;
        if (to == p) continue;
        if (cdep[to] < cdep[root]) continue;
        dfs(dfs, to, v);
        edges.eb(conv[v], conv[to], e.cost);
      }
    };
    for (auto&& e: G[root]) {
      if (cdep[e.to] < cdep[root]) continue;
      dfs(dfs, e.to, root);
      edges.eb(conv[root], conv[e.to], e.cost);
      indptr.eb(len(V));
    }
    int n = len(V);
    Graph<typename GT::cost_type, true> H(n);
    for (auto&& [a, b, c]: edges) H.add(a, b, c);
    H.build();
    for (auto&& v: V) conv[v] = -1;
    return {V, H, indptr};
  }
};

#pragma once

// HLD euler tour をとっていろいろ。

template <typename GT>
struct Tree {
  using Graph_type = GT;
  GT &G;
  using WT = typename GT::cost_type;
  int N;
  vector<int> LID, RID, head, V, parent, VtoE;
  vc<int> depth;
  vc<WT> depth_weighted;

  Tree(GT &G, int r = 0, bool hld = 1) : G(G) { build(r, hld); }

  void build(int r = 0, bool hld = 1) {
    if (r == -1) return; // build を遅延したいとき

    N = G.N;
    LID.assign(N, -1), RID.assign(N, -1), head.assign(N, r);
    V.assign(N, -1), parent.assign(N, -1), VtoE.assign(N, -1);
    depth.assign(N, -1), depth_weighted.assign(N, 0);
    assert(G.is_prepared());
    int t1 = 0;
    dfs_sz(r, -1, hld);
    dfs_hld(r, t1);
  }

  void dfs_sz(int v, int p, bool hld) {
    auto &sz = RID;
    parent[v] = p;
    depth[v] = (p == -1 ? 0 : depth[p] + 1);
    sz[v] = 1;
    int l = G.indptr[v], r = G.indptr[v + 1];
    auto &csr = G.csr_edges;
    // 使う辺があれば先頭にする

    for (int i = r - 2; i >= l; --i) {
      if (hld && depth[csr[i + 1].to] == -1) swap(csr[i], csr[i + 1]);
    }
    int hld_sz = 0;
    for (int i = l; i < r; ++i) {
      auto e = csr[i];
      if (depth[e.to] != -1) continue;
      depth_weighted[e.to] = depth_weighted[v] + e.cost;
      VtoE[e.to] = e.id;
      dfs_sz(e.to, v, hld);
      sz[v] += sz[e.to];
      if (hld && chmax(hld_sz, sz[e.to]) && l < i) { swap(csr[l], csr[i]); }
    }
  }

  void dfs_hld(int v, int &times) {
    LID[v] = times++;
    RID[v] += LID[v];
    V[LID[v]] = v;
    bool heavy = true;
    for (auto &&e: G[v]) {
      if (depth[e.to] <= depth[v]) continue;
      head[e.to] = (heavy ? head[v] : e.to);
      heavy = false;
      dfs_hld(e.to, times);
    }
  }

  vc<int> heavy_path_at(int v) {
    vc<int> P = {v};
    while (1) {
      int a = P.back();
      for (auto &&e: G[a]) {
        if (e.to != parent[a] && head[e.to] == v) {
          P.eb(e.to);
          break;
        }
      }
      if (P.back() == a) break;
    }
    return P;
  }

  int heavy_child(int v) {
    int k = LID[v] + 1;
    if (k == N) return -1;
    int w = V[k];
    return (parent[w] == v ? w : -1);
  }

  int e_to_v(int eid) {
    auto e = G.edges[eid];
    return (parent[e.frm] == e.to ? e.frm : e.to);
  }
  int v_to_e(int v) { return VtoE[v]; }

  int ELID(int v) { return 2 * LID[v] - depth[v]; }
  int ERID(int v) { return 2 * RID[v] - depth[v] - 1; }

  // 目標地点へ進む個数が k

  int LA(int v, int k) {
    assert(k <= depth[v]);
    while (1) {
      int u = head[v];
      if (LID[v] - k >= LID[u]) return V[LID[v] - k];
      k -= LID[v] - LID[u] + 1;
      v = parent[u];
    }
  }
  int la(int u, int v) { return LA(u, v); }

  int LCA(int u, int v) {
    for (;; v = parent[head[v]]) {
      if (LID[u] > LID[v]) swap(u, v);
      if (head[u] == head[v]) return u;
    }
  }
  // root を根とした場合の lca

  int LCA_root(int u, int v, int root) {
    return LCA(u, v) ^ LCA(u, root) ^ LCA(v, root);
  }
  int lca(int u, int v) { return LCA(u, v); }
  int lca_root(int u, int v, int root) { return LCA_root(u, v, root); }

  int subtree_size(int v, int root = -1) {
    if (root == -1) return RID[v] - LID[v];
    if (v == root) return N;
    int x = jump(v, root, 1);
    if (in_subtree(v, x)) return RID[v] - LID[v];
    return N - RID[x] + LID[x];
  }

  int dist(int a, int b) {
    int c = LCA(a, b);
    return depth[a] + depth[b] - 2 * depth[c];
  }

  WT dist_weighted(int a, int b) {
    int c = LCA(a, b);
    return depth_weighted[a] + depth_weighted[b] - WT(2) * depth_weighted[c];
  }

  // a is in b

  bool in_subtree(int a, int b) { return LID[b] <= LID[a] && LID[a] < RID[b]; }

  int jump(int a, int b, ll k) {
    if (k == 1) {
      if (a == b) return -1;
      return (in_subtree(b, a) ? LA(b, depth[b] - depth[a] - 1) : parent[a]);
    }
    int c = LCA(a, b);
    int d_ac = depth[a] - depth[c];
    int d_bc = depth[b] - depth[c];
    if (k > d_ac + d_bc) return -1;
    if (k <= d_ac) return LA(a, k);
    return LA(b, d_ac + d_bc - k);
  }

  vc<int> collect_child(int v) {
    vc<int> res;
    for (auto &&e: G[v])
      if (e.to != parent[v]) res.eb(e.to);
    return res;
  }

  vc<pair<int, int>> get_path_decomposition(int u, int v, bool edge) {
    // [始点, 終点] の"閉"区間列。

    vc<pair<int, int>> up, down;
    while (1) {
      if (head[u] == head[v]) break;
      if (LID[u] < LID[v]) {
        down.eb(LID[head[v]], LID[v]);
        v = parent[head[v]];
      } else {
        up.eb(LID[u], LID[head[u]]);
        u = parent[head[u]];
      }
    }
    if (LID[u] < LID[v]) down.eb(LID[u] + edge, LID[v]);
    elif (LID[v] + edge <= LID[u]) up.eb(LID[u], LID[v] + edge);
    reverse(all(down));
    up.insert(up.end(), all(down));
    return up;
  }

  vc<int> restore_path(int u, int v) {
    vc<int> P;
    for (auto &&[a, b]: get_path_decomposition(u, v, 0)) {
      if (a <= b) {
        FOR(i, a, b + 1) P.eb(V[i]);
      } else {
        FOR_R(i, b, a + 1) P.eb(V[i]);
      }
    }
    return P;
  }
};

int phi[N], pfact[N];
// int mobious[N];
vi primes;
vi fact[N];
int init = [] () {
    phi[1] = 1;
    // mobious[1] = 1;
    rep(i, 1, N) {
        if(!phi[i]) {
            primes.pb(i);
            phi[i] = i-1;
            // mobious[i] = -1;
            rep(j, 1, N) {
                if(i * j >= N) break;
                pfact[i*j] = i;
            }
        }
        each(j, primes) {
            if(i * j >= N) break;
            if(i % j == 0) {
                phi[i*j] = phi[i] * j;
                // mobious[i*j] = 0;
                break;
            }
            phi[i*j] = phi[i] * (j - 1);
            // mobious[i*j] = mobious[i] * mobious[j];
        }
        for(int j = i; j < N; j += i) fact[j].pb(i);
    }
    return 0;
} ();

map<int, int> getfact(int x) {
    map<int, int> res;
    while(x != 1) res[pfact[x]]++, x /= pfact[x];
    return res;
}

vi factlist(int x) {
    vi res;
    res.clear();
    res.pb(1);
    while(x != 1) {
        int k = pfact[x];
        int c = 0;
        while(x % k == 0) c++, x /= k;
        vi tmp;
        each(i, res) rep(j, 1, c+1) tmp.pb(i * pow(k, j));
        res.insert(res.end(), all(tmp));
    }
    return res;
}

void solve() {
    INT(n, k);
    k--;
    Graph G(n);
    rep(i, 1, n) {
        INT(p, w);
        p--;
        G.add(i, p, w);
    }
    G.build();
    Tree tree(G);
    Centroid_Decomposition CD(G);
    int ans = -1;
    rep(root, n) {
        auto f = [&](int x, auto e) -> int { return gcd(x, e.cost); };
        auto [V, dp, indptr] = CD.collect_path_data(root, 0, f);
        unordered_map<int, unordered_set<int>> M;
        auto calc = [&] (vi V, vi dp) -> void {
            rep(i, len(V)) {
                int v = V[i];
                int d = tree.dist(root, v);
                if (d < k) each(x, fact[dp[i]]) if (M[k - d].count(x)) chmax(ans, x);
            }
            rep(i, len(V)) {
                int v = V[i];
                int d = tree.dist(root, v);
                if (d == k) chmax(ans, dp[i]);
                if (d < k) each(x, fact[dp[i]]) M[d].insert(x);
            }
        };
        rep(i, 1, len(indptr) - 1) {
            int l = indptr[i], r = indptr[i + 1];
            calc({V.begin() + l, V.begin() + r}, {dp.begin() + l, dp.begin() + r});
        }
    }
    print(ans);

    
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cout << fixed << setprecision(15);
    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
