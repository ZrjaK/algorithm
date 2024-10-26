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

#line 2 "geo/cross_point.hpp"

#line 2 "geo/base.hpp"
template <typename T>
struct Point {
  T x, y;

  Point() : x(0), y(0) {}

  template <typename A, typename B>
  Point(A x, B y) : x(x), y(y) {}

  template <typename A, typename B>
  Point(pair<A, B> p) : x(p.fi), y(p.se) {}

  Point operator+=(const Point p) {
    x += p.x, y += p.y;
    return *this;
  }
  Point operator-=(const Point p) {
    x -= p.x, y -= p.y;
    return *this;
  }
  Point operator+(Point p) const { return {x + p.x, y + p.y}; }
  Point operator-(Point p) const { return {x - p.x, y - p.y}; }
  bool operator==(Point p) const { return x == p.x && y == p.y; }
  bool operator!=(Point p) const { return x != p.x || y != p.y; }
  Point operator-() const { return {-x, -y}; }
  Point operator*(T t) const { return {x * t, y * t}; }
  Point operator/(T t) const { return {x / t, y / t}; }

  bool operator<(Point p) const {
    if (x != p.x) return x < p.x;
    return y < p.y;
  }
  T dot(const Point& other) const { return x * other.x + y * other.y; }
  T det(const Point& other) const { return x * other.y - y * other.x; }

  double norm() { return sqrtl(x * x + y * y); }
  double angle() { return atan2(y, x); }

  Point rotate(double theta) {
    static_assert(!is_integral<T>::value);
    double c = cos(theta), s = sin(theta);
    return Point{c * x - s * y, s * x + c * y};
  }
  Point rot90(bool ccw) { return (ccw ? Point{-y, x} : Point{y, -x}); }
};

#ifdef FASTIO
template <typename T>
void rd(Point<T>& p) {
  fastio::rd(p.x), fastio::rd(p.y);
}
template <typename T>
void wt(Point<T>& p) {
  fastio::wt(p.x);
  fastio::wt(' ');
  fastio::wt(p.y);
}
#endif

// A -> B -> C と進むときに、左に曲がるならば +1、右に曲がるならば -1
template <typename T>
int ccw(Point<T> A, Point<T> B, Point<T> C) {
  T x = (B - A).det(C - A);
  if (x > 0) return 1;
  if (x < 0) return -1;
  return 0;
}

template <typename REAL, typename T, typename U>
REAL dist(Point<T> A, Point<U> B) {
  REAL dx = REAL(A.x) - REAL(B.x);
  REAL dy = REAL(A.y) - REAL(B.y);
  return sqrt(dx * dx + dy * dy);
}

// ax+by+c
template <typename T>
struct Line {
  T a, b, c;

  Line(T a, T b, T c) : a(a), b(b), c(c) {}
  Line(Point<T> A, Point<T> B) { a = A.y - B.y, b = B.x - A.x, c = A.x * B.y - A.y * B.x; }
  Line(T x1, T y1, T x2, T y2) : Line(Point<T>(x1, y1), Point<T>(x2, y2)) {}

  template <typename U>
  U eval(Point<U> P) {
    return a * P.x + b * P.y + c;
  }

  template <typename U>
  T eval(U x, U y) {
    return a * x + b * y + c;
  }

  // 同じ直線が同じ a,b,c で表現されるようにする
  void normalize() {
    static_assert(is_same_v<T, int> || is_same_v<T, long long>);
    T g = gcd(gcd(abs(a), abs(b)), abs(c));
    a /= g, b /= g, c /= g;
    if (b < 0) { a = -a, b = -b, c = -c; }
    if (b == 0 && a < 0) { a = -a, b = -b, c = -c; }
  }

  bool is_parallel(Line other) { return a * other.b - b * other.a == 0; }
  bool is_orthogonal(Line other) { return a * other.a + b * other.b == 0; }
};

template <typename T>
struct Segment {
  Point<T> A, B;

  Segment(Point<T> A, Point<T> B) : A(A), B(B) {}
  Segment(T x1, T y1, T x2, T y2) : Segment(Point<T>(x1, y1), Point<T>(x2, y2)) {}

  bool contain(Point<T> C) {
    T det = (C - A).det(B - A);
    if (det != 0) return 0;
    return (C - A).dot(B - A) >= 0 && (C - B).dot(A - B) >= 0;
  }

  Line<T> to_Line() { return Line(A, B); }
};

template <typename REAL>
struct Circle {
  Point<REAL> O;
  REAL r;
  Circle(Point<REAL> O, REAL r) : O(O), r(r) {}
  Circle(REAL x, REAL y, REAL r) : O(x, y), r(r) {}
  template <typename T>
  bool contain(Point<T> p) {
    REAL dx = p.x - O.x, dy = p.y - O.y;
    return dx * dx + dy * dy <= r * r;
  }
};
#line 4 "geo/cross_point.hpp"

// 平行でないことを仮定
template <typename REAL, typename T>
Point<REAL> cross_point(const Line<T> L1, const Line<T> L2) {
  T det = L1.a * L2.b - L1.b * L2.a;
  assert(det != 0);
  REAL x = -REAL(L1.c) * L2.b + REAL(L1.b) * L2.c;
  REAL y = -REAL(L1.a) * L2.c + REAL(L1.c) * L2.a;
  return Point<REAL>(x / det, y / det);
}

// 浮動小数点数はエラー
// 0: 交点なし
// 1: 一意な交点
// 2：2 つ以上の交点（整数型を利用して厳密にやる）
template <typename T>
int count_cross(Segment<T> S1, Segment<T> S2, bool include_ends) {
  static_assert(!std::is_floating_point<T>::value);
  Line<T> L1 = S1.to_Line();
  Line<T> L2 = S2.to_Line();
  if (L1.is_parallel(L2)) {
    if (L1.eval(S2.A) != 0) return 0;
    // 4 点とも同一直線上にある
    T a1 = S1.A.x, b1 = S1.B.x;
    T a2 = S2.A.x, b2 = S2.B.x;
    if (a1 == b1) {
      a1 = S1.A.y, b1 = S1.B.y;
      a2 = S2.A.y, b2 = S2.B.y;
    }
    if (a1 > b1) swap(a1, b1);
    if (a2 > b2) swap(a2, b2);
    T a = max(a1, a2);
    T b = min(b1, b2);
    if (a < b) return 2;
    if (a > b) return 0;
    return (include_ends ? 1 : 0);
  }
  // 平行でない場合
  T a1 = L2.eval(S1.A), b1 = L2.eval(S1.B);
  T a2 = L1.eval(S2.A), b2 = L1.eval(S2.B);
  if (a1 > b1) swap(a1, b1);
  if (a2 > b2) swap(a2, b2);
  bool ok1 = 0, ok2 = 0;

  if (include_ends) {
    ok1 = (a1 <= T(0)) && (T(0) <= b1);
    ok2 = (a2 <= T(0)) && (T(0) <= b2);
  } else {
    ok1 = (a1 < T(0)) && (T(0) < b1);
    ok2 = (a2 < T(0)) && (T(0) < b2);
  }
  return (ok1 && ok2 ? 1 : 0);
}

// https://codeforces.com/contest/607/problem/E
template <typename REAL, typename T>
vc<Point<REAL>> cross_point(const Circle<T> C, const Line<T> L) {
  T a = L.a, b = L.b, c = L.a * (C.O.x) + L.b * (C.O.y) + L.c;
  T r = C.r;
  bool SW = 0;
  if (abs(a) < abs(b)) {
    swap(a, b);
    SW = 1;
  }
  // ax+by+c=0, x^2+y^2=r^2
  T D = 4 * c * c * b * b - 4 * (a * a + b * b) * (c * c - a * a * r * r);
  if (D < 0) return {};
  REAL sqD = sqrtl(D);
  REAL y1 = (-2 * b * c + sqD) / (2 * (a * a + b * b));
  REAL y2 = (-2 * b * c - sqD) / (2 * (a * a + b * b));
  REAL x1 = (-b * y1 - c) / a;
  REAL x2 = (-b * y2 - c) / a;
  if (SW) swap(x1, y1), swap(x2, y2);
  x1 += C.O.x, x2 += C.O.x;
  y1 += C.O.y, y2 += C.O.y;
  if (D == 0) return {Point<REAL>(x1, y1)};
  return {Point<REAL>(x1, y1), Point<REAL>(x2, y2)};
}

// https://codeforces.com/contest/2/problem/C
template <typename REAL, typename T>
tuple<bool, Point<T>, Point<T>> cross_point_circle(Circle<T> C1, Circle<T> C2) {
  using P = Point<T>;
  P O{0, 0};
  P A = C1.O, B = C2.O;
  if (A == B) return {false, O, O};
  T d = (B - A).norm();
  REAL cos_val = (C1.r * C1.r + d * d - C2.r * C2.r) / (2 * C1.r * d);
  if (cos_val < -1 || 1 < cos_val) return {false, O, O};
  REAL t = acos(cos_val);
  REAL u = (B - A).angle();
  P X = A + P{C1.r * cos(u + t), C1.r * sin(u + t)};
  P Y = A + P{C1.r * cos(u - t), C1.r * sin(u - t)};
  return {true, X, Y};
}

void solve() {
    LL(n, m);
    set<tuple<ll, ll, ll>> S;
    set<pll> NOW;
    rep(m) {
        LL(x, y);
        NOW.insert({x, y});
        Point<ll> X(x, y);
        S.insert({0, 1, -y});
        S.insert({1, 0, -x});
        rep(dx, -1, 2) rep(dy, -1, 2) if (dx && dy) {
            ll nx = x + dx, ny = y + dy;
            Point<ll> Y(nx, ny);
            Line<ll> L(X, Y);
            L.normalize();
            S.insert({L.a, L.b, L.c});
        }
    }
    vc<tuple<ll, ll, ll>> ABC;
    each(a, b, c, S) ABC.eb(a, b, c);
    ll ans = n * n;
    map<pll, ll> CROSS;
    rep(i, len(ABC)) {
        auto [a1, b1, c1] = ABC[i];
        Line<double> L1(a1, b1, c1);
        if (b1 && a1) {
            ll y1 = (-c1 - a1) / b1, y2 = (-c1 - a1 * n) / b1;
            chmax(y1, 1);
            chmax(y2, 1);
            chmin(y1, n);
            chmin(y2, n);
            ans -= abs(y1 - y2) + 1;
        } else {
            ans -= n;
        }
        rep(j, i) {
            auto [a2, b2, c2] = ABC[j];
            Line<double> L2(a2, b2, c2);
            if (L1.is_parallel(L2)) continue;
            Point<double> P = cross_point<double>(L1, L2);
            if (P.x == ll(P.x) && P.y == ll(P.y) && 1 <= P.x && P.x <= n && 1 <= P.y && P.y <= n) {
                CROSS[{ll(P.x), ll(P.y)}]++;
            }
        }
    }
    each(_, v, CROSS) {
        if (v == 1) ans += 1;
        if (v == 3) ans += 2;
        if (v == 6) ans += 3;
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