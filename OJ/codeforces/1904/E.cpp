#ifdef ONLINE_JUDGE
#pragma GCC optimize("Ofast,unroll-loops")
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
using f128 =                __float128;
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
const i128 ONE = 1;
template <typename Iterable>
auto print_all(const Iterable& v, std::string sep = " ", std::string end = "\n") -> decltype(fastio::wt(*v.begin())) {
    for (auto it = v.begin(); it != v.end();) {
        fastio::wt(*it);
        if (++it != v.end()) fastio::wt(sep);
    }
    fastio::wt(end);
}
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
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 1e6 + 10;

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
#line 2 "graph/tree.hpp"

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
#line 3 "graph/ds/lazy_tree_monoid.hpp"

template <typename TREE, typename ActedMonoid, bool edge>
struct Lazy_Tree_Monoid {
  using MX = typename ActedMonoid::Monoid_X;
  using MA = typename ActedMonoid::Monoid_A;
  static_assert(MX::commute);
  using X = typename MX::value_type;
  using A = typename MA::value_type;
  TREE &tree;
  int N;
  Lazy_SegTree<ActedMonoid> seg;

  Lazy_Tree_Monoid(TREE &tree) : tree(tree), N(tree.N) {
    build([](int i) -> X { return MX::unit(); });
  }

  Lazy_Tree_Monoid(TREE &tree, vc<X> &dat) : tree(tree), N(tree.N) {
    build([&](int i) -> X { return dat[i]; });
  }

  template <typename F>
  Lazy_Tree_Monoid(TREE &tree, F f) : tree(tree), N(tree.N) {
    build(f);
  }

  template <typename F>
  void build(F f) {
    vc<X> seg_raw(N, MX::unit());
    if (!edge) {
      seg.build(N, [&](int i) -> X { return f(tree.V[i]); });
    } else {
      seg.build(N, [&](int i) -> X {
        return (i == 0 ? MX::unit() : f(tree.v_to_e(tree.V[i])));
      });
    }
  }

  void set(int i, X x) {
    if constexpr (edge) i = tree.e_to_v(i);
    i = tree.LID[i];
    seg.set(i, x);
  }

  X get(int v) { return seg.get(tree.LID[v]); }
  vc<X> get_all() {
    vc<X> dat = seg.get_all();
    if (!edge) {
      vc<X> res(N);
      FOR(v, N) res[v] = dat[tree.LID[v]];
      return res;
    } else {
      vc<X> res(N - 1);
      FOR(i, N - 1) { res[i] = dat[tree.LID[tree.e_to_v(i)]]; }
      return res;
    }
  }

  X prod_path(int u, int v) {
    auto pd = tree.get_path_decomposition(u, v, edge);
    X val = MX::unit();
    for (auto &&[a, b]: pd) {
      X x = get_prod(a, b);
      val = MX::op(val, x);
    }
    return val;
  }

  X prod_subtree(int u) {
    int l = tree.LID[u], r = tree.RID[u];
    return seg.prod(l + edge, r);
  }

  X prod_all() { return seg.prod_all(); }

  void apply_path(int u, int v, A a) {
    auto pd = tree.get_path_decomposition(u, v, edge);
    for (auto &&[x, y]: pd) {
      int l = min(x, y), r = max(x, y);
      seg.apply(l, r + 1, a);
    }
  }

  void apply_subtree(int u, A a) {
    int l = tree.LID[u], r = tree.RID[u];
    return seg.apply(l + edge, r, a);
  }

  void apply_outtree(int u, A a) {
    int l = tree.LID[u], r = tree.RID[u];
    seg.apply(0 + edge, l + edge, a);
    seg.apply(r, N, a);
  }

  template <class F>
  int max_path(F check, int u, int v) {
    if constexpr (edge) return max_path_edge(check, u, v);
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

        auto i = seg.max_right(check_tmp, a);
        return (i == a ? u : tree.V[i - 1]);
      } else {
        // 上り

        auto i = seg.min_left(check_tmp, a + 1);
        if (i == a + 1) return u;
        return tree.V[i];
      }
    }
    return v;
  }

  // closed range [a,b] を heavy path の形式に応じて

  inline X get_prod(int a, int b) {
    return (a <= b ? seg.prod(a, b + 1) : seg.prod(b, a + 1));
  }

private:
  template <class F>
  int max_path_edge(F &check, int u, int v) {
    assert(edge);
    if (!check(MX::unit())) return -1;
    int lca = tree.lca(u, v);
    auto pd = tree.get_path_decomposition(u, lca, edge);
    X val = MX::unit();

    // climb

    for (auto &&[a, b]: pd) {
      assert(a >= b);
      X x = seg.prod(b, a + 1);
      if (check(MX::op(val, x))) {
        val = MX::op(val, x);
        u = (tree.parent[tree.V[b]]);
        continue;
      }
      auto check_tmp = [&](X x) -> bool { return check(MX::op(val, x)); };
      auto i = seg.min_left(check_tmp, a + 1);
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

#line 2 "alg/monoid/add.hpp"

template <typename X>
struct Monoid_Add {
  using value_type = X;
  static constexpr X op(const X &x, const X &y) noexcept { return x + y; }
  static constexpr X inverse(const X &x) noexcept { return -x; }
  static constexpr X power(const X &x, ll n) noexcept { return X(n) * x; }
  static constexpr X unit() { return X(0); }
  static constexpr bool commute = true;
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
#line 3 "alg/acted_monoid/max_add.hpp"

template <typename E>
struct ActedMonoid_Max_Add {
  using Monoid_X = Monoid_Max<E>;
  using Monoid_A = Monoid_Add<E>;
  using X = typename Monoid_X::value_type;
  using A = typename Monoid_A::value_type;
  static constexpr X act(const X &x, const A &a, const ll &size) {
    if (x == -infty<E>) return x;
    return x + a;
  }
};

void solve() {
    INT(n, q);
    Graph G(n);
    G.read_tree();
    Tree tree(G);
    vvc<pair<vi, int>> Q(n);
    rep(idx, q) {
        INT(x, k);
        x--;
        VEC(int, a, k);
        each(i, a) i--;
        Q[x].eb(a, idx);
    }
    vll dat = {tree.depth.begin(), tree.depth.end()};
    Lazy_Tree_Monoid<decltype(tree), ActedMonoid_Max_Add<ll>, false> X(tree, dat);
    vi ans(q);
    auto dfs = [&] (auto dfs, int i, int fa) -> void {
        each(lst, idx, Q[i]) {
            each(a, lst) {
                if (tree.in_subtree(i, a)) {
                    int b = tree.jump(a, i, 1);
                    X.apply_outtree(b, -infty<int>);
                } else {
                    X.apply_subtree(a, -infty<int>);
                }
            }
            ans[idx] = X.prod_all();
            each(a, lst) {
                if (tree.in_subtree(i, a)) {
                    int b = tree.jump(a, i, 1);
                    X.apply_outtree(b, infty<int>);
                } else {
                    X.apply_subtree(a, infty<int>);
                }
            }
        }
        each(e, G[i]) if (e.to != fa) {
            X.apply_outtree(e.to, +1);
            X.apply_subtree(e.to, -1);
            dfs(dfs, e.to, i);
            X.apply_outtree(e.to, -1);
            X.apply_subtree(e.to, +1);
        }
    };
    dfs(dfs, 0, -1);
    print_all(ans, "\n");
    
}

signed main() {
    int T = 1;
    // read(T);
    while (T--) {
        solve();
    }
    return 0;
}