#ifdef ONLINE_JUDGE
#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx2,popcnt")
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
#line 3 "ds/fenwicktree/fenwicktree.hpp"

template <typename Monoid>
struct FenwickTree {
  using G = Monoid;
  using E = typename G::value_type;
  int n;
  vector<E> dat;
  E total;

  FenwickTree() {}
  FenwickTree(int n) { build(n); }
  template <typename F>
  FenwickTree(int n, F f) {
    build(n, f);
  }
  FenwickTree(const vc<E>& v) { build(v); }

  void build(int m) {
    n = m;
    dat.assign(m, G::unit());
    total = G::unit();
  }
  void build(const vc<E>& v) {
    build(len(v), [&](int i) -> E { return v[i]; });
  }
  template <typename F>
  void build(int m, F f) {
    n = m;
    dat.clear();
    dat.reserve(n);
    total = G::unit();
    FOR(i, n) { dat.eb(f(i)); }
    for (int i = 1; i <= n; ++i) {
      int j = i + (i & -i);
      if (j <= n) dat[j - 1] = G::op(dat[i - 1], dat[j - 1]);
    }
    total = prefix_sum(m);
  }

  E prod_all() { return total; }
  E sum_all() { return total; }
  E sum(int k) { return prefix_sum(k); }
  E prod(int k) { return prefix_prod(k); }
  E prefix_sum(int k) { return prefix_prod(k); }
  E prefix_prod(int k) {
    chmin(k, n);
    E ret = G::unit();
    for (; k > 0; k -= k & -k) ret = G::op(ret, dat[k - 1]);
    return ret;
  }
  E sum(int L, int R) { return prod(L, R); }
  E prod(int L, int R) {
    chmax(L, 0), chmin(R, n);
    if (L == 0) return prefix_prod(R);
    assert(0 <= L && L <= R && R <= n);
    E pos = G::unit(), neg = G::unit();
    while (L < R) { pos = G::op(pos, dat[R - 1]), R -= R & -R; }
    while (R < L) { neg = G::op(neg, dat[L - 1]), L -= L & -L; }
    return G::op(pos, G::inverse(neg));
  }

  void add(int k, E x) { multiply(k, x); }
  void multiply(int k, E x) {
    static_assert(G::commute);
    total = G::op(total, x);
    for (++k; k <= n; k += k & -k) dat[k - 1] = G::op(dat[k - 1], x);
  }

  template <class F>
  int max_right(const F check, int L = 0) {
    assert(check(G::unit()));
    E s = G::unit();
    int i = L;
    // 2^k 進むとダメ
    int k = [&]() {
      while (1) {
        if (i % 2 == 1) { s = G::op(s, G::inverse(dat[i - 1])), i -= 1; }
        if (i == 0) { return topbit(n) + 1; }
        int k = lowbit(i) - 1;
        if (i + (1 << k) > n) return k;
        E t = G::op(s, dat[i + (1 << k) - 1]);
        if (!check(t)) { return k; }
        s = G::op(s, G::inverse(dat[i - 1])), i -= i & -i;
      }
    }();
    while (k) {
      --k;
      if (i + (1 << k) - 1 < len(dat)) {
        E t = G::op(s, dat[i + (1 << k) - 1]);
        if (check(t)) { i += (1 << k), s = t; }
      }
    }
    return i;
  }

  // check(i, x)
  template <class F>
  int max_right_with_index(const F check, int L = 0) {
    assert(check(L, G::unit()));
    E s = G::unit();
    int i = L;
    // 2^k 進むとダメ
    int k = [&]() {
      while (1) {
        if (i % 2 == 1) { s = G::op(s, G::inverse(dat[i - 1])), i -= 1; }
        if (i == 0) { return topbit(n) + 1; }
        int k = lowbit(i) - 1;
        if (i + (1 << k) > n) return k;
        E t = G::op(s, dat[i + (1 << k) - 1]);
        if (!check(i + (1 << k), t)) { return k; }
        s = G::op(s, G::inverse(dat[i - 1])), i -= i & -i;
      }
    }();
    while (k) {
      --k;
      if (i + (1 << k) - 1 < len(dat)) {
        E t = G::op(s, dat[i + (1 << k) - 1]);
        if (check(i + (1 << k), t)) { i += (1 << k), s = t; }
      }
    }
    return i;
  }

  template <class F>
  int min_left(const F check, int R) {
    assert(check(G::unit()));
    E s = G::unit();
    int i = R;
    // false になるところまで戻る
    int k = 0;
    while (i > 0 && check(s)) {
      s = G::op(s, dat[i - 1]);
      k = lowbit(i);
      i -= i & -i;
    }
    if (check(s)) {
      assert(i == 0);
      return 0;
    }
    // 2^k 進むと ok になる
    // false を維持して進む
    while (k) {
      --k;
      E t = G::op(s, G::inverse(dat[i + (1 << k) - 1]));
      if (!check(t)) { i += (1 << k), s = t; }
    }
    return i + 1;
  }

  int kth(E k, int L = 0) {
    return max_right([&k](E x) -> bool { return x <= k; }, L);
  }
};
#line 2 "ds/fenwicktree/fenwicktree_01.hpp"

struct FenwickTree_01 {
  int N, n;
  vc<u64> dat;
  FenwickTree<Monoid_Add<int>> bit;
  FenwickTree_01() {}
  FenwickTree_01(int n) { build(n); }
  template <typename F>
  FenwickTree_01(int n, F f) {
    build(n, f);
  }

  void build(int m) {
    N = m;
    n = ceil<int>(N + 1, 64);
    dat.assign(n, u64(0));
    bit.build(n);
  }

  template <typename F>
  void build(int m, F f) {
    N = m;
    n = ceil<int>(N + 1, 64);
    dat.assign(n, u64(0));
    FOR(i, N) { dat[i / 64] |= u64(f(i)) << (i % 64); }
    bit.build(n, [&](int i) -> int { return popcnt(dat[i]); });
  }

  int sum_all() { return bit.sum_all(); }
  int sum(int k) { return prefix_sum(k); }
  int prefix_sum(int k) {
    int ans = bit.sum(k / 64);
    ans += popcnt(dat[k / 64] & ((u64(1) << (k % 64)) - 1));
    return ans;
  }
  int sum(int L, int R) {
    if (L == 0) return prefix_sum(R);
    int ans = 0;
    ans -= popcnt(dat[L / 64] & ((u64(1) << (L % 64)) - 1));
    ans += popcnt(dat[R / 64] & ((u64(1) << (R % 64)) - 1));
    ans += bit.sum(L / 64, R / 64);
    return ans;
  }

  void add(int k, int x) {
    if (x == 1) add(k);
    if (x == -1) remove(k);
  }

  void add(int k) {
    dat[k / 64] |= u64(1) << (k % 64);
    bit.add(k / 64, 1);
  }
  void remove(int k) {
    dat[k / 64] &= ~(u64(1) << (k % 64));
    bit.add(k / 64, -1);
  }

  int kth(int k, int L = 0) {
    if (k >= sum_all()) return N;
    k += popcnt(dat[L / 64] & ((u64(1) << (L % 64)) - 1));
    L /= 64;
    int mid = 0;
    auto check = [&](auto e) -> bool {
      if (e <= k) chmax(mid, e);
      return e <= k;
    };
    int idx = bit.max_right(check, L);
    if (idx == n) return N;
    k -= mid;
    u64 x = dat[idx];
    int p = popcnt(x);
    if (p <= k) return N;
    k = binary_search([&](int n) -> bool { return (p - popcnt(x >> n)) <= k; },
                      0, 64, 0);
    return 64 * idx + k;
  }

  int next(int k) {
    int idx = k / 64;
    k %= 64;
    u64 x = dat[idx] & ~((u64(1) << k) - 1);
    if (x) return 64 * idx + lowbit(x);
    idx = bit.kth(0, idx + 1);
    if (idx == n || !dat[idx]) return N;
    return 64 * idx + lowbit(dat[idx]);
  }

  int prev(int k) {
    if (k == N) --k;
    int idx = k / 64;
    k %= 64;
    u64 x = dat[idx];
    if (k < 63) x &= (u64(1) << (k + 1)) - 1;
    if (x) return 64 * idx + topbit(x);
    idx = bit.min_left([&](auto e) -> bool { return e <= 0; }, idx) - 1;
    if (idx == -1) return -1;
    return 64 * idx + topbit(dat[idx]);
  }
};
#line 3 "seq/inversion.hpp"

template <typename T>
ll inversion(vc<T> A) {
  int N = len(A);
  if (A.empty()) return 0;
  ll ANS = 0;
  FenwickTree_01 bit(N);
  auto I = argsort(A);
  for (auto& i: I) {
    ANS += bit.sum_all() - bit.sum(i);
    bit.add(i, 1);
  }
  return ANS;
}

// i 番目：A_i が先頭になるように rotate したときの転倒数
template <typename T, bool SMALL = false>
vi inversion_rotate(vc<T>& A) {
  const int N = len(A);
  if (!SMALL) {
    auto key = A;
    UNIQUE(key);
    for (auto&& x: A) x = LB(key, x);
  }
  ll K = MAX(A) + 1;
  ll ANS = 0;
  FenwickTree<Monoid_Add<int>> bit(K);
  for (auto&& x: A) {
    ANS += bit.sum(x + 1, K);
    bit.add(x, 1);
  }
  vi res(N);
  FOR(i, N) {
    res[i] = ANS;
    ll x = A[i];
    ANS = ANS + bit.sum(x + 1, K) - bit.prefix_sum(x);
  }
  return res;
}

// inv[i][j] = inversion A[i:j) であるような (N+1, N+1) テーブル
template <typename T>
vvc<int> all_range_inversion(vc<T>& A) {
  int N = len(A);
  vv(int, dp, N + 1, N + 1);
  FOR_R(L, N + 1) FOR(R, L + 2, N + 1) {
    dp[L][R] = dp[L][R - 1] + dp[L + 1][R] - dp[L + 1][R - 1];
    if (A[L] > A[R - 1]) ++dp[L][R];
  }
  return dp;
}

void solve() {
    INT(n);
    VEC(int, a, n);
    deque<int> ANS;
    FenwickTree<Monoid_Add<int>> X(n + 1);
    ll ans = 0;
    each(i, a) {
        int l = X.prod(0, i), r = X.prod(i, n + 1);
        ans += min(l, r);
        if (l < r) ANS.push_front(i);
        elif (l > r) ANS.push_back(i);
        else {
            if (len(ANS) && ANS.front() < i) ANS.push_back(i);
            else ANS.push_front(i);
        }
        X.add(i, 1);
    }
    print(ans);
    print_all(ANS);
    
}

signed main() {
    int T = 1;
    read(T);
    while (T--) {
        solve();
    }
    return 0;
}