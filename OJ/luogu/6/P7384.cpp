// #ifdef ONLINE_JUDGE
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
// #endif
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
const int N = 1e6 + 10;

struct DSU {
    std::vector<int> f, siz;
    
    DSU() {}
    DSU(int n) {
        init(n);
    }
    
    void init(int n) {
        f.resize(n);
        std::iota(f.begin(), f.end(), 0);
        siz.assign(n, 1);
    }
    
    int find(int x) {
        while (x != f[x]) {
            x = f[x] = f[f[x]];
        }
        return x;
    }
    
    bool same(int x, int y) {
        return find(x) == find(y);
    }
    
    bool merge(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) {
            return false;
        }
        siz[x] += siz[y];
        f[y] = x;
        return true;
    }
    
    int size(int x) {
        return siz[find(x)];
    }
};

#line 1 "graph/ds/tree_wavelet_matrix.hpp"

#line 1 "ds/bit_vector.hpp"
struct Bit_Vector {
  vc<pair<u32, u32>> dat;
  Bit_Vector(int n) { dat.assign((n + 63) >> 5, {0, 0}); }

  void set(int i) { dat[i >> 5].fi |= u32(1) << (i & 31); }

  void build() {
    FOR(i, len(dat) - 1) dat[i + 1].se = dat[i].se + popcnt(dat[i].fi);
  }

  // [0, k) 内の 1 の個数
  int rank(int k, bool f = 1) {
    auto [a, b] = dat[k >> 5];
    int ret = b + popcnt(a & ((u32(1) << (k & 31)) - 1));
    return (f ? ret : k - ret);
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
#line 3 "ds/wavelet_matrix.hpp"

// 座圧するかどうかを COMPRESS で指定する

// xor 的な使い方をする場合には、コンストラクタで log を渡すこと

template <typename T, bool COMPRESS, typename Monoid = Monoid_Add<T>>
struct Wavelet_Matrix {
  using MX = Monoid;
  using X = typename MX::value_type;
  static_assert(MX::commute);
  int N, lg;
  vector<int> mid;
  vector<Bit_Vector> bv;
  vc<T> key;
  bool set_log;
  vvc<X> cumsum;

  Wavelet_Matrix() {}

  // 和を使わないなら、SUM_data は空でよい

  Wavelet_Matrix(vc<T> A, vc<X> SUM_data = {}, int log = -1) {
    build(A, SUM_data, log);
  }

  void build(vc<T> A, vc<X> SUM_data = {}, int log = -1) {
    N = len(A), lg = log, set_log = (log != -1);
    bool MAKE_SUM = !(SUM_data.empty());
    vc<X>& S = SUM_data;
    if (COMPRESS) {
      assert(!set_log);
      key.reserve(N);
      vc<int> I = argsort(A);
      for (auto&& i: I) {
        if (key.empty() || key.back() != A[i]) key.eb(A[i]);
        A[i] = len(key) - 1;
      }
      key.shrink_to_fit();
    }
    if (lg == -1) lg = __lg(max<ll>(MAX(A), 1)) + 1;
    mid.resize(lg);
    bv.assign(lg, Bit_Vector(N));
    if (MAKE_SUM) cumsum.assign(1 + lg, vc<X>(N + 1, MX::unit()));
    S.resize(N);
    vc<T> A0(N), A1(N);
    vc<X> S0(N), S1(N);
    FOR_R(d, -1, lg) {
      int p0 = 0, p1 = 0;
      if (MAKE_SUM) {
        FOR(i, N) { cumsum[d + 1][i + 1] = MX::op(cumsum[d + 1][i], S[i]); }
      }
      if (d == -1) break;
      FOR(i, N) {
        bool f = (A[i] >> d & 1);
        if (!f) {
          if (MAKE_SUM) S0[p0] = S[i];
          A0[p0++] = A[i];
        }
        if (f) {
          if (MAKE_SUM) S1[p1] = S[i];
          bv[d].set(i), A1[p1++] = A[i];
        }
      }
      mid[d] = p0;
      bv[d].build();
      swap(A, A0), swap(S, S0);
      FOR(i, p1) A[p0 + i] = A1[i], S[p0 + i] = S1[i];
    }
  }

  // xor した結果で [a, b) に収まるものを数える

  int count(int L, int R, T a, T b, T xor_val = 0) {
    return prefix_count(L, R, b, xor_val) - prefix_count(L, R, a, xor_val);
  }

  int count(vc<pair<int, int>> segments, T a, T b, T xor_val = 0) {
    int res = 0;
    for (auto&& [L, R]: segments) res += count(L, R, a, b, xor_val);
    return res;
  }

  // xor した結果で、[L, R) の中で k>=0 番目と prefix sum

  pair<T, X> kth_value_and_sum(int L, int R, int k, T xor_val = 0) {
    assert(!cumsum.empty());
    if (xor_val != 0) assert(set_log);
    assert(0 <= k && k <= R - L);
    if (k == R - L) { return {infty<T>, sum_all(L, R)}; }
    int cnt = 0;
    X sm = MX::unit();
    T ret = 0;
    for (int d = lg - 1; d >= 0; --d) {
      bool f = (xor_val >> d) & 1;
      int l0 = bv[d].rank(L, 0), r0 = bv[d].rank(R, 0);
      int c = (f ? (R - L) - (r0 - l0) : (r0 - l0));
      if (cnt + c > k) {
        if (!f) L = l0, R = r0;
        if (f) L += mid[d] - l0, R += mid[d] - r0;
      } else {
        X s = (f ? get(d, L + mid[d] - l0, R + mid[d] - r0) : get(d, l0, r0));
        cnt += c, ret |= T(1) << d, sm = MX::op(sm, s);
        if (!f) L += mid[d] - l0, R += mid[d] - r0;
        if (f) L = l0, R = r0;
      }
    }
    sm = MX::op(sm, get(0, L, L + k - cnt));
    if (COMPRESS) ret = key[ret];
    return {ret, sm};
  }

  // xor した結果で、[L, R) の中で k>=0 番目と prefix sum

  pair<T, X> kth_value_and_sum(vc<pair<int, int>> segments, int k,
                               T xor_val = 0) {
    assert(!cumsum.empty());
    if (xor_val != 0) assert(set_log);
    int total_len = 0;
    for (auto&& [L, R]: segments) total_len += R - L;
    assert(0 <= k && k <= total_len);
    if (k == total_len) { return {infty<T>, sum_all(segments)}; }
    int cnt = 0;
    X sm = MX::unit();
    T ret = 0;
    for (int d = lg - 1; d >= 0; --d) {
      bool f = (xor_val >> d) & 1;
      int c = 0;
      for (auto&& [L, R]: segments) {
        int l0 = bv[d].rank(L, 0), r0 = bv[d].rank(R, 0);
        c += (f ? (R - L) - (r0 - l0) : (r0 - l0));
      }
      if (cnt + c > k) {
        for (auto&& [L, R]: segments) {
          int l0 = bv[d].rank(L, 0), r0 = bv[d].rank(R, 0);
          if (!f) L = l0, R = r0;
          if (f) L += mid[d] - l0, R += mid[d] - r0;
        }
      } else {
        cnt += c, ret |= T(1) << d;
        for (auto&& [L, R]: segments) {
          int l0 = bv[d].rank(L, 0), r0 = bv[d].rank(R, 0);
          X s = (f ? get(d, L + mid[d] - l0, R + mid[d] - r0) : get(d, l0, r0));
          sm = MX::op(sm, s);
          if (!f) L += mid[d] - l0, R += mid[d] - r0;
          if (f) L = l0, R = r0;
        }
      }
    }
    for (auto&& [L, R]: segments) {
      int t = min(R - L, k - cnt);
      sm = MX::op(sm, get(0, L, L + t));
      cnt += t;
    }
    if (COMPRESS) ret = key[ret];
    return {ret, sm};
  }

  // xor した結果で、[L, R) の中で k>=0 番目

  T kth(int L, int R, int k, T xor_val = 0) {
    if (xor_val != 0) assert(set_log);
    assert(0 <= k && k < R - L);
    int cnt = 0;
    T ret = 0;
    for (int d = lg - 1; d >= 0; --d) {
      bool f = (xor_val >> d) & 1;
      int l0 = bv[d].rank(L, 0), r0 = bv[d].rank(R, 0);
      int c = (f ? (R - L) - (r0 - l0) : (r0 - l0));
      if (cnt + c > k) {
        if (!f) L = l0, R = r0;
        if (f) L += mid[d] - l0, R += mid[d] - r0;
      } else {
        cnt += c, ret |= T(1) << d;
        if (!f) L += mid[d] - l0, R += mid[d] - r0;
        if (f) L = l0, R = r0;
      }
    }
    if (COMPRESS) ret = key[ret];
    return ret;
  }

  T kth(vc<pair<int, int>> segments, int k, T xor_val = 0) {
    int total_len = 0;
    for (auto&& [L, R]: segments) total_len += R - L;
    assert(0 <= k && k < total_len);
    int cnt = 0;
    T ret = 0;
    for (int d = lg - 1; d >= 0; --d) {
      bool f = (xor_val >> d) & 1;
      int c = 0;
      for (auto&& [L, R]: segments) {
        int l0 = bv[d].rank(L, 0), r0 = bv[d].rank(R, 0);
        c += (f ? (R - L) - (r0 - l0) : (r0 - l0));
      }
      if (cnt + c > k) {
        for (auto&& [L, R]: segments) {
          int l0 = bv[d].rank(L, 0), r0 = bv[d].rank(R, 0);
          if (!f) L = l0, R = r0;
          if (f) L += mid[d] - l0, R += mid[d] - r0;
        }
      } else {
        cnt += c, ret |= T(1) << d;
        for (auto&& [L, R]: segments) {
          int l0 = bv[d].rank(L, 0), r0 = bv[d].rank(R, 0);
          if (!f) L += mid[d] - l0, R += mid[d] - r0;
          if (f) L = l0, R = r0;
        }
      }
    }
    if (COMPRESS) ret = key[ret];
    return ret;
  }

  // xor した結果で、[L, R) の中で中央値。

  // LOWER = true：下側中央値、false：上側中央値

  T median(bool UPPER, int L, int R, T xor_val = 0) {
    int n = R - L;
    int k = (UPPER ? n / 2 : (n - 1) / 2);
    return kth(L, R, k, xor_val);
  }

  T median(bool UPPER, vc<pair<int, int>> segments, T xor_val = 0) {
    int n = 0;
    for (auto&& [L, R]: segments) n += R - L;
    int k = (UPPER ? n / 2 : (n - 1) / 2);
    return kth(segments, k, xor_val);
  }

  // xor した結果で [k1, k2) 番目であるところの SUM_data の和

  X sum(int L, int R, int k1, int k2, T xor_val = 0) {
    X add = prefix_sum(L, R, k2, xor_val);
    X sub = prefix_sum(L, R, k1, xor_val);
    return MX::op(add, MX::inverse(sub));
  }

  X sum_all(int L, int R) { return get(lg, L, R); }

  X sum_all(vc<pair<int, int>> segments) {
    X sm = MX::unit();
    for (auto&& [L, R]: segments) { sm = MX::op(sm, get(lg, L, R)); }
    return sm;
  }

  // check(cnt, prefix sum) が true となるような最大の (cnt, sum)

  template <typename F>
  pair<int, X> max_right(F check, int L, int R, T xor_val = 0) {
    assert(check(0, MX::unit()));
    if (xor_val != 0) assert(set_log);
    if (check(R - L, get(lg, L, R))) return {R - L, get(lg, L, R)};
    int cnt = 0;
    X sm = MX::unit();
    for (int d = lg - 1; d >= 0; --d) {
      bool f = (xor_val >> d) & 1;
      int l0 = bv[d].rank(L, 0), r0 = bv[d].rank(R, 0);
      int c = (f ? (R - L) - (r0 - l0) : (r0 - l0));
      X s = (f ? get(d, L + mid[d] - l0, R + mid[d] - r0) : get(d, l0, r0));
      if (check(cnt + c, MX::op(sm, s))) {
        cnt += c, sm = MX::op(sm, s);
        if (f) L = l0, R = r0;
        if (!f) L += mid[d] - l0, R += mid[d] - r0;
      } else {
        if (!f) L = l0, R = r0;
        if (f) L += mid[d] - l0, R += mid[d] - r0;
      }
    }
    int k = binary_search(
        [&](int k) -> bool {
          return check(cnt + k, MX::op(sm, get(0, L, L + k)));
        },
        0, R - L);
    cnt += k;
    sm = MX::op(sm, get(0, L, L + k));
    return {cnt, sm};
  }

private:
  inline X get(int d, int L, int R) {
    assert(!cumsum.empty());
    return MX::op(MX::inverse(cumsum[d][L]), cumsum[d][R]);
  }

  // xor した結果で [0, x) に収まるものを数える

  int prefix_count(int L, int R, T x, T xor_val = 0) {
    if (xor_val != 0) assert(set_log);
    x = (COMPRESS ? LB(key, x) : x);
    if (x == 0) return 0;
    if (x >= (1 << lg)) return R - L;
    int cnt = 0;
    FOR_R(d, lg) {
      bool add = (x >> d) & 1;
      bool f = ((xor_val) >> d) & 1;
      int l0 = bv[d].rank(L, 0), r0 = bv[d].rank(R, 0);
      int kf = (f ? (R - L) - (r0 - l0) : (r0 - l0));
      if (add) {
        cnt += kf;
        if (f) { L = l0, R = r0; }
        if (!f) { L += mid[d] - l0, R += mid[d] - r0; }
      } else {
        if (!f) L = l0, R = r0;
        if (f) L += mid[d] - l0, R += mid[d] - r0;
      }
    }
    return cnt;
  }

  // xor した結果で [0, k) 番目のものの和

  X prefix_sum(int L, int R, int k, T xor_val = 0) {
    return kth_value_and_sum(L, R, k, xor_val).se;
  }

  // xor した結果で [0, k) 番目のものの和

  X prefix_sum(vc<pair<int, int>> segments, int k, T xor_val = 0) {
    return kth_value_and_sum(segments, k, xor_val).se;
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
#line 4 "graph/ds/tree_wavelet_matrix.hpp"

// https://atcoder.jp/contests/pakencamp-2022-day1/tasks/pakencamp_2022_day1_j
// https://atcoder.jp/contests/utpc2011/tasks/utpc2011_12
template <typename TREE, bool edge, typename T, bool COMPRESS,
          typename Monoid = Monoid_Add<T>>
struct Tree_Wavelet_Matrix {
  TREE& tree;
  int N;
  using WM = Wavelet_Matrix<T, COMPRESS, Monoid_Add<T>>;
  using X = typename Monoid::value_type;
  WM wm;

  Tree_Wavelet_Matrix(TREE& tree, vc<T> A, vc<X> SUM_data = {}, int log = -1)
      : tree(tree), N(tree.N) {
    vc<X>& S = SUM_data;
    vc<T> A1;
    vc<X> S1;
    A1.resize(N);
    if (!S.empty()) S1.resize(N);
    if (!edge) {
      assert(len(A) == N && (len(S) == 0 || len(S) == N));
      FOR(v, N) A1[tree.LID[v]] = A[v];
      if (len(S) == N) { FOR(v, N) S1[tree.LID[v]] = S[v]; }
      wm.build(A1, S1, log);
    } else {
      assert(len(A) == N - 1 && (len(S) == 0 || len(S) == N - 1));
      if (!S.empty()) {
        FOR(e, N - 1) { S1[tree.LID[tree.e_to_v(e)]] = S[e]; }
      }
      FOR(e, N - 1) { A1[tree.LID[tree.e_to_v(e)]] = A[e]; }
      wm.build(A1, S1, log);
    }
  }

  // xor した結果で [a, b) に収まるものを数える
  int count_path(int s, int t, T a, T b, T xor_val = 0) {
    return wm.count(get_segments(s, t), a, b, xor_val);
  }

  // xor した結果で [a, b) に収まるものを数える
  int count_subtree(int u, T a, T b, T xor_val = 0) {
    int l = tree.LID[u], r = tree.RID[u];
    return wm.count(l + edge, r, a, b, xor_val);
  }

  // xor した結果で、[L, R) の中で k>=0 番目と prefix sum
  pair<T, X> kth_value_and_sum_path(int s, int t, int k, T xor_val = 0) {
    return wm.kth_value_and_sum(get_segments(s, t), k, xor_val);
  }

  // xor した結果で、[L, R) の中で k>=0 番目と prefix sum
  pair<T, X> kth_value_and_sum_subtree(int u, int k, T xor_val = 0) {
    int l = tree.LID[u], r = tree.RID[u];
    return wm.kth_value_and_sum(l + edge, r, k, xor_val);
  }

  // xor した結果で、[L, R) の中で k>=0 番目
  T kth_path(int s, int t, int k, T xor_val = 0) {
    return wm.kth(get_segments(s, t), k, xor_val);
  }

  // xor した結果で、[L, R) の中で k>=0 番目
  T kth_subtree(int u, int k, T xor_val = 0) {
    int l = tree.LID[u], r = tree.RID[u];
    return wm.kth(l + edge, r, k, xor_val);
  }

  // xor した結果で、[L, R) の中で中央値。
  // LOWER = true：下側中央値、false：上側中央値
  T median_path(bool UPPER, int s, int t, T xor_val = 0) {
    return wm.median(UPPER, get_segments(s, t), xor_val);
  }

  T median_subtree(bool UPPER, int u, T xor_val = 0) {
    int l = tree.LID[u], r = tree.RID[u];
    return wm.median(UPPER, l + edge, r, xor_val);
  }

  // xor した結果で [k1, k2) 番目であるところの SUM_data の和
  X sum_path(int s, int t, int k1, int k2, T xor_val = 0) {
    return wm.sum(get_segments(s, t), k1, k2, xor_val);
  }

  // xor した結果で [k1, k2) 番目であるところの SUM_data の和
  X sum_subtree(int u, int k1, int k2, T xor_val = 0) {
    int l = tree.LID[u], r = tree.RID[u];
    return wm.sum(l + edge, r, k1, k2, xor_val);
  }

  X sum_all_path(int s, int t) { return wm.sum_all(get_segments(s, t)); }

  X sum_all_subtree(int u) {
    int l = tree.LID[u], r = tree.RID[u];
    return wm.sum_all(l + edge, r);
  }

private:
  vc<pair<int, int>> get_segments(int s, int t) {
    vc<pair<int, int>> segments = tree.get_path_decomposition(s, t, edge);
    for (auto&& [a, b]: segments) {
      if (a >= b) swap(a, b);
      ++b;
    }
    return segments;
  }
};

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
    int k = 31 - __builtin_clz(L ^ R);
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
    INT(n, m, q);
    VEC(ll, a, n);
    rep(_, n) a.pb(infty<int>);
    using T = array<int, 3>;
    VEC(T, E, m);
    sort(all(E), [] (auto& i, auto& j) { return i[2] < j[2]; });
    DSU dsu(2 * n);
    Graph<int> G(2 * n);
    int root = n;
    vi val(2 * n);
    each(u, v, w, E) {
        u--, v--;
        u = dsu.find(u), v = dsu.find(v);
        if (!dsu.same(u, v)) {
            G.add(root, u);
            G.add(root, v);
            dsu.merge(root, u);
            dsu.merge(root, v);
            val[root] = w;
            root++;
        }
    }
    set<int> R;
    rep(i, n) R.insert(dsu.find(i));
    each(i, R) G.add(root, i);
    rep(i, root + 1, 2 * n) G.add(i - 1, i);
    root = 2 * n - 1;
    G.build();
    auto tree = Tree<decltype(G)>(G, root);
    Tree_Wavelet_Matrix<decltype(tree), 0, ll, 1> X(tree, a);
    vi cnt(2 * n);
    auto dfs = [&] (auto dfs, int i, int fa) -> void {
        cnt[i] = i < n;
        each(e, G[i]) if (e.to != fa) {
            dfs(dfs, e.to, i);
            cnt[i] += cnt[e.to];
        }
    };
    dfs(dfs, root, -1);
    Static_Tree_Monoid<decltype(tree), Monoid_Max<int>, false> Y(tree, val);
    int ans = 0;
    rep(_, q) {
        INT(u, x, k);
        u = (u ^ ans) % n;
        k = (k ^ ans) % n;
        x ^= ans;
        auto check = [&] (auto e) -> bool {
            return e <= x;
        };
        int r = Y.max_path(check, u, dsu.find(u));
        if (k >= cnt[r]) {
            ans = 0;
            print(-1);
            continue;
        }
        k = cnt[r] - 1 - k;
        ans = X.kth_subtree(r, k);
        print(ans);
    }

    
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
