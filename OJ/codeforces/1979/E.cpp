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

#line 1 "ds/segtree/segtree_2d.hpp"
// 点の重複があっても別の点として set などがされる

template <typename Monoid, typename XY, bool SMALL_X = false>
struct SegTree_2D {
  using MX = Monoid;
  using S = typename MX::value_type;
  static_assert(MX::commute);
  int N;
  // X to idx

  vc<XY> keyX;
  int minX;
  // top node の点列

  vc<XY> all_Y;
  vc<int> pos;
  // segtree data

  int NX, log, size;
  vc<int> indptr;
  vc<S> dat;
  // fractional cascading

  vc<int> to_left;

  SegTree_2D(vc<XY>& X, vc<XY>& Y)
      : SegTree_2D(len(X), [&](int i) -> tuple<XY, XY, S> {
          return {X[i], Y[i], MX::unit()};
        }) {}

  SegTree_2D(vc<XY>& X, vc<XY>& Y, vc<S>& vals)
      : SegTree_2D(len(X), [&](int i) -> tuple<XY, XY, S> {
          return {X[i], Y[i], vals[i]};
        }) {}

  // f(i) = (x,y,val)

  template <typename F>
  SegTree_2D(int N, F f) {
    vc<XY> X(N), Y(N);
    vc<S> wt(N);
    FOR(i, N) {
      auto [a, b, c] = f(i);
      X[i] = a, Y[i] = b, wt[i] = c;
    }
    if (!SMALL_X) {
      keyX = X;
      UNIQUE(keyX);
      NX = len(keyX);
    } else {
      minX = (X.empty() ? 0 : MIN(X));
      NX = (X.empty() ? 1 : MAX(X) - minX + 1);
    }

    log = 0;
    while ((1 << log) < NX) ++log;
    size = (1 << log);

    vc<int> IX(N);
    FOR(i, N) IX[i] = xtoi(X[i]);
    indptr.assign(2 * size, 0);
    for (auto i: IX) {
      i += size;
      while (i) indptr[i]++, i /= 2;
    }
    indptr = cumsum<int>(indptr);
    dat.assign(2 * indptr.back(), MX::unit());
    to_left.assign(indptr[size], 0);

    vc<int> ptr = indptr;
    vc<int> I = argsort(Y);
    pos.resize(N);
    FOR(i, N) pos[I[i]] = i;
    for (auto raw_idx: I) {
      int i = IX[raw_idx] + size;
      int j = -1;
      while (i) {
        int p = ptr[i];
        ptr[i]++;
        dat[indptr[i + 1] + p] = wt[raw_idx];
        if (j != -1) { to_left[p] = (j % 2 == 0); }
        j = i, i /= 2;
      }
    }
    to_left = cumsum<int>(to_left);

    FOR(i, 2 * size) {
      int off = 2 * indptr[i], n = indptr[i + 1] - indptr[i];
      FOR_R(j, 1, n) {
        dat[off + j] = MX::op(dat[off + 2 * j + 0], dat[off + 2 * j + 1]);
      }
    }
    all_Y = Y;
    sort(all(all_Y));
  }

  // 最初に与えた点群の index

  void multiply(int raw_idx, S val) {
    int i = 1, p = pos[raw_idx];
    while (1) {
      multiply_i(i, p - indptr[i], val);
      if (i >= size) break;
      int lc = to_left[p] - to_left[indptr[i]];
      int rc = (p - indptr[i]) - lc;
      if (to_left[p + 1] - to_left[p]) {
        p = indptr[2 * i + 0] + lc;
        i = 2 * i + 0;
      } else {
        p = indptr[2 * i + 1] + rc;
        i = 2 * i + 1;
      }
    }
  }

  // 最初に与えた点群の index

  void set(int raw_idx, S val) {
    int i = 1, p = pos[raw_idx];
    while (1) {
      set_i(i, p - indptr[i], val);
      if (i >= size) break;
      int lc = to_left[p] - to_left[indptr[i]];
      int rc = (p - indptr[i]) - lc;
      if (to_left[p + 1] - to_left[p]) {
        p = indptr[2 * i + 0] + lc;
        i = 2 * i + 0;
      } else {
        p = indptr[2 * i + 1] + rc;
        i = 2 * i + 1;
      }
    }
  }

  S prod(XY lx, XY rx, XY ly, XY ry) {
    assert(lx <= rx && ly <= ry);
    int L = xtoi(lx), R = xtoi(rx);
    S res = MX::unit();
    auto dfs = [&](auto& dfs, int i, int l, int r, int a, int b) -> void {
      if (a == b || R <= l || r <= L) return;
      if (L <= l && r <= R) {
        res = MX::op(res, prod_i(i, a, b));
        return;
      }
      int la = to_left[indptr[i] + a] - to_left[indptr[i]];
      int ra = a - la;
      int lb = to_left[indptr[i] + b] - to_left[indptr[i]];
      int rb = b - lb;
      int m = (l + r) / 2;
      dfs(dfs, 2 * i + 0, l, m, la, lb);
      dfs(dfs, 2 * i + 1, m, r, ra, rb);
    };
    dfs(dfs, 1, 0, size, LB(all_Y, ly), LB(all_Y, ry));
    return res;
  }

  // 矩形内の全点を数える, NlogN

  int count(XY lx, XY rx, XY ly, XY ry) {
    assert(lx <= rx && ly <= ry);
    int L = xtoi(lx), R = xtoi(rx);
    int res = 0;
    auto dfs = [&](auto& dfs, int i, int l, int r, int a, int b) -> void {
      if (a == b || R <= l || r <= L) return;
      if (L <= l && r <= R) {
        res += b - a;
        return;
      }
      int la = to_left[indptr[i] + a] - to_left[indptr[i]];
      int ra = a - la;
      int lb = to_left[indptr[i] + b] - to_left[indptr[i]];
      int rb = b - lb;
      int m = (l + r) / 2;
      dfs(dfs, 2 * i + 0, l, m, la, lb);
      dfs(dfs, 2 * i + 1, m, r, ra, rb);
    };
    dfs(dfs, 1, 0, size, LB(all_Y, ly), LB(all_Y, ry));
    return res;
  }

private:
  inline int xtoi(XY x) {
    if constexpr (SMALL_X) return clamp<XY>(x - minX, 0, NX);
    return LB(keyX, x);
  }

  S prod_i(int i, int a, int b) {
    int LID = indptr[i], n = indptr[i + 1] - indptr[i];
    int off = 2 * LID;
    int L = n + a, R = n + b;
    S val = MX::unit();
    while (L < R) {
      if (L & 1) val = MX::op(val, dat[off + (L++)]);
      if (R & 1) val = MX::op(dat[off + (--R)], val);
      L >>= 1, R >>= 1;
    }
    return val;
  }
  void multiply_i(int i, int j, S val) {
    int LID = indptr[i], n = indptr[i + 1] - indptr[i];
    int off = 2 * LID;
    j += n;
    while (j) {
      dat[off + j] = MX::op(dat[off + j], val);
      j >>= 1;
    }
  }
  void set_i(int i, int j, S val) {
    int LID = indptr[i], n = indptr[i + 1] - indptr[i];
    int off = 2 * LID;
    j += n;
    dat[off + j] = val;
    while (j > 1) {
      j /= 2;
      dat[off + j] = MX::op(dat[off + 2 * j + 0], dat[off + 2 * j + 1]);
    }
  }
};

#line 2 "alg/monoid/max.hpp"

template <typename E>
struct Monoid_Max {
  using X = E;
  using value_type = X;
  static constexpr X op(const X &x, const X &y) noexcept { return max(x, y); }
  static constexpr X unit() { return -infty<E>; }
  static constexpr bool commute = true;
};

void solve() {
    LL(n, D);
    vll X(n), Y(n);
    rep(i, n) read(X[i], Y[i]);
    vll A(n), B(n);
    rep(i, n) {
        A[i] = X[i] + Y[i];
        B[i] = X[i] - Y[i];
    }
    vll VAL(n);
    iota(all(VAL), 0);
    SegTree_2D<Monoid_Max<ll>, ll> seg(A, B, VAL);
    rep(i, n) {
        {
            auto x = seg.prod(A[i] + D, A[i] + D + 1, B[i], B[i] + 1);
            auto y = seg.prod(A[i], A[i] + D + 1, B[i] + D, B[i] + D + 1);
            if (x != -infty<ll> && y != -infty<ll> && x != y) {
                auto calc = [&] (ll x, ll y) -> ll {
                    return abs(X[x] - X[y]) + abs(Y[x] - Y[y]);
                };
                assert(calc(i, x) == D);
                assert(calc(i, y) == D);
                assert(calc(x, y) == D);
                return print(i + 1, x + 1, y + 1);
            }
        }
        {
            auto x = seg.prod(A[i] + D, A[i] + D + 1, B[i], B[i] + 1);
            auto y = seg.prod(A[i], A[i] + D + 1, B[i] - D, B[i] - D + 1);
            if (x != -infty<ll> && y != -infty<ll> && x != y) {
                auto calc = [&] (ll x, ll y) -> ll {
                    return abs(X[x] - X[y]) + abs(Y[x] - Y[y]);
                };
                assert(calc(i, x) == D);
                assert(calc(i, y) == D);
                assert(calc(x, y) == D);
                return print(i + 1, x + 1, y + 1);
            }
        }
        {
            auto x = seg.prod(A[i], A[i] + 1, B[i] + D, B[i] + D + 1);
            auto y = seg.prod(A[i] + D, A[i] + D + 1, B[i], B[i] + D + 1);
            if (x != -infty<ll> && y != -infty<ll> && x != y) {
                auto calc = [&] (ll x, ll y) -> ll {
                    return abs(X[x] - X[y]) + abs(Y[x] - Y[y]);
                };
                assert(calc(i, x) == D);
                assert(calc(i, y) == D);
                assert(calc(x, y) == D);
                return print(i + 1, x + 1, y + 1);
            }
        }
        {
            auto x = seg.prod(A[i], A[i] + 1, B[i] + D, B[i] + D + 1);
            auto y = seg.prod(A[i] - D, A[i] - D + 1, B[i], B[i] + D + 1);
            if (x != -infty<ll> && y != -infty<ll> && x != y) {
                auto calc = [&] (ll x, ll y) -> ll {
                    return abs(X[x] - X[y]) + abs(Y[x] - Y[y]);
                };
                assert(calc(i, x) == D);
                assert(calc(i, y) == D);
                assert(calc(x, y) == D);
                return print(i + 1, x + 1, y + 1);
            }
        }
    }
    print(0, 0, 0);

    
}

signed main() {
    int T = 1;
    read(T);
    while (T--) {
        solve();
    }
    return 0;
}