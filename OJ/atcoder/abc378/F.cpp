#ifdef ONLINE_JUDGE
#pragma GCC optimize("Ofast,unroll-loops")
// #pragma GCC target("avx2,popcnt")
#endif
#include <bits/stdc++.h>
using namespace std;
using ll   =                long long;
using u32  =                unsigned int;
using u64  =                unsigned long long;
using i128 =                __int128;
using u128 =                __uint128_t;
using f128 =                __float128;
using ld   =                long double;
using pii  =                pair<int, int>;
using pll  =                pair<ll, ll>;
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
#define eb                  emplace_back
#define fi                  first
#define se                  second
#define mp                  make_pair
#define mt                  make_tuple
#define stoi                stoll
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
#define len(x)              ll(x.size())
#define elif                else if
#define all1(i)             begin(i), end(i)
#define all2(i, a)          begin(i), begin(i) + a
#define all3(i, a, b)       begin(i) + a, begin(i) + b
#define all(...)            overload3(__VA_ARGS__, all3, all2, all1) (__VA_ARGS__)
#define rall1(i)            rbegin(i), rend(i)
#define rall2(i, a)         rbegin(i), rbegin(i) + a
#define rall3(i, a, b)      rbegin(i) + a, rbegin(i) + b
#define rall(...)           overload3(__VA_ARGS__, rall3, rall2, rall1) (__VA_ARGS__)
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
int popcnt_mod_2(int x) { return __builtin_parity(x); }
int popcnt_mod_2(u32 x) { return __builtin_parity(x); }
int popcnt_mod_2(ll x) { return __builtin_parityll(x); }
int popcnt_mod_2(u64 x) { return __builtin_parityll(x); }
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
T bmod(T x, U y) {
    return x - y * floor(x, y);
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
template <typename T, typename... Vectors>
void concat(vc<T> &first, const Vectors &... others) {
  vc<T> &res = first;
  (res.insert(res.end(), others.begin(), others.end()), ...);
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
template <class T, class S>
inline bool chmax(T &a, const S &b) {
  return (a < b ? a = b, 1 : 0);
}
template <class T, class S>
inline bool chmin(T &a, const S &b) {
  return (a > b ? a = b, 1 : 0);
}
// ? は -1
vc<int> s_to_vi(const string &S, char first_char) {
  vc<int> A(S.size());
  FOR(i, S.size()) { A[i] = (S[i] != '?' ? S[i] - first_char : -1); }
  return A;
}
#define FASTIO
#include <unistd.h>


// https://judge.yosupo.jp/submission/21623

namespace fastio {
static constexpr uint32_t SZ = 1 << 17;
char ibuf[SZ];
char obuf[SZ];
char out[100];
// pointer of ibuf, obuf

uint32_t pil = 0, pir = 0, por = 0;

struct Pre {
  char num[10000][4];
  constexpr Pre() : num() {
    for (int i = 0; i < 10000; i++) {
      int n = i;
      for (int j = 3; j >= 0; j--) {
        num[i][j] = n % 10 | '0';
        n /= 10;
      }
    }
  }
} constexpr pre;

inline void load() {
  memcpy(ibuf, ibuf + pil, pir - pil);
  pir = pir - pil + fread(ibuf + pir - pil, 1, SZ - pir + pil, stdin);
  pil = 0;
  if (pir < SZ) ibuf[pir++] = '\n';
}

inline void flush() {
  fwrite(obuf, 1, por, stdout);
  por = 0;
}

void rd(char &c) {
  do {
    if (pil + 1 > pir) load();
    c = ibuf[pil++];
  } while (isspace(c));
}

void rd(string &x) {
  x.clear();
  char c;
  do {
    if (pil + 1 > pir) load();
    c = ibuf[pil++];
  } while (isspace(c));
  do {
    x += c;
    if (pil == pir) load();
    c = ibuf[pil++];
  } while (!isspace(c));
}

template <typename T>
void rd_real(T &x) {
  string s;
  rd(s);
  x = stod(s);
}

template <typename T>
void rd_integer(T &x) {
  if (pil + 100 > pir) load();
  char c;
  do
    c = ibuf[pil++];
  while (c < '-');
  bool minus = 0;
  if constexpr (is_signed<T>::value || is_same_v<T, i128>) {
    if (c == '-') { minus = 1, c = ibuf[pil++]; }
  }
  x = 0;
  while ('0' <= c) { x = x * 10 + (c & 15), c = ibuf[pil++]; }
  if constexpr (is_signed<T>::value || is_same_v<T, i128>) {
    if (minus) x = -x;
  }
}

void rd(int &x) { rd_integer(x); }
void rd(ll &x) { rd_integer(x); }
void rd(i128 &x) { rd_integer(x); }
void rd(u32 &x) { rd_integer(x); }
void rd(u64 &x) { rd_integer(x); }
void rd(u128 &x) { rd_integer(x); }
void rd(double &x) { rd_real(x); }
void rd(long double &x) { rd_real(x); }
void rd(f128 &x) { rd_real(x); }

template <class T, class U>
void rd(pair<T, U> &p) {
  return rd(p.first), rd(p.second);
}
template <size_t N = 0, typename T>
void rd_tuple(T &t) {
  if constexpr (N < std::tuple_size<T>::value) {
    auto &x = std::get<N>(t);
    rd(x);
    rd_tuple<N + 1>(t);
  }
}
template <class... T>
void rd(tuple<T...> &tpl) {
  rd_tuple(tpl);
}

template <size_t N = 0, typename T>
void rd(array<T, N> &x) {
  for (auto &d: x) rd(d);
}
template <class T>
void rd(vc<T> &x) {
  for (auto &d: x) rd(d);
}

void read() {}
template <class H, class... T>
void read(H &h, T &... t) {
  rd(h), read(t...);
}

void wt(const char c) {
  if (por == SZ) flush();
  obuf[por++] = c;
}
void wt(const string s) {
  for (char c: s) wt(c);
}
void wt(const char *s) {
  size_t len = strlen(s);
  for (size_t i = 0; i < len; i++) wt(s[i]);
}

template <typename T>
void wt_integer(T x) {
  if (por > SZ - 100) flush();
  if (x < 0) { obuf[por++] = '-', x = -x; }
  int outi;
  for (outi = 96; x >= 10000; outi -= 4) {
    memcpy(out + outi, pre.num[x % 10000], 4);
    x /= 10000;
  }
  if (x >= 1000) {
    memcpy(obuf + por, pre.num[x], 4);
    por += 4;
  } else if (x >= 100) {
    memcpy(obuf + por, pre.num[x] + 1, 3);
    por += 3;
  } else if (x >= 10) {
    int q = (x * 103) >> 10;
    obuf[por] = q | '0';
    obuf[por + 1] = (x - q * 10) | '0';
    por += 2;
  } else
    obuf[por++] = x | '0';
  memcpy(obuf + por, out + outi + 4, 96 - outi);
  por += 96 - outi;
}

template <typename T>
void wt_real(T x) {
  ostringstream oss;
  oss << fixed << setprecision(15) << double(x);
  string s = oss.str();
  wt(s);
}

void wt(int x) { wt_integer(x); }
void wt(ll x) { wt_integer(x); }
void wt(i128 x) { wt_integer(x); }
void wt(u32 x) { wt_integer(x); }
void wt(u64 x) { wt_integer(x); }
void wt(u128 x) { wt_integer(x); }
void wt(double x) { wt_real(x); }
void wt(long double x) { wt_real(x); }
void wt(f128 x) { wt_real(x); }

template <class T, class U>
void wt(const pair<T, U> val) {
  wt(val.first);
  wt(' ');
  wt(val.second);
}
template <size_t N = 0, typename T>
void wt_tuple(const T t) {
  if constexpr (N < std::tuple_size<T>::value) {
    if constexpr (N > 0) { wt(' '); }
    const auto x = std::get<N>(t);
    wt(x);
    wt_tuple<N + 1>(t);
  }
}
template <class... T>
void wt(tuple<T...> tpl) {
  wt_tuple(tpl);
}
template <class T, size_t S>
void wt(const array<T, S> val) {
  auto n = val.size();
  for (size_t i = 0; i < n; i++) {
    if (i) wt(' ');
    wt(val[i]);
  }
}
template <class T>
void wt(const vector<T> val) {
  auto n = val.size();
  for (size_t i = 0; i < n; i++) {
    if (i) wt(' ');
    wt(val[i]);
  }
}

void print() { wt('\n'); }
template <class Head, class... Tail>
void print(Head &&head, Tail &&... tail) {
  wt(head);
  if (sizeof...(Tail)) wt(' ');
  print(forward<Tail>(tail)...);
}

// gcc expansion. called automaticall after main.

void __attribute__((destructor)) _d() { flush(); }
} // namespace fastio

using fastio::read;
using fastio::print;
using fastio::flush;

#ifndef ONLINE_JUDGE
#define SHOW(...) \
  SHOW_IMPL(__VA_ARGS__, SHOW4, SHOW3, SHOW2, SHOW1)(__VA_ARGS__)
#define SHOW_IMPL(_1, _2, _3, _4, NAME, ...) NAME
#define SHOW1(x) print(#x, "=", (x)), flush()
#define SHOW2(x, y) print(#x, "=", (x), #y, "=", (y)), flush()
#define SHOW3(x, y, z) print(#x, "=", (x), #y, "=", (y), #z, "=", (z)), flush()
#define SHOW4(x, y, z, w) \
  print(#x, "=", (x), #y, "=", (y), #z, "=", (z), #w, "=", (w)), flush()
#else
#define SHOW(...)
#endif

#define INT(...)   \
  int __VA_ARGS__; \
  read(__VA_ARGS__)
#define LL(...)   \
  ll __VA_ARGS__; \
  read(__VA_ARGS__)
#define U32(...)   \
  u32 __VA_ARGS__; \
  read(__VA_ARGS__)
#define U64(...)   \
  u64 __VA_ARGS__; \
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
template <typename Iterable>
auto print_all(const Iterable& v, std::string sep = " ", std::string end = "\n") -> decltype(fastio::wt(*v.begin())) {
    for (auto it = v.begin(); it != v.end();) {
        fastio::wt(*it);
        if (++it != v.end()) fastio::wt(sep);
    }
    fastio::wt(end);
}
vvi getGraph(int n, int m, bool directed = false) {
    vvi res(n);
    rep(_, 0, m) {
        INT(u, v);
        u--, v--;
        res[u].emplace_back(v);
        if(!directed) res[v].emplace_back(u);
    }
    return res;
}
vector<vpii> getWeightedGraph(int n, int m, bool directed = false) {
    vector<vpii> res(n);
    rep(_, 0, m) {
        INT(u, v, w);
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

#ifdef FASTIO
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
#endif

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

#ifdef FASTIO
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
#endif

  vc<int> new_idx;
  vc<bool> used_e;

  // G における頂点 V[i] が、新しいグラフで i になるようにする
  // {G, es}
  Graph<T, directed> rearrange(vc<int> V, bool keep_eid = 0) {
    if (len(new_idx) != N) new_idx.assign(N, -1);
    if (len(used_e) != M) used_e.assign(M, 0);
    int n = len(V);
    FOR(i, n) new_idx[V[i]] = i;
    Graph<T, directed> G(n);
    vc<int> history;
    FOR(i, n) {
      for (auto&& e: (*this)[V[i]]) {
        if (used_e[e.id]) continue;
        int a = e.frm, b = e.to;
        if (new_idx[a] != -1 && new_idx[b] != -1) {
          history.eb(e.id);
          used_e[e.id] = 1;
          int eid = (keep_eid ? e.id : -1);
          G.add(new_idx[a], new_idx[b], e.cost, eid);
        }
      }
    }
    FOR(i, n) new_idx[V[i]] = -1;
    for (auto&& eid: history) used_e[eid] = 0;
    G.build();
    return G;
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
#line 3 "graph/shortest_path/bfs01.hpp"

template <typename T, typename GT>
pair<vc<T>, vc<int>> bfs01(GT& G, int v) {
  assert(G.is_prepared());
  int N = G.N;
  vc<T> dist(N, infty<T>);
  vc<int> par(N, -1);
  deque<int> que;

  dist[v] = 0;
  que.push_front(v);
  while (!que.empty()) {
    auto v = que.front();
    que.pop_front();
    for (auto&& e: G[v]) {
      if (dist[e.to] == infty<T> || dist[e.to] > dist[e.frm] + e.cost) {
        dist[e.to] = dist[e.frm] + e.cost;
        par[e.to] = e.frm;
        if (e.cost == 0)
          que.push_front(e.to);
        else
          que.push_back(e.to);
      }
    }
  }
  return {dist, par};
}

// 多点スタート。[dist, par, root]
template <typename T, typename GT>
tuple<vc<T>, vc<int>, vc<int>> bfs01(GT& G, vc<int> vs) {
  assert(G.is_prepared());
  int N = G.N;
  vc<T> dist(N, infty<T>);
  vc<int> par(N, -1);
  vc<int> root(N, -1);
  deque<int> que;

  for (auto&& v: vs) {
    dist[v] = 0;
    root[v] = v;
    que.push_front(v);
  }

  while (!que.empty()) {
    auto v = que.front();
    que.pop_front();
    for (auto&& e: G[v]) {
      if (dist[e.to] == infty<T> || dist[e.to] > dist[e.frm] + e.cost) {
        dist[e.to] = dist[e.frm] + e.cost;
        root[e.to] = root[e.frm];
        par[e.to] = e.frm;
        if (e.cost == 0)
          que.push_front(e.to);
        else
          que.push_back(e.to);
      }
    }
  }
  return {dist, par, root};
}
#line 3 "graph/centroid_decomposition.hpp"

// 頂点ベースの重心分解
// f(par, V, indptr)
template <typename F>
void centroid_decomposition_0_dfs(vc<int>& par, vc<int>& vs, F f) {
  const int N = len(par);
  assert(N >= 1);
  int c = -1;
  vc<int> sz(N, 1);
  FOR_R(i, N) {
    if (sz[i] >= ceil<int>(N, 2)) {
      c = i;
      break;
    }
    sz[par[i]] += sz[i];
  }
  vc<int> color(N);
  vc<int> V = {c};
  int nc = 1;
  FOR(v, 1, N) {
    if (par[v] == c) { V.eb(v), color[v] = nc++; }
  }
  if (c > 0) {
    for (int a = par[c]; a != -1; a = par[a]) { color[a] = nc, V.eb(a); }
    ++nc;
  }
  FOR(i, N) {
    if (i != c && color[i] == 0) color[i] = color[par[i]], V.eb(i);
  }
  vc<int> indptr(nc + 1);
  FOR(i, N) indptr[1 + color[i]]++;
  FOR(i, nc) indptr[i + 1] += indptr[i];
  vc<int> counter = indptr;
  vc<int> ord(N);
  for (auto& v: V) { ord[counter[color[v]]++] = v; }
  vc<int> new_idx(N);
  FOR(i, N) new_idx[ord[i]] = i;
  vc<int> name(N);
  FOR(i, N) name[new_idx[i]] = vs[i];
  {
    vc<int> tmp(N, -1);
    FOR(i, 1, N) {
      int a = new_idx[i], b = new_idx[par[i]];
      if (a > b) swap(a, b);
      tmp[b] = a;
    }
    swap(par, tmp);
  }
  f(par, name, indptr);
  FOR(k, 1, nc) {
    int L = indptr[k], R = indptr[k + 1];
    vc<int> par1(R - L, -1);
    vc<int> name1(R - L, -1);
    name1[0] = name[0];
    FOR(i, L, R) name1[i - L] = name[i];
    FOR(i, L, R) { par1[i - L] = max(par[i] - L, -1); }
    centroid_decomposition_0_dfs(par1, name1, f);
  }
}

/*
https://maspypy.com/%e9%87%8d%e5%bf%83%e5%88%86%e8%a7%a3%e3%83%bb1-3%e9%87%8d%e5%bf%83%e5%88%86%e8%a7%a3%e3%81%ae%e3%81%8a%e7%b5%b5%e6%8f%8f%e3%81%8d
centroid_decomposition_1：長さ 2 以上のパス全体
f(par, V, n1, n2)
[1,1+n1]: color 1
[1+n1,1+n1+n2]: color 2
*/
template <typename F>
void centroid_decomposition_1_dfs(vc<int>& par, vc<int> vs, F f) {
  const int N = len(par);
  assert(N > 1);
  if (N == 2) { return; }
  int c = -1;
  vc<int> sz(N, 1);
  FOR_R(i, N) {
    if (sz[i] >= ceil<int>(N, 2)) {
      c = i;
      break;
    }
    sz[par[i]] += sz[i];
  }
  vc<int> color(N, -1);
  int take = 0;
  vc<int> ord(N, -1);
  ord[c] = 0;
  int p = 1;
  FOR(v, 1, N) {
    if (par[v] == c && take + sz[v] <= floor<int>(N - 1, 2)) {
      color[v] = 0, ord[v] = p++, take += sz[v];
    }
  }
  FOR(i, 1, N) {
    if (color[par[i]] == 0) color[i] = 0, ord[i] = p++;
  }
  int n0 = p - 1;
  for (int a = par[c]; a != -1; a = par[a]) { color[a] = 1, ord[a] = p++; }
  FOR(i, N) {
    if (i != c && color[i] == -1) color[i] = 1, ord[i] = p++;
  }
  assert(p == N);
  int n1 = N - 1 - n0;
  vc<int> par0(n0 + 1, -1), par1(n1 + 1, -1), par2(N, -1);
  vc<int> V0(n0 + 1), V1(n1 + 1), V2(N);
  FOR(v, N) {
    int i = ord[v];
    V2[i] = vs[v];
    if (color[v] != 1) { V0[i] = vs[v]; }
    if (color[v] != 0) { V1[max(i - n0, 0)] = vs[v]; }
  }
  FOR(v, 1, N) {
    int a = ord[v], b = ord[par[v]];
    if (a > b) swap(a, b);
    par2[b] = a;
    if (color[v] != 1 && color[par[v]] != 1) par0[b] = a;
    if (color[v] != 0 && color[par[v]] != 0)
      par1[max(b - n0, 0)] = max(a - n0, 0);
  }
  f(par2, V2, n0, n1);
  centroid_decomposition_1_dfs(par0, V0, f);
  centroid_decomposition_1_dfs(par1, V1, f);
}

/*
https://maspypy.com/%e9%87%8d%e5%bf%83%e5%88%86%e8%a7%a3%e3%83%bb1-3%e9%87%8d%e5%bf%83%e5%88%86%e8%a7%a3%e3%81%ae%e3%81%8a%e7%b5%b5%e6%8f%8f%e3%81%8d
f(par2, V2, color)
color in [-1,0,1], -1 is virtual.
*/
template <typename F>
void centroid_decomposition_2_dfs(vc<int>& par, vc<int>& vs, vc<int>& real,
                                  F f) {
  const int N = len(par);
  assert(N > 1);
  if (N == 2) {
    if (real[0] && real[1]) {
      vc<int> color = {0, 1};
      f(par, vs, color);
    }
    return;
  }
  int c = -1;
  vc<int> sz(N, 1);
  FOR_R(i, N) {
    if (sz[i] >= ceil<int>(N, 2)) {
      c = i;
      break;
    }
    sz[par[i]] += sz[i];
  }
  vc<int> color(N, -1);
  int take = 0;
  vc<int> ord(N, -1);
  ord[c] = 0;
  int p = 1;
  FOR(v, 1, N) {
    if (par[v] == c && take + sz[v] <= floor<int>(N - 1, 2)) {
      color[v] = 0, ord[v] = p++, take += sz[v];
    }
  }
  FOR(i, 1, N) {
    if (color[par[i]] == 0) color[i] = 0, ord[i] = p++;
  }
  int n0 = p - 1;
  for (int a = par[c]; a != -1; a = par[a]) { color[a] = 1, ord[a] = p++; }
  FOR(i, N) {
    if (i != c && color[i] == -1) color[i] = 1, ord[i] = p++;
  }
  assert(p == N);
  int n1 = N - 1 - n0;
  vc<int> par0(n0 + 1, -1), par1(n1 + 1, -1), par2(N, -1);
  vc<int> V0(n0 + 1), V1(n1 + 1), V2(N);
  vc<int> rea0(n0 + 1), rea1(n1 + 1), rea2(N);
  FOR(v, N) {
    int i = ord[v];
    V2[i] = vs[v], rea2[i] = real[v];
    if (color[v] != 1) { V0[i] = vs[v], rea0[i] = real[v]; }
    if (color[v] != 0) {
      V1[max(i - n0, 0)] = vs[v], rea1[max(i - n0, 0)] = real[v];
    }
  }
  FOR(v, 1, N) {
    int a = ord[v], b = ord[par[v]];
    if (a > b) swap(a, b);
    par2[b] = a;
    if (color[v] != 1 && color[par[v]] != 1) par0[b] = a;
    if (color[v] != 0 && color[par[v]] != 0)
      par1[max(b - n0, 0)] = max(a - n0, 0);
  }
  if (real[c]) {
    color.assign(N, -1);
    color[0] = 0;
    FOR(i, 1, N) color[i] = rea2[i] ? 1 : -1;
    f(par2, V2, color);
    rea0[0] = rea1[0] = rea2[0] = 0;
  }
  color.assign(N, -1);
  FOR(i, 1, N) if (rea2[i]) color[i] = (i <= n0 ? 0 : 1);
  f(par2, V2, color);
  centroid_decomposition_2_dfs(par0, V0, rea0, f);
  centroid_decomposition_2_dfs(par1, V1, rea1, f);
}

// f(par, V, color)
// V: label in original tree, dfs order
// color in [-1,0,1], color=-1: virtual
template <int MODE, typename GT, typename F>
void centroid_decomposition(GT& G, F f) {
  const int N = G.N;
  if (N == 1) return;
  vc<int> V(N), par(N, -1);
  int l = 0, r = 0;
  V[r++] = 0;
  while (l < r) {
    int v = V[l++];
    for (auto& e: G[v]) {
      if (e.to != par[v]) V[r++] = e.to, par[e.to] = v;
    }
  }
  assert(r == N);
  vc<int> new_idx(N);
  FOR(i, N) new_idx[V[i]] = i;
  vc<int> tmp(N, -1);
  FOR(i, 1, N) {
    int j = par[i];
    tmp[new_idx[i]] = new_idx[j];
  }
  swap(par, tmp);
  static_assert(MODE == 0 || MODE == 1 || MODE == 2);
  if constexpr (MODE == 0) { centroid_decomposition_0_dfs(par, V, f); }
  elif constexpr(MODE == 1) { centroid_decomposition_1_dfs(par, V, f); }
  else {
    vc<int> real(N, 1);
    centroid_decomposition_2_dfs(par, V, real, f);
  }
}

#line 2 "ds/sparse_table/disjoint_sparse_table.hpp"

template <class Monoid>
struct Disjoint_Sparse_Table {
  using MX = Monoid;
  using X = typename MX::value_type;
  int n, log;
  vvc<X> dat;

  Disjoint_Sparse_Table() {}
  Disjoint_Sparse_Table(int n) { build(n); }
  template <typename F>
  Disjoint_Sparse_Table(int n, F f) {
    build(n, f);
  }
  Disjoint_Sparse_Table(const vc<X>& v) { build(v); }

  void build(int m) {
    build(m, [](int i) -> X { return MX::unit(); });
  }
  void build(const vc<X>& v) {
    build(len(v), [&](int i) -> X { return v[i]; });
  }
  template <typename F>
  void build(int m, F f) {
    n = m, log = 1;
    while ((1 << log) < n) ++log;
    dat.resize(log);
    dat[0].reserve(n);
    FOR(i, n) dat[0].eb(f(i));
    FOR(i, 1, log) {
      auto& v = dat[i];
      v = dat[0];
      int b = 1 << i;
      for (int m = b; m <= n; m += 2 * b) {
        int L = m - b, R = min(n, m + b);
        FOR_R(j, L + 1, m) v[j - 1] = MX::op(v[j - 1], v[j]);
        FOR(j, m, R - 1) v[j + 1] = MX::op(v[j], v[j + 1]);
      }
    }
  }

  X prod(int L, int R) {
    if (L == R) return MX::unit();
    --R;
    if (L == R) return dat[0][L];
    int k = topbit(L ^ R);
    return MX::op(dat[k][L], dat[k][R]);
  }

  template <class F>
  int max_right(const F check, int L) {
    assert(0 <= L && L <= n && check(MX::unit()));
    if (L == n) return n;
    int ok = L, ng = n + 1;
    while (ok + 1 < ng) {
      int k = (ok + ng) / 2;
      bool bl = check(prod(L, k));
      if (bl) ok = k;
      if (!bl) ng = k;
    }
    return ok;
  }

  template <class F>
  int min_left(const F check, int R) {
    assert(0 <= R && R <= n && check(MX::unit()));
    if (R == 0) return 0;
    int ok = R, ng = -1;
    while (ng + 1 < ok) {
      int k = (ok + ng) / 2;
      bool bl = check(prod(k, R));
      if (bl) ok = k;
      if (!bl) ng = k;
    }
    return ok;
  }
};
#line 2 "graph/tree.hpp"

#line 4 "graph/tree.hpp"

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
  int get_eid(int u, int v) {
    if (parent[u] != v) swap(u, v);
    assert(parent[u] == v);
    return VtoE[u];
  }

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

  int meet(int a, int b, int c) { return LCA(a, b) ^ LCA(a, c) ^ LCA(b, c); }
  int lca(int u, int v) { return LCA(u, v); }

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

  vc<int> collect_light(int v) {
    vc<int> res;
    bool skip = true;
    for (auto &&e: G[v])
      if (e.to != parent[v]) {
        if (!skip) res.eb(e.to);
        skip = false;
      }
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

  // 辺の列の情報 (frm,to,str)

  // str = "heavy_up", "heavy_down", "light_up", "light_down"

  vc<tuple<int, int, string>> get_path_decomposition_detail(int u, int v) {
    vc<tuple<int, int, string>> up, down;
    while (1) {
      if (head[u] == head[v]) break;
      if (LID[u] < LID[v]) {
        if (v != head[v]) down.eb(head[v], v, "heavy_down"), v = head[v];
        down.eb(parent[v], v, "light_down"), v = parent[v];
      } else {
        if (u != head[u]) up.eb(u, head[u], "heavy_up"), u = head[u];
        up.eb(u, parent[u], "light_up"), u = parent[u];
      }
    }
    if (LID[u] < LID[v]) down.eb(u, v, "heavy_down");
    elif (LID[v] < LID[u]) up.eb(u, v, "heavy_up");
    reverse(all(down));
    concat(up, down);
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

  // path [a,b] と [c,d] の交わり. 空ならば {-1,-1}.

  // https://codeforces.com/problemset/problem/500/G

  pair<int, int> path_intersection(int a, int b, int c, int d) {
    int ab = lca(a, b), ac = lca(a, c), ad = lca(a, d);
    int bc = lca(b, c), bd = lca(b, d), cd = lca(c, d);
    int x = ab ^ ac ^ bc, y = ab ^ ad ^ bd; // meet(a,b,c), meet(a,b,d)

    if (x != y) return {x, y};
    int z = ac ^ ad ^ cd;
    if (x != z) x = -1;
    return {x, x};
  }
};
#line 2 "alg/monoid/monoid_reverse.hpp"

template <class Monoid>
struct Monoid_Reverse {
  using value_type = typename Monoid::value_type;
  using X = value_type;
  static constexpr X op(const X &x, const X &y) { return Monoid::op(y, x); }
  static constexpr X unit() { return Monoid::unit(); }
  static const bool commute = Monoid::commute;
};
#line 4 "graph/ds/static_tree_monoid.hpp"

template <typename TREE, typename Monoid, bool edge>
struct Static_Tree_Monoid {
  using MX = Monoid;
  using X = typename Monoid::value_type;
  TREE &tree;
  int N;
  Disjoint_Sparse_Table<MX> seg;
  Disjoint_Sparse_Table<Monoid_Reverse<MX>> seg_r;

  Static_Tree_Monoid(TREE &tree) : tree(tree), N(tree.N) {
    build([](int i) -> X { return MX::unit(); });
  }

  Static_Tree_Monoid(TREE &tree, vc<X> &dat) : tree(tree), N(tree.N) {
    build([&](int i) -> X { return dat[i]; });
  }

  template <typename F>
  Static_Tree_Monoid(TREE &tree, F f) : tree(tree), N(tree.N) {
    build(f);
  }

  template <typename F>
  void build(F f) {
    if (!edge) {
      auto f_v = [&](int i) -> X { return f(tree.V[i]); };
      seg.build(N, f_v);
      if constexpr (!MX::commute) seg_r.build(N, f_v);
    } else {
      auto f_e = [&](int i) -> X {
        return (i == 0 ? MX::unit() : f(tree.v_to_e(tree.V[i])));
      };
      seg.build(N, f_e);
      if constexpr (!MX::commute) seg_r.build(N, f_e);
    }
  }

  X prod_path(int u, int v) {
    auto pd = tree.get_path_decomposition(u, v, edge);
    X val = MX::unit();
    for (auto &&[a, b]: pd) { val = MX::op(val, get_prod(a, b)); }
    return val;
  }

  // uv path 上で prod_path(u, x) が check を満たす最後の x
  // なければ -1
  template <class F>
  int max_path(F check, int u, int v) {
    if (edge) return max_path_edge(check, u, v);
    if (!check(prod_path(u, u))) return -1;
    auto pd = tree.get_path_decomposition(u, v, edge);
    X val = MX::unit();
    for (auto &&[a, b]: pd) {
      X x = get_prod(a, b);
      if (check(MX::op(val, x))) {
        val = MX::op(val, x);
        u = (tree.V[b]);
        continue;
      }
      auto check_tmp = [&](X x) -> bool { return check(MX::op(val, x)); };
      if (a <= b) {
        // 下り
        int i = seg.max_right(check_tmp, a);
        return (i == a ? u : tree.V[i - 1]);
      } else {
        // 上り
        int i = 0;
        if constexpr (MX::commute) i = seg.min_left(check_tmp, a + 1);
        if constexpr (!MX::commute) i = seg_r.min_left(check_tmp, a + 1);
        if (i == a + 1) return u;
        return (edge ? tree.parent[tree.V[i]] : tree.V[i]);
      }
    }
    return v;
  }

  X prod_subtree(int u) {
    int l = tree.LID[u], r = tree.RID[u];
    return seg.prod(l + edge, r);
  }

  // [a,b] heavy path 形式
  inline X get_prod(int a, int b) {
    if constexpr (MX::commute)
      return (a <= b ? seg.prod(a, b + 1) : seg.prod(b, a + 1));
    return (a <= b ? seg.prod(a, b + 1) : seg_r.prod(b, a + 1));
  }

private:
  template <class F>
  int max_path_edge(F check, int u, int v) {
    assert(edge);
    if (!check(MX::unit())) return -1;
    int lca = tree.lca(u, v);
    auto pd = tree.get_path_decomposition(u, lca, edge);
    X val = MX::unit();

    // climb
    for (auto &&[a, b]: pd) {
      assert(a >= b);
      X x = get_prod(a, b);
      if (check(MX::op(val, x))) {
        val = MX::op(val, x);
        u = (tree.parent[tree.V[b]]);
        continue;
      }
      auto check_tmp = [&](X x) -> bool { return check(MX::op(val, x)); };
      int i = 0;
      if constexpr (MX::commute) i = seg.min_left(check_tmp, a + 1);
      if constexpr (!MX::commute) i = seg_r.min_left(check_tmp, a + 1);
      if (i == a + 1) return u;
      return tree.parent[tree.V[i]];
    }
    // down
    pd = tree.get_path_decomposition(lca, v, edge);
    for (auto &&[a, b]: pd) {
      assert(a <= b);
      X x = seg.prod(a, b + 1);
      if (check(MX::op(val, x))) {
        val = MX::op(val, x);
        u = (tree.V[b]);
        continue;
      }
      auto check_tmp = [&](X x) -> bool { return check(MX::op(val, x)); };
      auto i = seg.max_right(check_tmp, a);
      return (i == a ? u : tree.V[i - 1]);
    }
    return v;
  }
};

#line 2 "alg/monoid/min.hpp"

template <typename E>
struct Monoid_Min {
  using X = E;
  using value_type = X;
  static constexpr X op(const X &x, const X &y) noexcept { return min(x, y); }
  static constexpr X unit() { return infty<E>; }
  static constexpr bool commute = true;
};

void solve() {
    INT(N);
    Graph G(N);
    G.read_tree();
    Tree tree(G);
    vc<int> dat(N);
    rep(i, N) if (G.deg(i) == 3) dat[i] = 1;
    Static_Tree_Monoid<decltype(tree), Monoid_Min<int>, false> TM(tree, dat);
    ll ans = 0;
    auto f = [&](vc<int>& par, vc<int>& V, vc<int>& indptr) -> void {
        int n = len(par);
        assert(len(V) == n);
        rep(i, 1, n) if (G.deg(V[0]) == 2 && G.deg(V[i]) == 2 && tree.dist(V[0], V[i]) >= 2) {
            int p = tree.jump(V[i], V[0], 1);
            int q = tree.jump(V[0], V[i], 1);
            if (TM.prod_path(p, q)) {
                ans++;
            }
        }
        ll can = 0;
        rep(t, 2, len(indptr)) {
            int l = indptr[t - 1], r = indptr[t];
            rep(i, l, r) if (G.deg(V[i]) == 2) {
                int p = tree.jump(V[i], V[0], 1);
                if (TM.prod_path(V[0], p)) {
                    ans += can;
                }
            }
            rep(i, l, r) if (G.deg(V[i]) == 2) {
                int p = tree.jump(V[i], V[0], 1);
                can += TM.prod_path(V[0], p);
            }
        }
        
    };
    centroid_decomposition<0>(G, f);
    print(ans);
    
}

signed main() {
    int T = 1;
    // read(T);
    while (T--) {
        solve();
    }
    return 0;
}