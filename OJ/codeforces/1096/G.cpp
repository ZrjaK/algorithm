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

#line 2 "poly/convolution_all.hpp"

#line 2 "mod/modint_common.hpp"

struct has_mod_impl {
  template <class T>
  static auto check(T &&x) -> decltype(x.get_mod(), std::true_type{});
  template <class T>
  static auto check(...) -> std::false_type;
};

template <class T>
class has_mod : public decltype(has_mod_impl::check<T>(std::declval<T>())) {};

template <typename mint>
mint inv(int n) {
  static const int mod = mint::get_mod();
  static vector<mint> dat = {0, 1};
  assert(0 <= n);
  if (n >= mod) n %= mod;
  while (len(dat) <= n) {
    int k = len(dat);
    int q = (mod + k - 1) / k;
    dat.eb(dat[k * q - mod] * mint::raw(q));
  }
  return dat[n];
}

template <typename mint>
mint fact(int n) {
  static const int mod = mint::get_mod();
  assert(0 <= n && n < mod);
  static vector<mint> dat = {1, 1};
  while (len(dat) <= n) dat.eb(dat[len(dat) - 1] * mint::raw(len(dat)));
  return dat[n];
}

template <typename mint>
mint fact_inv(int n) {
  static vector<mint> dat = {1, 1};
  if (n < 0) return mint(0);
  while (len(dat) <= n) dat.eb(dat[len(dat) - 1] * inv<mint>(len(dat)));
  return dat[n];
}

template <class mint, class... Ts>
mint fact_invs(Ts... xs) {
  return (mint(1) * ... * fact_inv<mint>(xs));
}

template <typename mint, class Head, class... Tail>
mint multinomial(Head &&head, Tail &&... tail) {
  return fact<mint>(head) * fact_invs<mint>(std::forward<Tail>(tail)...);
}

template <typename mint>
mint C_dense(int n, int k) {
  static vvc<mint> C;
  static int H = 0, W = 0;
  auto calc = [&](int i, int j) -> mint {
    if (i == 0) return (j == 0 ? mint(1) : mint(0));
    return C[i - 1][j] + (j ? C[i - 1][j - 1] : 0);
  };
  if (W <= k) {
    FOR(i, H) {
      C[i].resize(k + 1);
      FOR(j, W, k + 1) { C[i][j] = calc(i, j); }
    }
    W = k + 1;
  }
  if (H <= n) {
    C.resize(n + 1);
    FOR(i, H, n + 1) {
      C[i].resize(W);
      FOR(j, W) { C[i][j] = calc(i, j); }
    }
    H = n + 1;
  }
  return C[n][k];
}

template <typename mint, bool large = false, bool dense = false>
mint C(ll n, ll k) {
  assert(n >= 0);
  if (k < 0 || n < k) return 0;
  if constexpr (dense) return C_dense<mint>(n, k);
  if constexpr (!large) return multinomial<mint>(n, k, n - k);
  k = min(k, n - k);
  mint x(1);
  FOR(i, k) x *= mint(n - i);
  return x * fact_inv<mint>(k);
}

template <typename mint, bool large = false>
mint C_inv(ll n, ll k) {
  assert(n >= 0);
  assert(0 <= k && k <= n);
  if (!large) return fact_inv<mint>(n) * fact<mint>(k) * fact<mint>(n - k);
  return mint(1) / C<mint, 1>(n, k);
}

// [x^d](1-x)^{-n}
template <typename mint, bool large = false, bool dense = false>
mint C_negative(ll n, ll d) {
  assert(n >= 0);
  if (d < 0) return mint(0);
  if (n == 0) { return (d == 0 ? mint(1) : mint(0)); }
  return C<mint, large, dense>(n + d - 1, d);
}
#line 3 "mod/modint.hpp"

template <int mod>
struct modint {
  static constexpr u32 umod = u32(mod);
  static_assert(umod < u32(1) << 31);
  u32 val;

  static modint raw(u32 v) {
    modint x;
    x.val = v;
    return x;
  }
  constexpr modint() : val(0) {}
  constexpr modint(u32 x) : val(x % umod) {}
  constexpr modint(u64 x) : val(x % umod) {}
  constexpr modint(u128 x) : val(x % umod) {}
  constexpr modint(int x) : val((x %= mod) < 0 ? x + mod : x){};
  constexpr modint(ll x) : val((x %= mod) < 0 ? x + mod : x){};
  constexpr modint(i128 x) : val((x %= mod) < 0 ? x + mod : x){};
  bool operator<(const modint &other) const { return val < other.val; }
  modint &operator+=(const modint &p) {
    if ((val += p.val) >= umod) val -= umod;
    return *this;
  }
  modint &operator-=(const modint &p) {
    if ((val += umod - p.val) >= umod) val -= umod;
    return *this;
  }
  modint &operator*=(const modint &p) {
    val = u64(val) * p.val % umod;
    return *this;
  }
  modint &operator/=(const modint &p) {
    *this *= p.inverse();
    return *this;
  }
  modint operator-() const { return modint::raw(val ? mod - val : u32(0)); }
  modint operator+(const modint &p) const { return modint(*this) += p; }
  modint operator-(const modint &p) const { return modint(*this) -= p; }
  modint operator*(const modint &p) const { return modint(*this) *= p; }
  modint operator/(const modint &p) const { return modint(*this) /= p; }
  bool operator==(const modint &p) const { return val == p.val; }
  bool operator!=(const modint &p) const { return val != p.val; }
  modint inverse() const {
    int a = val, b = mod, u = 1, v = 0, t;
    while (b > 0) {
      t = a / b;
      swap(a -= t * b, b), swap(u -= t * v, v);
    }
    return modint(u);
  }
  modint pow(ll n) const {
    assert(n >= 0);
    modint ret(1), mul(val);
    while (n > 0) {
      if (n & 1) ret *= mul;
      mul *= mul;
      n >>= 1;
    }
    return ret;
  }
  static constexpr int get_mod() { return mod; }
  // (n, r), r は 1 の 2^n 乗根
  static constexpr pair<int, int> ntt_info() {
    if (mod == 120586241) return {20, 74066978};
    if (mod == 167772161) return {25, 17};
    if (mod == 469762049) return {26, 30};
    if (mod == 754974721) return {24, 362};
    if (mod == 880803841) return {23, 211};
    if (mod == 943718401) return {22, 663003469};
    if (mod == 998244353) return {23, 31};
    if (mod == 1045430273) return {20, 363};
    if (mod == 1051721729) return {20, 330};
    if (mod == 1053818881) return {20, 2789};
    return {-1, -1};
  }
  static constexpr bool can_ntt() { return ntt_info().fi != -1; }
};

#ifdef FASTIO
template <int mod>
void rd(modint<mod> &x) {
  fastio::rd(x.val);
  x.val %= mod;
  // assert(0 <= x.val && x.val < mod);
}
template <int mod>
void wt(modint<mod> x) {
  fastio::wt(x.val);
}
#endif

using modint107 = modint<1000000007>;
using modint998 = modint<998244353>;
#line 2 "mod/mod_inv.hpp"

// long でも大丈夫

// (val * x - 1) が mod の倍数になるようにする

// 特に mod=0 なら x=0 が満たす

ll mod_inv(ll val, ll mod) {
  if (mod == 0) return 0;
  mod = abs(mod);
  val %= mod;
  if (val < 0) val += mod;
  ll a = val, b = mod, u = 1, v = 0, t;
  while (b > 0) {
    t = a / b;
    swap(a -= t * b, b), swap(u -= t * v, v);
  }
  if (u < 0) u += mod;
  return u;
}
#line 1 "mod/crt3.hpp"

constexpr u32 mod_pow_constexpr(u64 a, u64 n, u32 mod) {
  a %= mod;
  u64 res = 1;
  FOR(32) {
    if (n & 1) res = res * a % mod;
    a = a * a % mod, n /= 2;
  }
  return res;
}

template <typename T, u32 p0, u32 p1, u32 p2>
T CRT3(u64 a0, u64 a1, u64 a2) {
  static_assert(p0 < p1 && p1 < p2);
  static constexpr u64 x0_1 = mod_pow_constexpr(p0, p1 - 2, p1);
  static constexpr u64 x01_2 = mod_pow_constexpr(u64(p0) * p1 % p2, p2 - 2, p2);
  u64 c = (a1 - a0 + p1) * x0_1 % p1;
  u64 a = a0 + c * p0;
  c = (a2 - a % p2 + p2) * x01_2 % p2;
  return T(a) + T(c) * T(p0) * T(p1);
}
#line 2 "poly/convolution_naive.hpp"

template <class T, typename enable_if<!has_mod<T>::value>::type* = nullptr>
vc<T> convolution_naive(const vc<T>& a, const vc<T>& b) {
  int n = int(a.size()), m = int(b.size());
  if (n > m) return convolution_naive<T>(b, a);
  if (n == 0) return {};
  vector<T> ans(n + m - 1);
  FOR(i, n) FOR(j, m) ans[i + j] += a[i] * b[j];
  return ans;
}

template <class T, typename enable_if<has_mod<T>::value>::type* = nullptr>
vc<T> convolution_naive(const vc<T>& a, const vc<T>& b) {
  int n = int(a.size()), m = int(b.size());
  if (n > m) return convolution_naive<T>(b, a);
  if (n == 0) return {};
  vc<T> ans(n + m - 1);
  if (n <= 16 && (T::get_mod() < (1 << 30))) {
    for (int k = 0; k < n + m - 1; ++k) {
      int s = max(0, k - m + 1);
      int t = min(n, k + 1);
      u64 sm = 0;
      for (int i = s; i < t; ++i) { sm += u64(a[i].val) * (b[k - i].val); }
      ans[k] = sm;
    }
  } else {
    for (int k = 0; k < n + m - 1; ++k) {
      int s = max(0, k - m + 1);
      int t = min(n, k + 1);
      u128 sm = 0;
      for (int i = s; i < t; ++i) { sm += u64(a[i].val) * (b[k - i].val); }
      ans[k] = T::raw(sm % T::get_mod());
    }
  }
  return ans;
}
#line 2 "poly/convolution_karatsuba.hpp"

// 任意の環でできる
template <typename T>
vc<T> convolution_karatsuba(const vc<T>& f, const vc<T>& g) {
  const int thresh = 30;
  if (min(len(f), len(g)) <= thresh) return convolution_naive(f, g);
  int n = max(len(f), len(g));
  int m = ceil(n, 2);
  vc<T> f1, f2, g1, g2;
  if (len(f) < m) f1 = f;
  if (len(f) >= m) f1 = {f.begin(), f.begin() + m};
  if (len(f) >= m) f2 = {f.begin() + m, f.end()};
  if (len(g) < m) g1 = g;
  if (len(g) >= m) g1 = {g.begin(), g.begin() + m};
  if (len(g) >= m) g2 = {g.begin() + m, g.end()};
  vc<T> a = convolution_karatsuba(f1, g1);
  vc<T> b = convolution_karatsuba(f2, g2);
  FOR(i, len(f2)) f1[i] += f2[i];
  FOR(i, len(g2)) g1[i] += g2[i];
  vc<T> c = convolution_karatsuba(f1, g1);
  vc<T> F(len(f) + len(g) - 1);
  assert(2 * m + len(b) <= len(F));
  FOR(i, len(a)) F[i] += a[i], c[i] -= a[i];
  FOR(i, len(b)) F[2 * m + i] += b[i], c[i] -= b[i];
  if (c.back() == T(0)) c.pop_back();
  FOR(i, len(c)) if (c[i] != T(0)) F[m + i] += c[i];
  return F;
}
#line 2 "poly/ntt.hpp"

template <class mint>
void ntt(vector<mint>& a, bool inverse) {
  assert(mint::can_ntt());
  const int rank2 = mint::ntt_info().fi;
  const int mod = mint::get_mod();
  static array<mint, 30> root, iroot;
  static array<mint, 30> rate2, irate2;
  static array<mint, 30> rate3, irate3;

  assert(rank2 != -1 && len(a) <= (1 << max(0, rank2)));

  static bool prepared = 0;
  if (!prepared) {
    prepared = 1;
    root[rank2] = mint::ntt_info().se;
    iroot[rank2] = mint(1) / root[rank2];
    FOR_R(i, rank2) {
      root[i] = root[i + 1] * root[i + 1];
      iroot[i] = iroot[i + 1] * iroot[i + 1];
    }
    mint prod = 1, iprod = 1;
    for (int i = 0; i <= rank2 - 2; i++) {
      rate2[i] = root[i + 2] * prod;
      irate2[i] = iroot[i + 2] * iprod;
      prod *= iroot[i + 2];
      iprod *= root[i + 2];
    }
    prod = 1, iprod = 1;
    for (int i = 0; i <= rank2 - 3; i++) {
      rate3[i] = root[i + 3] * prod;
      irate3[i] = iroot[i + 3] * iprod;
      prod *= iroot[i + 3];
      iprod *= root[i + 3];
    }
  }

  int n = int(a.size());
  int h = topbit(n);
  assert(n == 1 << h);
  if (!inverse) {
    int len = 0;
    while (len < h) {
      if (h - len == 1) {
        int p = 1 << (h - len - 1);
        mint rot = 1;
        FOR(s, 1 << len) {
          int offset = s << (h - len);
          FOR(i, p) {
            auto l = a[i + offset];
            auto r = a[i + offset + p] * rot;
            a[i + offset] = l + r;
            a[i + offset + p] = l - r;
          }
          rot *= rate2[topbit(~s & -~s)];
        }
        len++;
      } else {
        int p = 1 << (h - len - 2);
        mint rot = 1, imag = root[2];
        for (int s = 0; s < (1 << len); s++) {
          mint rot2 = rot * rot;
          mint rot3 = rot2 * rot;
          int offset = s << (h - len);
          for (int i = 0; i < p; i++) {
            u64 mod2 = u64(mod) * mod;
            u64 a0 = a[i + offset].val;
            u64 a1 = u64(a[i + offset + p].val) * rot.val;
            u64 a2 = u64(a[i + offset + 2 * p].val) * rot2.val;
            u64 a3 = u64(a[i + offset + 3 * p].val) * rot3.val;
            u64 a1na3imag = (a1 + mod2 - a3) % mod * imag.val;
            u64 na2 = mod2 - a2;
            a[i + offset] = a0 + a2 + a1 + a3;
            a[i + offset + 1 * p] = a0 + a2 + (2 * mod2 - (a1 + a3));
            a[i + offset + 2 * p] = a0 + na2 + a1na3imag;
            a[i + offset + 3 * p] = a0 + na2 + (mod2 - a1na3imag);
          }
          rot *= rate3[topbit(~s & -~s)];
        }
        len += 2;
      }
    }
  } else {
    mint coef = mint(1) / mint(len(a));
    FOR(i, len(a)) a[i] *= coef;
    int len = h;
    while (len) {
      if (len == 1) {
        int p = 1 << (h - len);
        mint irot = 1;
        FOR(s, 1 << (len - 1)) {
          int offset = s << (h - len + 1);
          FOR(i, p) {
            u64 l = a[i + offset].val;
            u64 r = a[i + offset + p].val;
            a[i + offset] = l + r;
            a[i + offset + p] = (mod + l - r) * irot.val;
          }
          irot *= irate2[topbit(~s & -~s)];
        }
        len--;
      } else {
        int p = 1 << (h - len);
        mint irot = 1, iimag = iroot[2];
        FOR(s, (1 << (len - 2))) {
          mint irot2 = irot * irot;
          mint irot3 = irot2 * irot;
          int offset = s << (h - len + 2);
          for (int i = 0; i < p; i++) {
            u64 a0 = a[i + offset + 0 * p].val;
            u64 a1 = a[i + offset + 1 * p].val;
            u64 a2 = a[i + offset + 2 * p].val;
            u64 a3 = a[i + offset + 3 * p].val;
            u64 x = (mod + a2 - a3) * iimag.val % mod;
            a[i + offset] = a0 + a1 + a2 + a3;
            a[i + offset + 1 * p] = (a0 + mod - a1 + x) * irot.val;
            a[i + offset + 2 * p] = (a0 + a1 + 2 * mod - a2 - a3) * irot2.val;
            a[i + offset + 3 * p] = (a0 + 2 * mod - a1 - x) * irot3.val;
          }
          irot *= irate3[topbit(~s & -~s)];
        }
        len -= 2;
      }
    }
  }
}
#line 1 "poly/fft.hpp"
namespace CFFT {
using real = double;

struct C {
  real x, y;

  C() : x(0), y(0) {}

  C(real x, real y) : x(x), y(y) {}
  inline C operator+(const C& c) const { return C(x + c.x, y + c.y); }
  inline C operator-(const C& c) const { return C(x - c.x, y - c.y); }
  inline C operator*(const C& c) const {
    return C(x * c.x - y * c.y, x * c.y + y * c.x);
  }

  inline C conj() const { return C(x, -y); }
};

const real PI = acosl(-1);
int base = 1;
vector<C> rts = {{0, 0}, {1, 0}};
vector<int> rev = {0, 1};

void ensure_base(int nbase) {
  if (nbase <= base) return;
  rev.resize(1 << nbase);
  rts.resize(1 << nbase);
  for (int i = 0; i < (1 << nbase); i++) {
    rev[i] = (rev[i >> 1] >> 1) + ((i & 1) << (nbase - 1));
  }
  while (base < nbase) {
    real angle = PI * 2.0 / (1 << (base + 1));
    for (int i = 1 << (base - 1); i < (1 << base); i++) {
      rts[i << 1] = rts[i];
      real angle_i = angle * (2 * i + 1 - (1 << base));
      rts[(i << 1) + 1] = C(cos(angle_i), sin(angle_i));
    }
    ++base;
  }
}

void fft(vector<C>& a, int n) {
  assert((n & (n - 1)) == 0);
  int zeros = __builtin_ctz(n);
  ensure_base(zeros);
  int shift = base - zeros;
  for (int i = 0; i < n; i++) {
    if (i < (rev[i] >> shift)) { swap(a[i], a[rev[i] >> shift]); }
  }
  for (int k = 1; k < n; k <<= 1) {
    for (int i = 0; i < n; i += 2 * k) {
      for (int j = 0; j < k; j++) {
        C z = a[i + j + k] * rts[j + k];
        a[i + j + k] = a[i + j] - z;
        a[i + j] = a[i + j] + z;
      }
    }
  }
}
} // namespace CFFT
#line 9 "poly/convolution.hpp"

template <class mint>
vector<mint> convolution_ntt(vector<mint> a, vector<mint> b) {
  if (a.empty() || b.empty()) return {};
  int n = int(a.size()), m = int(b.size());
  int sz = 1;
  while (sz < n + m - 1) sz *= 2;

  // sz = 2^k のときの高速化。分割統治的なやつで損しまくるので。

  if ((n + m - 3) <= sz / 2) {
    auto a_last = a.back(), b_last = b.back();
    a.pop_back(), b.pop_back();
    auto c = convolution(a, b);
    c.resize(n + m - 1);
    c[n + m - 2] = a_last * b_last;
    FOR(i, len(a)) c[i + len(b)] += a[i] * b_last;
    FOR(i, len(b)) c[i + len(a)] += b[i] * a_last;
    return c;
  }

  a.resize(sz), b.resize(sz);
  bool same = a == b;
  ntt(a, 0);
  if (same) {
    b = a;
  } else {
    ntt(b, 0);
  }
  FOR(i, sz) a[i] *= b[i];
  ntt(a, 1);
  a.resize(n + m - 1);
  return a;
}

template <typename mint>
vector<mint> convolution_garner(const vector<mint>& a, const vector<mint>& b) {
  int n = len(a), m = len(b);
  if (!n || !m) return {};
  static constexpr int p0 = 167772161;
  static constexpr int p1 = 469762049;
  static constexpr int p2 = 754974721;
  using mint0 = modint<p0>;
  using mint1 = modint<p1>;
  using mint2 = modint<p2>;
  vc<mint0> a0(n), b0(m);
  vc<mint1> a1(n), b1(m);
  vc<mint2> a2(n), b2(m);
  FOR(i, n) a0[i] = a[i].val, a1[i] = a[i].val, a2[i] = a[i].val;
  FOR(i, m) b0[i] = b[i].val, b1[i] = b[i].val, b2[i] = b[i].val;
  auto c0 = convolution_ntt<mint0>(a0, b0);
  auto c1 = convolution_ntt<mint1>(a1, b1);
  auto c2 = convolution_ntt<mint2>(a2, b2);
  vc<mint> c(len(c0));
  FOR(i, n + m - 1) {
    c[i] = CRT3<mint, p0, p1, p2>(c0[i].val, c1[i].val, c2[i].val);
  }
  return c;
}

template <typename R>
vc<double> convolution_fft(const vc<R>& a, const vc<R>& b) {
  using C = CFFT::C;
  int need = (int)a.size() + (int)b.size() - 1;
  int nbase = 1;
  while ((1 << nbase) < need) nbase++;
  CFFT::ensure_base(nbase);
  int sz = 1 << nbase;
  vector<C> fa(sz);
  for (int i = 0; i < sz; i++) {
    double x = (i < (int)a.size() ? a[i] : 0);
    double y = (i < (int)b.size() ? b[i] : 0);
    fa[i] = C(x, y);
  }
  CFFT::fft(fa, sz);
  C r(0, -0.25 / (sz >> 1)), s(0, 1), t(0.5, 0);
  for (int i = 0; i <= (sz >> 1); i++) {
    int j = (sz - i) & (sz - 1);
    C z = (fa[j] * fa[j] - (fa[i] * fa[i]).conj()) * r;
    fa[j] = (fa[i] * fa[i] - (fa[j] * fa[j]).conj()) * r;
    fa[i] = z;
  }
  for (int i = 0; i < (sz >> 1); i++) {
    C A0 = (fa[i] + fa[i + (sz >> 1)]) * t;
    C A1 = (fa[i] - fa[i + (sz >> 1)]) * t * CFFT::rts[(sz >> 1) + i];
    fa[i] = A0 + A1 * s;
  }
  CFFT::fft(fa, sz >> 1);
  vector<double> ret(need);
  for (int i = 0; i < need; i++) {
    ret[i] = (i & 1 ? fa[i >> 1].y : fa[i >> 1].x);
  }
  return ret;
}

vector<ll> convolution(const vector<ll>& a, const vector<ll>& b) {
  int n = len(a), m = len(b);
  if (!n || !m) return {};
  if (min(n, m) <= 2500) return convolution_naive(a, b);
  ll abs_sum_a = 0, abs_sum_b = 0;
  ll LIM = 1e15;
  FOR(i, n) abs_sum_a = min(LIM, abs_sum_a + abs(a[i]));
  FOR(i, m) abs_sum_b = min(LIM, abs_sum_b + abs(b[i]));
  if (i128(abs_sum_a) * abs_sum_b < 1e15) {
    vc<double> c = convolution_fft<ll>(a, b);
    vc<ll> res(len(c));
    FOR(i, len(c)) res[i] = ll(floor(c[i] + .5));
    return res;
  }

  static constexpr unsigned long long MOD1 = 754974721; // 2^24

  static constexpr unsigned long long MOD2 = 167772161; // 2^25

  static constexpr unsigned long long MOD3 = 469762049; // 2^26

  static constexpr unsigned long long M2M3 = MOD2 * MOD3;
  static constexpr unsigned long long M1M3 = MOD1 * MOD3;
  static constexpr unsigned long long M1M2 = MOD1 * MOD2;
  static constexpr unsigned long long M1M2M3 = MOD1 * MOD2 * MOD3;

  static const unsigned long long i1 = mod_inv(MOD2 * MOD3, MOD1);
  static const unsigned long long i2 = mod_inv(MOD1 * MOD3, MOD2);
  static const unsigned long long i3 = mod_inv(MOD1 * MOD2, MOD3);

  using mint1 = modint<MOD1>;
  using mint2 = modint<MOD2>;
  using mint3 = modint<MOD3>;

  vc<mint1> a1(n), b1(m);
  vc<mint2> a2(n), b2(m);
  vc<mint3> a3(n), b3(m);
  FOR(i, n) a1[i] = a[i], a2[i] = a[i], a3[i] = a[i];
  FOR(i, m) b1[i] = b[i], b2[i] = b[i], b3[i] = b[i];

  auto c1 = convolution_ntt<mint1>(a1, b1);
  auto c2 = convolution_ntt<mint2>(a2, b2);
  auto c3 = convolution_ntt<mint3>(a3, b3);

  vc<ll> c(n + m - 1);
  FOR(i, n + m - 1) {
    u64 x = 0;
    x += (c1[i].val * i1) % MOD1 * M2M3;
    x += (c2[i].val * i2) % MOD2 * M1M3;
    x += (c3[i].val * i3) % MOD3 * M1M2;
    ll diff = c1[i].val - ((long long)(x) % (long long)(MOD1));
    if (diff < 0) diff += MOD1;
    static constexpr unsigned long long offset[5]
        = {0, 0, M1M2M3, 2 * M1M2M3, 3 * M1M2M3};
    x -= offset[diff % 5];
    c[i] = x;
  }
  return c;
}

template <typename mint>
vc<mint> convolution(const vc<mint>& a, const vc<mint>& b) {
  int n = len(a), m = len(b);
  if (!n || !m) return {};
  if (mint::can_ntt()) {
    if (min(n, m) <= 50) return convolution_karatsuba<mint>(a, b);
    return convolution_ntt(a, b);
  }
  if (min(n, m) <= 200) return convolution_karatsuba<mint>(a, b);
  return convolution_garner(a, b);
}
#line 4 "poly/convolution_all.hpp"

template <typename T>
vc<T> convolution_all(vc<vc<T>>& polys) {
  if (len(polys) == 0) return {T(1)};
  while (1) {
    int n = len(polys);
    if (n == 1) break;
    int m = ceil(n, 2);
    FOR(i, m) {
      if (2 * i + 1 == n) {
        polys[i] = polys[2 * i];
      } else {
        polys[i] = convolution(polys[2 * i], polys[2 * i + 1]);
      }
    }
    polys.resize(m);
  }
  return polys[0];
}

using mint = modint998;

using poly = vc<mint>;

void solve() {
    INT(n, k);
    VEC(int, a, k);
    poly f(10);
    each(i, a) f[i] += 1;
    vc<poly> F(n / 2, f);
    auto dp = convolution_all(F);
    mint ans = 0;
    rep(i, len(dp)) ans += dp[i] * dp[i];
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