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
    tie(ok, ng) = (check(x) ? make_pair(x, ng) : make_pair(ok, x));
  }
  return ok;
}
template <typename F>
double binary_search_real(F check, double ok, double ng, int iter = 100) {
  while (iter--) {
    double x = (ok + ng) / 2;
    tie(ok, ng) = (check(x) ? make_pair(x, ng) : make_pair(ok, x));
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
template <class T> istream &operator>>(istream &in, vector<T> &v) {
    for(auto& x : v) cin >> x;
    return in;
}
template <class T> ostream &operator<<(ostream &os, const vector<T> &v) {
    for(auto it = begin(v); it != end(v); ++it) {
        if(it == begin(v)) os << *it;
        else os << " " << *it;
    }
    return os;
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
    cin >> p.first >> p.second;
    return in;
}
template <class T, class S> ostream &operator<<(ostream &os, const pair<T, S> &p) {
    os << p.first << " " << p.second;
    return os;
}
template <class T, size_t size> istream &operator>>(istream &in, array<T, size> &v) {
    for(auto& x : v) cin >> x;
    return in;
}
template <class T, size_t size> ostream &operator<<(ostream &os, const array<T, size> &v) {
    for(int i = 0; i < size; i++) {
        if(i == 0) os << v[i];
        else os << " " << v[i];
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

#line 2 "ds/splaytree/splaytree.hpp"
// Node 型を別に定義して使う
template <typename Node, int NODES = 1'000'000>
struct SplayTree {
  Node *pool;
  int pid;
  using np = Node *;
  using X = typename Node::value_type;
  using A = typename Node::operator_type;

  SplayTree() : pid(0) { pool = new Node[NODES]; }

  void reset() { pid = 0; }

  np new_root() { return nullptr; }

  np new_node(const X &x) {
    np n = &(pool[pid++]);
    Node::new_node(n, x);
    return n;
  }

  np new_node(const vc<X> &dat) {
    auto dfs = [&](auto &dfs, int l, int r) -> np {
      if (l == r) return nullptr;
      if (r == l + 1) return new_node(dat[l]);
      int m = (l + r) / 2;
      np l_root = dfs(dfs, l, m);
      np r_root = dfs(dfs, m + 1, r);
      np root = new_node(dat[m]);
      root->l = l_root, root->r = r_root;
      if (l_root) l_root->p = root;
      if (r_root) r_root->p = root;
      root->update();
      return root;
    };
    return dfs(dfs, 0, len(dat));
  }

  u32 get_size(np root) { return (root ? root->size : 0); }

  np merge(np l_root, np r_root) {
    if (!l_root) return r_root;
    if (!r_root) return l_root;
    splay_kth(r_root, 0); // splay したので prop 済
    r_root->l = l_root;
    l_root->p = r_root;
    r_root->update();
    return r_root;
  }
  np merge3(np a, np b, np c) { return merge(merge(a, b), c); }
  np merge4(np a, np b, np c, np d) { return merge(merge(merge(a, b), c), d); }

  pair<np, np> split(np root, u32 k) {
    if (k == 0) return {nullptr, root};
    if (k == (root->size)) return {root, nullptr};
    splay_kth(root, k - 1);
    np right = root->r;
    root->r = nullptr, right->p = nullptr;
    root->update();
    return {root, right};
  }
  tuple<np, np, np> split3(np root, u32 l, u32 r) {
    np nm, nr;
    tie(root, nr) = split(root, r);
    tie(root, nm) = split(root, l);
    return {root, nm, nr};
  }
  tuple<np, np, np, np> split4(np root, u32 i, u32 j, u32 k) {
    np d;
    tie(root, d) = split(root, k);
    auto [a, b, c] = split3(root, i, j);
    return {a, b, c, d};
  }

  // 部分木が区間 [l,r) に対応するようなノードを作って返す
  // そのノードが root になるわけではないので、
  // このノードを参照した後にすぐに splay して根に持ち上げること
  void goto_between(np &root, u32 l, u32 r) {
    if (l == 0 && r == root->size) return;
    if (l == 0) {
      splay_kth(root, r);
      root = root->l;
      return;
    }
    if (r == root->size) {
      splay_kth(root, l - 1);
      root = root->r;
      return;
    }
    splay_kth(root, r);
    np rp = root;
    root = rp->l;
    root->p = nullptr;
    splay_kth(root, l - 1);
    root->p = rp;
    rp->l = root;
    rp->update();
    root = root->r;
  }

  vc<X> get_all(const np &root) {
    vc<X> res;
    auto dfs = [&](auto &dfs, np root) -> void {
      if (!root) return;
      root->prop();
      dfs(dfs, root->l);
      res.eb(root->get());
      dfs(dfs, root->r);
    };
    dfs(dfs, root);
    return res;
  }

  X get(np &root, u32 k) {
    splay_kth(root, k);
    return root->get();
  }

  void set(np &root, u32 k, const X &x) {
    splay_kth(root, k);
    root->set(x);
  }

  void multiply(np &root, u32 k, const X &x) {
    splay_kth(root, k);
    root->multiply(x);
  }

  X prod(np &root, u32 l, u32 r) {
    using Mono = typename Node::Monoid_X;
    if (l == r) return Mono::unit();
    assert(0 <= l && l < r && r <= root->size);
    goto_between(root, l, r);
    X res = root->prod;
    splay(root);
    return res;
  }

  X prod(np &root) {
    using Mono = typename Node::Monoid_X;
    return (root ? root->prod : Mono::unit());
  }

  void apply(np &root, u32 l, u32 r, const A &a) {
    if (l == r) return;
    assert(0 <= l && l < r && r <= root->size);
    goto_between(root, l, r);
    root->apply(a);
    splay(root);
  }
  void apply(np &root, const A &a) {
    if (!root) return;
    root->apply(a);
  }

  void reverse(np &root, u32 l, u32 r) {
    if (l == r) return;
    assert(0 <= l && l < r && r <= root->size);
    goto_between(root, l, r);
    root->reverse();
    splay(root);
  }
  void reverse(np root) {
    if (!root) return;
    root->reverse();
  }

  void rotate(Node *n) {
    // n を根に近づける。prop, update は rotate の外で行う。
    Node *pp, *p, *c;
    p = n->p;
    pp = p->p;
    if (p->l == n) {
      c = n->r;
      n->r = p;
      p->l = c;
    } else {
      c = n->l;
      n->l = p;
      p->r = c;
    }
    if (pp && pp->l == p) pp->l = n;
    if (pp && pp->r == p) pp->r = n;
    n->p = pp;
    p->p = n;
    if (c) c->p = p;
  }

  void splay(Node *me) {
    // これを呼ぶ時点で、me の祖先（me を除く）は既に prop 済であることを仮定
    // 特に、splay 終了時点で me は upd / prop 済である
    me->prop();
    while (me->p) {
      np p = me->p;
      np pp = p->p;
      if (!pp) {
        rotate(me);
        p->update();
        break;
      }
      bool same = (p->l == me && pp->l == p) || (p->r == me && pp->r == p);
      if (same) rotate(p), rotate(me);
      if (!same) rotate(me), rotate(me);
      pp->update(), p->update();
    }
    // me の update は最後だけでよい
    me->update();
  }

  void splay_kth(np &root, u32 k) {
    assert(0 <= k && k < (root->size));
    while (1) {
      u32 sl = (root->l ? root->l->size : 0);
      if (k == sl) break;
      root->prop();
      if (k < sl)
        root = root->l;
      else {
        k -= sl + 1;
        root = root->r;
      }
    }
    splay(root);
  }

  // check(x), 左側のノード全体が check を満たすように切る
  template <typename F>
  pair<np, np> split_max_right(np root, F check) {
    if (!root) return {nullptr, nullptr};
    np c = find_max_right(root, check);
    if (!c) {
      splay(root);
      return {nullptr, root};
    }
    splay(c);
    np right = c->r;
    if (!right) return {c, nullptr};
    right->p = nullptr;
    c->r = nullptr;
    c->update();
    return {c, right};
  }

  // 左側のノード全体の prod が check を満たすように切る
  template <typename F>
  pair<np, np> split_max_right_prod(np root, F check) {
    if (!root) return {nullptr, nullptr};
    np c = find_max_right_prod(root, check);
    if (!c) {
      splay(root);
      return {nullptr, root};
    }
    splay(c);
    np right = c->r;
    if (!right) return {c, nullptr};
    right->p = nullptr;
    c->r = nullptr;
    c->update();
    return {c, right};
  }

  template <typename F>
  np find_max_right(np root, const F &check) {
    // 最後に見つけた ok の点、最後に探索した点
    np last_ok = nullptr, last = nullptr;
    while (root) {
      last = root;
      root->prop();
      if (check(root->x)) {
        last_ok = root;
        root = root->r;
      } else {
        root = root->l;
      }
    }
    splay(last);
    return last_ok;
  }

  template <typename F>
  np find_max_right_prod(np root, const F &check) {
    using Mono = typename Node::Monoid_X;
    X prod = Mono::unit();
    // 最後に見つけた ok の点、最後に探索した点
    np last_ok = nullptr, last = nullptr;
    while (root) {
      last = root;
      root->prop();
      X lprod = prod;
      if (root->l) lprod = Mono::op(lprod, root->l->prod);
      lprod = Mono::op(lprod, root->x);
      if (check(lprod)) {
        prod = lprod;
        last_ok = root;
        root = root->r;
      } else {
        root = root->l;
      }
    }
    splay(last);
    return last_ok;
  }
};
#line 2 "ds/splaytree/splaytree_basic.hpp"

namespace SplayTreeNodes {
template <typename S>
struct Node_Basic {
  using value_type = S;
  using operator_type = int;
  using np = Node_Basic *;

  np p, l, r;
  bool rev;
  S x;
  u32 size;

  static void new_node(np n, const S &x) {
    n->p = n->l = n->r = nullptr;
    n->x = x, n->size = 1, n->rev = 0;
  }

  void update() {
    size = 1;
    if (l) { size += l->size; }
    if (r) { size += r->size; }
  }

  void prop() {
    if (rev) {
      if (l) { l->rev ^= 1, swap(l->l, l->r); }
      if (r) { r->rev ^= 1, swap(r->l, r->r); }
      rev = 0;
    }
  }

  // update, prop 以外で呼ばれるものは、splay 後であることが想定されている。
  // したがってその時点で update, prop 済であることを仮定してよい。
  S get() { return x; }
  void set(const S &xx) {
    x = xx;
    update();
  }
  void reverse() {
    swap(l, r);
    rev ^= 1;
  }
};
template <typename S, int NODES>
using SplayTree_Basic = SplayTree<Node_Basic<S>, NODES>;
} // namespace SplayTreeNodes

using SplayTreeNodes::SplayTree_Basic;

void solve() {
    INT(n, k);
    STR(s);
    VEC(int, L, k);
    VEC(int, R, k);
    INT(q);
    VEC(int, Q, q);
    static SplayTree_Basic<int, 1'000'000> X;
    auto root = X.new_node(vi(all(s)));
    each(x, Q) {
        int i = LB(R, x);
        int a = min(x, R[i] + L[i] - x), b = max(x, R[i] + L[i] - x);
        a--, b--;
        auto [l, m, r] = X.split3(root, a, b + 1);
        X.reverse(m);
        root = X.merge3(l, m, r);
    }
    string ans;
    each(i, X.get_all(root)) ans += i;
    print(ans);
    
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
