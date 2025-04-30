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

#line 1 "ds/bit_vector.hpp"
struct Bit_Vector {
  int n;
  bool prepared = 0;
  vc<pair<u64, u32>> dat;
  Bit_Vector(int n = 0) : n(n) { dat.assign((n + 127) >> 6, {0, 0}); }
  void set(int i) {
    assert(!prepared && (0 <= i && i < n));
    dat[i >> 6].fi |= u64(1) << (i & 63);
  }
  void reset() {
    fill(all(dat), pair<u64, u32>{0, 0});
    prepared = 0;
  }
  void build() {
    prepared = 1;
    FOR(i, len(dat) - 1) dat[i + 1].se = dat[i].se + popcnt(dat[i].fi);
  }
  // [0, k) 内の 1 の個数
  bool operator[](int i) { return dat[i >> 6].fi >> (i & 63) & 1; }
  int count_prefix(int k, bool f = true) {
    assert(prepared);
    auto [a, b] = dat[k >> 6];
    int ret = b + popcnt(a & ((u64(1) << (k & 63)) - 1));
    return (f ? ret : k - ret);
  }
  int count(int L, int R, bool f = true) { return count_prefix(R, f) - count_prefix(L, f); }
  string to_string() {
    string ans;
    FOR(i, n) ans += '0' + (dat[i / 64].fi >> (i % 64) & 1);
    return ans;
  }
};
#line 1 "ds/index_compression.hpp"
template <typename T>
struct Index_Compression_DISTINCT_SMALL {
  static_assert(is_same_v<T, int>);
  int mi, ma;
  vc<int> dat;
  vc<int> build(vc<int> X) {
    mi = 0, ma = -1;
    if (!X.empty()) mi = MIN(X), ma = MAX(X);
    dat.assign(ma - mi + 2, 0);
    for (auto& x: X) dat[x - mi + 1]++;
    FOR(i, len(dat) - 1) dat[i + 1] += dat[i];
    for (auto& x: X) { x = dat[x - mi]++; }
    FOR_R(i, 1, len(dat)) dat[i] = dat[i - 1];
    dat[0] = 0;
    return X;
  }
  int operator()(ll x) { return dat[clamp<ll>(x - mi, 0, ma - mi + 1)]; }
};

template <typename T>
struct Index_Compression_SAME_SMALL {
  static_assert(is_same_v<T, int>);
  int mi, ma;
  vc<int> dat;
  vc<int> build(vc<int> X) {
    mi = 0, ma = -1;
    if (!X.empty()) mi = MIN(X), ma = MAX(X);
    dat.assign(ma - mi + 2, 0);
    for (auto& x: X) dat[x - mi + 1] = 1;
    FOR(i, len(dat) - 1) dat[i + 1] += dat[i];
    for (auto& x: X) { x = dat[x - mi]; }
    return X;
  }
  int operator()(ll x) { return dat[clamp<ll>(x - mi, 0, ma - mi + 1)]; }
};

template <typename T>
struct Index_Compression_SAME_LARGE {
  vc<T> dat;
  vc<int> build(vc<T> X) {
    vc<int> I = argsort(X);
    vc<int> res(len(X));
    for (auto& i: I) {
      if (!dat.empty() && dat.back() == X[i]) {
        res[i] = len(dat) - 1;
      } else {
        res[i] = len(dat);
        dat.eb(X[i]);
      }
    }
    dat.shrink_to_fit();
    return res;
  }
  int operator()(T x) { return LB(dat, x); }
};

template <typename T>
struct Index_Compression_DISTINCT_LARGE {
  vc<T> dat;
  vc<int> build(vc<T> X) {
    vc<int> I = argsort(X);
    vc<int> res(len(X));
    for (auto& i: I) { res[i] = len(dat), dat.eb(X[i]); }
    dat.shrink_to_fit();
    return res;
  }
  int operator()(T x) { return LB(dat, x); }
};

template <typename T, bool SMALL>
using Index_Compression_DISTINCT =
    typename std::conditional<SMALL, Index_Compression_DISTINCT_SMALL<T>,
                              Index_Compression_DISTINCT_LARGE<T>>::type;
template <typename T, bool SMALL>
using Index_Compression_SAME =
    typename std::conditional<SMALL, Index_Compression_SAME_SMALL<T>,
                              Index_Compression_SAME_LARGE<T>>::type;

// SAME: [2,3,2] -> [0,1,0]
// DISTINCT: [2,2,3] -> [0,2,1]
// (x): lower_bound(X,x) をかえす
template <typename T, bool SAME, bool SMALL>
using Index_Compression =
    typename std::conditional<SAME, Index_Compression_SAME<T, SMALL>,
                              Index_Compression_DISTINCT<T, SMALL>>::type;
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
#line 4 "ds/wavelet_matrix/wavelet_matrix.hpp"

// 静的メソッドinverseの存在をチェックするテンプレート

template <typename, typename = std::void_t<>>
struct has_inverse : std::false_type {};

template <typename T>
struct has_inverse<T, std::void_t<decltype(T::inverse(std::declval<typename T::value_type>()))>> : std::true_type {};

struct Dummy_Data_Structure {
  using MX = Monoid_Add<bool>;
  void build(const vc<bool>& A) {}
};

template <typename Y, bool SMALL_Y, typename SEGTREE = Dummy_Data_Structure>
struct Wavelet_Matrix {
  using Mono = typename SEGTREE::MX;
  using T = typename Mono::value_type;
  static_assert(Mono::commute);

  int n, log, K;
  Index_Compression<Y, true, SMALL_Y> IDX;
  vc<Y> ItoY;
  vc<int> mid;
  vc<Bit_Vector> bv;
  vc<SEGTREE> seg;

  Wavelet_Matrix() {}
  Wavelet_Matrix(const vc<Y>& A) { build(A); }
  Wavelet_Matrix(const vc<Y>& A, vc<T>& SUM_Data) { build(A, SUM_Data); }
  template <typename F>
  Wavelet_Matrix(int n, F f) {
    build(n, f);
  }

  template <typename F>
  void build(int m, F f) {
    vc<Y> A(m);
    vc<T> S(m);
    for (int i = 0; i < m; ++i) {
      auto p = f(i);
      A[i] = p.fi, S[i] = p.se;
    }
    build(A, S);
  }

  void build(const vc<Y>& A) { build(A, vc<T>(len(A), Mono::unit())); }
  void build(const vc<Y>& A, vc<T> S) {
    n = len(A);
    vc<int> B = IDX.build(A);
    K = 0;
    for (auto& x: B) chmax(K, x + 1);
    ItoY.resize(K);
    FOR(i, n) ItoY[B[i]] = A[i];
    log = 0;
    while ((1 << log) < K) ++log;
    mid.resize(log), bv.assign(log, Bit_Vector(n));
    vc<int> B0(n), B1(n);
    vc<T> S0(n), S1(n);
    seg.resize(log + 1);
    seg[log].build(S);
    for (int d = log - 1; d >= 0; --d) {
      int p0 = 0, p1 = 0;
      for (int i = 0; i < n; ++i) {
        bool f = (B[i] >> d & 1);
        if (!f) { B0[p0] = B[i], S0[p0] = S[i], p0++; }
        if (f) { bv[d].set(i), B1[p1] = B[i], S1[p1] = S[i], p1++; }
      }
      swap(B, B0), swap(S, S0);
      move(B1.begin(), B1.begin() + p1, B.begin() + p0);
      move(S1.begin(), S1.begin() + p1, S.begin() + p0);
      mid[d] = p0, bv[d].build(), seg[d].build(S);
    }
  }

  // [L,R) x [0,y)

  int prefix_count(int L, int R, Y y) {
    int p = IDX(y);
    if (L == R || p == 0) return 0;
    if (p == K) return R - L;
    int cnt = 0;
    for (int d = log - 1; d >= 0; --d) {
      int l0 = bv[d].count_prefix(L, 0), r0 = bv[d].count_prefix(R, 0);
      int l1 = L + mid[d] - l0, r1 = R + mid[d] - r0;
      if (p >> d & 1) cnt += r0 - l0, L = l1, R = r1;
      if (!(p >> d & 1)) L = l0, R = r0;
    }
    return cnt;
  }

  // [L,R) x [y1,y2)

  int count(int L, int R, Y y1, Y y2) { return prefix_count(L, R, y2) - prefix_count(L, R, y1); }

  // [L,R) x [0,y)

  pair<int, T> prefix_count_and_prod(int L, int R, Y y) {
    int p = IDX(y);
    if (p == 0) return {0, Mono::unit()};
    if (p == K) return {R - L, seg[log].prod(L, R)};
    int cnt = 0;
    T t = Mono::unit();
    for (int d = log - 1; d >= 0; --d) {
      int l0 = bv[d].count_prefix(L, 0), r0 = bv[d].count_prefix(R, 0);
      int l1 = L + mid[d] - l0, r1 = R + mid[d] - r0;
      if (p >> d & 1) { cnt += r0 - l0, t = Mono::op(t, seg[d].prod(l0, r0)), L = l1, R = r1; }
      if (!(p >> d & 1)) L = l0, R = r0;
    }
    return {cnt, t};
  }

  // [L,R) x [y1,y2)

  pair<int, T> count_and_prod(int L, int R, Y y1, Y y2) {
    if constexpr (has_inverse<Mono>::value) {
      auto [c1, t1] = prefix_count_and_prod(L, R, y1);
      auto [c2, t2] = prefix_count_and_prod(L, R, y2);
      return {c2 - c1, Mono::op(Mono::inverse(t1), t2)};
    }
    int lo = IDX(y1), hi = IDX(y2), cnt = 0;
    T t = Mono::unit();
    auto dfs = [&](auto& dfs, int d, int L, int R, int a, int b) -> void {
      assert(b - a == (1 << d));
      if (hi <= a || b <= lo) return;
      if (lo <= a && b <= hi) {
        cnt += R - L, t = Mono::op(t, seg[d].prod(L, R));
        return;
      }
      --d;
      int c = (a + b) / 2;
      int l0 = bv[d].count_prefix(L, 0), r0 = bv[d].count_prefix(R, 0);
      int l1 = L + mid[d] - l0, r1 = R + mid[d] - r0;
      dfs(dfs, d, l0, r0, a, c), dfs(dfs, d, l1, r1, c, b);
    };
    dfs(dfs, log, L, R, 0, 1 << log);
    return {cnt, t};
  }

  // [L,R) x [y1,y2)

  T prefix_prod(int L, int R, Y y) { return prefix_count_and_prod(L, R, y).se; }
  // [L,R) x [y1,y2)

  T prod(int L, int R, Y y1, Y y2) { return count_and_prod(L, R, y1, y2).se; }
  T prod_all(int L, int R) { return seg[log].prod(L, R); }

  Y kth(int L, int R, int k) {
    assert(0 <= k && k < R - L);
    int p = 0;
    for (int d = log - 1; d >= 0; --d) {
      int l0 = bv[d].count_prefix(L, 0), r0 = bv[d].count_prefix(R, 0);
      int l1 = L + mid[d] - l0, r1 = R + mid[d] - r0;
      if (k < r0 - l0) {
        L = l0, R = r0;
      } else {
        k -= r0 - l0, L = l1, R = r1, p |= 1 << d;
      }
    }
    return ItoY[p];
  }

  // y 以上最小 OR infty<Y>

  Y next(int L, int R, Y y) {
    int k = IDX(y);
    int p = K;

    auto dfs = [&](auto& dfs, int d, int L, int R, int a, int b) -> void {
      if (p <= a || L == R || b <= k) return;
      if (d == 0) {
        chmin(p, a);
        return;
      }
      --d;
      int c = (a + b) / 2;
      int l0 = bv[d].count_prefix(L, 0), r0 = bv[d].count_prefix(R, 0);
      int l1 = L + mid[d] - l0, r1 = R + mid[d] - r0;
      dfs(dfs, d, l0, r0, a, c), dfs(dfs, d, l1, r1, c, b);
    };
    dfs(dfs, log, L, R, 0, 1 << log);
    return (p == K ? infty<Y> : ItoY[p]);
  }

  // y 以下最大 OR -infty<T>

  Y prev(int L, int R, Y y) {
    int k = IDX(y + 1);
    int p = -1;
    auto dfs = [&](auto& dfs, int d, int L, int R, int a, int b) -> void {
      if (b - 1 <= p || L == R || k <= a) return;
      if (d == 0) {
        chmax(p, a);
        return;
      }
      --d;
      int c = (a + b) / 2;
      int l0 = bv[d].count_prefix(L, 0), r0 = bv[d].count_prefix(R, 0);
      int l1 = L + mid[d] - l0, r1 = R + mid[d] - r0;
      dfs(dfs, d, l1, r1, c, b), dfs(dfs, d, l0, r0, a, c);
    };
    dfs(dfs, log, L, R, 0, 1 << log);
    return (p == -1 ? -infty<Y> : ItoY[p]);
  }

  Y median(bool UPPER, int L, int R) {
    assert(0 <= L && L < R && R <= n);
    int k = (UPPER ? (R - L) / 2 : (R - L - 1) / 2);
    return kth(L, R, k);
  }

  pair<Y, T> kth_value_and_prod(int L, int R, int k) {
    assert(0 <= k && k <= R - L);
    if (k == R - L) return {infty<Y>, seg[log].prod(L, R)};
    int p = 0;
    T t = Mono::unit();
    for (int d = log - 1; d >= 0; --d) {
      int l0 = bv[d].count_prefix(L, 0), r0 = bv[d].count_prefix(R, 0);
      int l1 = L + mid[d] - l0, r1 = R + mid[d] - r0;
      if (k < r0 - l0) {
        L = l0, R = r0;
      } else {
        t = Mono::op(t, seg[d].prod(l0, r0)), k -= r0 - l0, L = l1, R = r1, p |= 1 << d;
      }
    }
    t = Mono::op(t, seg[0].prod(L, L + k));
    return {ItoY[p], t};
  }

  T prod_index_range(int L, int R, int k1, int k2) {
    static_assert(has_inverse<Mono>::value);
    T t1 = kth_value_and_prod(L, R, k1).se;
    T t2 = kth_value_and_prod(L, R, k2).se;
    return Mono::op(Mono::inverse(t1), t2);
  }

  // [L,R) x [0,y) での check(cnt, prod) が true となる最大の (cnt,prod)

  template <typename F>
  pair<int, T> max_right(F check, int L, int R) {
    int cnt = 0;
    T t = Mono::unit();
    assert(check(0, Mono::unit()));
    if (check(R - L, seg[log].prod(L, R))) { return {R - L, seg[log].prod(L, R)}; }
    for (int d = log - 1; d >= 0; --d) {
      int l0 = bv[d].count_prefix(L, 0), r0 = bv[d].count_prefix(R, 0);
      int l1 = L + mid[d] - l0, r1 = R + mid[d] - r0;
      int cnt1 = cnt + r0 - l0;
      T t1 = Mono::op(t, seg[d].prod(l0, r0));
      if (check(cnt1, t1)) {
        cnt = cnt1, t = t1, L = l1, R = r1;
      } else {
        L = l0, R = r0;
      }
    }
    return {cnt, t};
  }

  void set(int i, T t) {
    assert(0 <= i && i < n);
    int L = i, R = i + 1;
    seg[log].set(L, t);
    for (int d = log - 1; d >= 0; --d) {
      int l0 = bv[d].count_prefix(L, 0), r0 = bv[d].count_prefix(R, 0);
      int l1 = L + mid[d] - l0, r1 = R + mid[d] - r0;
      if (l0 < r0) L = l0, R = r0;
      if (l0 == r0) L = l1, R = r1;
      seg[d].set(L, t);
    }
  }
  void multiply(int i, T t) {
    assert(0 <= i && i < n);
    int L = i, R = i + 1;
    seg[log].multiply(L, t);
    for (int d = log - 1; d >= 0; --d) {
      int l0 = bv[d].count_prefix(L, 0), r0 = bv[d].count_prefix(R, 0);
      int l1 = L + mid[d] - l0, r1 = R + mid[d] - r0;
      if (l0 < r0) L = l0, R = r0;
      if (l0 == r0) L = l1, R = r1;
      seg[d].multiply(L, t);
    }
  }
  void add(int i, T t) { multiply(i, t); }
};

void solve() {
    INT(n);
    VEC(int, P, n);
    Wavelet_Matrix<int, true> wm(P);
    ll ans = 0;
    rep(i, n) {
        int l_gt = wm.count(0, i, P[i], n + 1), r_gt = wm.count(i + 1, n, P[i], n + 1);
        if (l_gt == 0 && r_gt == 0) continue;
        ll l2 = -2, l1 = -1, r1 = n + 1, r2 = n + 2;
        if (l_gt >= 2) {
            l2 = binary_search([&] (int x) -> bool {
                return wm.count(x, i, P[i], n + 1) >= 2;
            }, 0, i);
        }
        if (l_gt >= 1) {
            l1 = binary_search([&] (int x) -> bool {
                return wm.count(x, i, P[i], n + 1) >= 1;
            }, 0, i);
            chmax(l2, -1);
        }
        if (r_gt >= 2) {
            r2 = binary_search([&] (int x) -> bool {
                return wm.count(i + 1, x, P[i], n + 1) >= 2;
            }, n, i);
        }
        if (r_gt >= 1) {
            r1 = binary_search([&] (int x) -> bool {
                return wm.count(i + 1, x, P[i], n + 1) >= 1;
            }, n, i);
            chmin(r2, n + 1);
        }
        if (l_gt >= 1) ans += (r1 - i - 1) * (l1 - l2) * P[i];
        if (r_gt >= 1) ans += (i - l1) * (r2 - r1) * P[i];
        SHOW(P[i], ans);
        SHOW(l_gt, r_gt);
        SHOW(l2, l1, r1, r2);
    }
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