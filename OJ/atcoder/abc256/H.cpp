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

#line 2 "ds/segtree/lazy_segtree.hpp"

template <typename ActedMonoid>
struct Lazy_SegTree {
  using AM = ActedMonoid;
  using MX = typename AM::Monoid_X;
  using MA = typename AM::Monoid_A;
  using X = typename MX::value_type;
  using A = typename MA::value_type;
  int n, log, size;
  vc<X> dat;
  vc<A> laz;

  Lazy_SegTree() {}
  Lazy_SegTree(int n) { build(n); }
  template <typename F>
  Lazy_SegTree(int n, F f) {
    build(n, f);
  }
  Lazy_SegTree(const vc<X>& v) { build(v); }

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
    size = 1 << log;
    dat.assign(size << 1, MX::unit());
    laz.assign(size, MA::unit());
    FOR(i, n) dat[size + i] = f(i);
    FOR_R(i, 1, size) update(i);
  }

  void update(int k) { dat[k] = MX::op(dat[2 * k], dat[2 * k + 1]); }
  void set(int p, X x) {
    assert(0 <= p && p < n);
    p += size;
    for (int i = log; i >= 1; i--) push(p >> i);
    dat[p] = x;
    for (int i = 1; i <= log; i++) update(p >> i);
  }
  void multiply(int p, const X& x) {
    assert(0 <= p && p < n);
    p += size;
    for (int i = log; i >= 1; i--) push(p >> i);
    dat[p] = MX::op(dat[p], x);
    for (int i = 1; i <= log; i++) update(p >> i);
  }

  X get(int p) {
    assert(0 <= p && p < n);
    p += size;
    for (int i = log; i >= 1; i--) push(p >> i);
    return dat[p];
  }

  vc<X> get_all() {
    FOR(k, 1, size) { push(k); }
    return {dat.begin() + size, dat.begin() + size + n};
  }

  X prod(int l, int r) {
    assert(0 <= l && l <= r && r <= n);
    if (l == r) return MX::unit();
    l += size, r += size;
    for (int i = log; i >= 1; i--) {
      if (((l >> i) << i) != l) push(l >> i);
      if (((r >> i) << i) != r) push((r - 1) >> i);
    }
    X xl = MX::unit(), xr = MX::unit();
    while (l < r) {
      if (l & 1) xl = MX::op(xl, dat[l++]);
      if (r & 1) xr = MX::op(dat[--r], xr);
      l >>= 1, r >>= 1;
    }
    return MX::op(xl, xr);
  }

  X prod_all() { return dat[1]; }

  void apply(int l, int r, A a) {
    assert(0 <= l && l <= r && r <= n);
    if (l == r) return;
    l += size, r += size;
    for (int i = log; i >= 1; i--) {
      if (((l >> i) << i) != l) push(l >> i);
      if (((r >> i) << i) != r) push((r - 1) >> i);
    }
    int l2 = l, r2 = r;
    while (l < r) {
      if (l & 1) apply_at(l++, a);
      if (r & 1) apply_at(--r, a);
      l >>= 1, r >>= 1;
    }
    l = l2, r = r2;
    for (int i = 1; i <= log; i++) {
      if (((l >> i) << i) != l) update(l >> i);
      if (((r >> i) << i) != r) update((r - 1) >> i);
    }
  }

  template <typename F>
  int max_right(const F check, int l) {
    assert(0 <= l && l <= n);
    assert(check(MX::unit()));
    if (l == n) return n;
    l += size;
    for (int i = log; i >= 1; i--) push(l >> i);
    X sm = MX::unit();
    do {
      while (l % 2 == 0) l >>= 1;
      if (!check(MX::op(sm, dat[l]))) {
        while (l < size) {
          push(l);
          l = (2 * l);
          if (check(MX::op(sm, dat[l]))) { sm = MX::op(sm, dat[l++]); }
        }
        return l - size;
      }
      sm = MX::op(sm, dat[l++]);
    } while ((l & -l) != l);
    return n;
  }

  template <typename F>
  int min_left(const F check, int r) {
    assert(0 <= r && r <= n);
    assert(check(MX::unit()));
    if (r == 0) return 0;
    r += size;
    for (int i = log; i >= 1; i--) push((r - 1) >> i);
    X sm = MX::unit();
    do {
      r--;
      while (r > 1 && (r % 2)) r >>= 1;
      if (!check(MX::op(dat[r], sm))) {
        while (r < size) {
          push(r);
          r = (2 * r + 1);
          if (check(MX::op(dat[r], sm))) { sm = MX::op(dat[r--], sm); }
        }
        return r + 1 - size;
      }
      sm = MX::op(dat[r], sm);
    } while ((r & -r) != r);
    return 0;
  }

private:
  void apply_at(int k, A a) {
    ll sz = 1 << (log - topbit(k));
    dat[k] = AM::act(dat[k], a, sz);
    if (k < size) laz[k] = MA::op(laz[k], a);
  }
  void push(int k) {
    if (laz[k] == MA::unit()) return;
    apply_at(2 * k, laz[k]), apply_at(2 * k + 1, laz[k]);
    laz[k] = MA::unit();
  }
};

#line 2 "alg/monoid/add.hpp"

template <typename E>
struct Monoid_Add {
  using X = E;
  using value_type = X;
  static constexpr X op(const X &x, const X &y) noexcept { return x + y; }
  static constexpr X inverse(const X &x) noexcept { return -x; }
  static constexpr X power(const X &x, ll n) noexcept { return X(n) * x; }
  static constexpr X unit() { return X(0); }
  static constexpr bool commute = true;
};
#line 2 "alg/monoid/assign.hpp"

template <typename X, int none_val>
struct Monoid_Assign {
  using value_type = X;
  static X op(X x, X y) { return (y == X(none_val) ? x : y); }
  static constexpr X unit() { return X(none_val); }
  static constexpr bool commute = false;
};
#line 3 "alg/acted_monoid/sum_assign.hpp"

template <typename E, E none_val>
struct ActedMonoid_Sum_Assign {
  using Monoid_X = Monoid_Add<E>;
  using Monoid_A = Monoid_Assign<E, none_val>;
  using X = typename Monoid_X::value_type;
  using A = typename Monoid_A::value_type;
  static constexpr X act(const X &x, const A &a, const ll &size) {
    if (a == Monoid_A::unit()) return x;
    return a * E(size);
  }
};

#line 2 "ds/fastset.hpp"

// 64-ary tree

// space: (N/63) * u64

struct FastSet {
  static constexpr u32 B = 64;
  int n, log;
  vvc<u64> seg;

  FastSet() {}
  FastSet(int n) { build(n); }

  int size() { return n; }

  template <typename F>
  FastSet(int n, F f) {
    build(n, f);
  }

  void build(int m) {
    seg.clear();
    n = m;
    do {
      seg.push_back(vc<u64>((m + B - 1) / B));
      m = (m + B - 1) / B;
    } while (m > 1);
    log = len(seg);
  }
  template <typename F>
  void build(int n, F f) {
    build(n);
    FOR(i, n) { seg[0][i / B] |= u64(f(i)) << (i % B); }
    FOR(h, log - 1) {
      FOR(i, len(seg[h])) { seg[h + 1][i / B] |= u64(bool(seg[h][i])) << (i % B); }
    }
  }

  bool operator[](int i) const { return seg[0][i / B] >> (i % B) & 1; }
  void insert(int i) {
    assert(0 <= i && i < n);
    for (int h = 0; h < log; h++) { seg[h][i / B] |= u64(1) << (i % B), i /= B; }
  }
  void add(int i) { insert(i); }
  void erase(int i) {
    assert(0 <= i && i < n);
    u64 x = 0;
    for (int h = 0; h < log; h++) {
      seg[h][i / B] &= ~(u64(1) << (i % B));
      seg[h][i / B] |= x << (i % B);
      x = bool(seg[h][i / B]);
      i /= B;
    }
  }
  void remove(int i) { erase(i); }

  // min[x,n) or n

  int next(int i) {
    assert(i <= n);
    chmax(i, 0);
    for (int h = 0; h < log; h++) {
      if (i / B == seg[h].size()) break;
      u64 d = seg[h][i / B] >> (i % B);
      if (!d) {
        i = i / B + 1;
        continue;
      }
      i += lowbit(d);
      for (int g = h - 1; g >= 0; g--) {
        i *= B;
        i += lowbit(seg[g][i / B]);
      }
      return i;
    }
    return n;
  }

  // max [0,x], or -1

  int prev(int i) {
    assert(i >= -1);
    if (i >= n) i = n - 1;
    for (int h = 0; h < log; h++) {
      if (i == -1) break;
      u64 d = seg[h][i / B] << (63 - i % B);
      if (!d) {
        i = i / B - 1;
        continue;
      }
      i -= __builtin_clzll(d);
      for (int g = h - 1; g >= 0; g--) {
        i *= B;
        i += topbit(seg[g][i / B]);
      }
      return i;
    }
    return -1;
  }

  bool any(int l, int r) { return next(l) < r; }

  // [l, r)

  template <typename F>
  void enumerate(int l, int r, F f) {
    for (int x = next(l); x < r; x = next(x + 1)) f(x);
  }

  string to_string() {
    string s(n, '?');
    for (int i = 0; i < n; ++i) s[i] = ((*this)[i] ? '1' : '0');
    return s;
  }
};
#line 2 "ds/intervals.hpp"

// FastSet で高速化したもの
template <typename T>
struct Intervals_Fast {
  const int LLIM, RLIM;
  const T none_val;
  // none_val でない区間の個数と長さ合計
  int total_num;
  int total_len;
  vc<T> dat;
  FastSet ss;

  Intervals_Fast(int N, T none_val) : LLIM(0), RLIM(N), none_val(none_val), total_num(0), total_len(0), dat(N, none_val), ss(N) { ss.insert(0); }

  // x を含む区間の情報の取得 l, r, t
  tuple<int, int, T> get(int x, bool ERASE = false) {
    int l = ss.prev(x);
    int r = ss.next(x + 1);
    T t = dat[l];
    if (t != none_val && ERASE) {
      --total_num, total_len -= r - l;
      dat[l] = none_val;
      merge_at(l);
      merge_at(r);
    }
    return {l, r, t};
  }

  // [L, R) 内の全データの取得
  // f(l,r,x)
  template <typename F>
  void enumerate_range(int L, int R, F f, bool ERASE = false) {
    assert(LLIM <= L && L <= R && R <= RLIM);
    if (L == R) return;
    if (!ERASE) {
      int l = ss.prev(L);
      while (l < R) {
        int r = ss.next(l + 1);
        f(max(l, L), min(r, R), dat[l]);
        l = r;
      }
      return;
    }
    // 半端なところの分割
    int p = ss.prev(L);
    if (p < L) {
      ss.insert(L);
      dat[L] = dat[p];
      if (dat[L] != none_val) ++total_num;
    }
    p = ss.next(R);
    if (R < p) {
      dat[R] = dat[ss.prev(R)];
      ss.insert(R);
      if (dat[R] != none_val) ++total_num;
    }
    p = L;
    while (p < R) {
      int q = ss.next(p + 1);
      T x = dat[p];
      f(p, q, x);
      if (dat[p] != none_val) --total_num, total_len -= q - p;
      ss.erase(p);
      p = q;
    }
    ss.insert(L);
    dat[L] = none_val;
  }

  void set(int L, int R, T t) {
    if (L == R) return;
    enumerate_range(
        L, R, [](int l, int r, T x) -> void {}, true);
    ss.insert(L);
    dat[L] = t;
    if (t != none_val) total_num++, total_len += R - L;
    merge_at(L);
    merge_at(R);
  }

  template <typename F>
  void enumerate_all(F f) {
    enumerate_range(0, RLIM, f, false);
  }

  void merge_at(int p) {
    if (p <= 0 || RLIM <= p) return;
    int q = ss.prev(p - 1);
    if (dat[p] == dat[q]) {
      if (dat[p] != none_val) --total_num;
      ss.erase(p);
    }
  }
};

// https://codeforces.com/contest/1638/problem/E
// 持つ値のタイプ T、座標タイプ X
// コンストラクタでは T none_val を指定する
// 先読み可能なら座圧して fastset の方が速い
template <typename T, typename X = ll>
struct Intervals {
  static constexpr X LLIM = -infty<X>;
  static constexpr X RLIM = infty<X>;
  T none_val;
  // const T none_val;
  // none_val でない区間の個数と長さ合計
  int total_num;
  X total_len;
  map<X, T> dat;

  Intervals(T none_val) : none_val(none_val), total_num(0), total_len(0) {
    dat[LLIM] = none_val;
    dat[RLIM] = none_val;
  }

  // x を含む区間の情報の取得 l, r, t
  tuple<X, X, T> get(X x, bool ERASE = false) {
    auto it2 = dat.upper_bound(x);
    auto it1 = prev(it2);
    auto [l, tl] = *it1;
    auto [r, tr] = *it2;
    if (tl != none_val && ERASE) {
      --total_num, total_len -= r - l;
      dat[l] = none_val;
      merge_at(l);
      merge_at(r);
    }
    return {l, r, tl};
  }

  // [L, R) 内の全データの取得 f(l, r, t)
  template <typename F>
  void enumerate_range(X L, X R, F f, bool ERASE = false) {
    assert(LLIM <= L && L <= R && R <= RLIM);
    if (!ERASE) {
      auto it = prev(dat.upper_bound(L));
      while ((*it).fi < R) {
        auto it2 = next(it);
        f(max((*it).fi, L), min((*it2).fi, R), (*it).se);
        it = it2;
      }
      return;
    }
    // 半端なところの分割
    auto p = prev(dat.upper_bound(L));
    if ((*p).fi < L) {
      dat[L] = (*p).se;
      if (dat[L] != none_val) ++total_num;
    }
    p = dat.lower_bound(R);
    if (R < (*p).fi) {
      T t = (*prev(p)).se;
      dat[R] = t;
      if (t != none_val) ++total_num;
    }
    p = dat.lower_bound(L);
    while (1) {
      if ((*p).fi >= R) break;
      auto q = next(p);
      T t = (*p).se;
      f((*p).fi, (*q).fi, t);
      if (t != none_val) --total_num, total_len -= (*q).fi - (*p).fi;
      p = dat.erase(p);
    }
    dat[L] = none_val;
  }

  void set(X L, X R, T t) {
    assert(L <= R);
    if (L == R) return;
    enumerate_range(
        L, R, [](int l, int r, T x) -> void {}, true);
    dat[L] = t;
    if (t != none_val) total_num++, total_len += R - L;
    merge_at(L);
    merge_at(R);
  }

  template <typename F>
  void enumerate_all(F f) {
    enumerate_range(LLIM, RLIM, f, false);
  }

  void merge_at(X p) {
    if (p == LLIM || RLIM == p) return;
    auto itp = dat.lower_bound(p);
    assert((*itp).fi == p);
    auto itq = prev(itp);
    if ((*itp).se == (*itq).se) {
      if ((*itp).se != none_val) --total_num;
      dat.erase(itp);
    }
  }
};

void solve() {
    INT(n, q);
    VEC(ll, A, n);
    Lazy_SegTree<ActedMonoid_Sum_Assign<ll, -infty<int>>> seg(n);
    Intervals<int, int> X(0);
    rep(i, n) {
        X.set(i, i + 1, A[i]);
        seg.set(i, A[i]);
    }
    rep(q) {
        INT(op, L, R);
        L--;
        if (op == 1) {
            INT(x);
            vc<tuple<int, int, int>> dat;
            auto f = [&] (int l, int r, int X) -> void {
                if (!len(dat)) dat.eb(l, r, X / x);
                auto [a, b, c] = dat.back();
                if (c == X / x) {
                    dat.back() = {a, r, c};
                } else {
                    dat.eb(l, r, X / x);
                }
            };
            X.enumerate_range(L, R, f);
            each(a, b, c, dat) {
                X.set(a, b, c);
                seg.apply(a, b, c);
            }
        }
        if (op == 2) {
            INT(y);
            X.set(L, R, y);
            seg.apply(L, R, y);
        }
        if (op == 3) {
            print(seg.prod(L, R));
        }
    }
    
}

signed main() {
    int T = 1;
    // read(T);
    while (T--) {
        solve();
    }
    return 0;
}