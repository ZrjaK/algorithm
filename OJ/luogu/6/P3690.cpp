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
template <class T> using Tree = tree<T, null_type, less_equal<T>, rb_tree_tag,tree_order_statistics_node_update>;
using Trie = trie<string, null_type, trie_string_access_traits<>, pat_trie_tag, trie_prefix_search_node_update>;
// template <class T> using heapq = __gnu_pbds::priority_queue<T, greater<T>, pairing_heap_tag>;
template <class T> using heapq = std::priority_queue<T, vector<T>, greater<T>>;
#define ll                  long long
#define i128                __int128
#define ld                  long double
#define ui                  unsigned int
#define ull                 unsigned long long
#define pii                 pair<int, int>
#define pll                 pair<ll, ll>
#define pdd                 pair<ld, ld>
#define vi                  vector<int>
#define vvi                 vector<vector<int>>
#define vll                 vector<ll>
#define vvll                vector<vector<ll>>
#define vpii                vector<pii>
#define vpll                vector<pll>
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
#define FOR_subset(t, s)    for (int t = (s); t >= 0; t = (t == 0 ? -1 : (t - 1) & (s)))
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
#define lowbit(x)           (x & (-x))
#define bitcnt(x)           (__builtin_popcountll(x))
#define endl                "\n"
#define LB(c, x)            distance((c).begin(), lower_bound(all(c), (x)))
#define UB(c, x)            distance((c).begin(), upper_bound(all(c), (x)))
#define UNIQUE(x)           sort(all(x)), x.erase(unique(all(x)), x.end()), x.shrink_to_fit()
#define SUM(...)            accumulate(all(__VA_ARGS__), 0LL)
#define SORT(a)             sort(all(a))
#define REV(a)              reverse(all(a))
template<class T> auto max(const T& a){ return *max_element(all(a)); }
template<class T> auto min(const T& a){ return *min_element(all(a)); }
template <class T> vector<long long> cumsum(vector<T> &A, int off = 1) {
    int N = A.size();
    vector<long long> B(N + 1);
    for (int i = 0; i < N; i++) B[i + 1] = B[i] + A[i];
    if (off == 0) B.erase(B.begin());
    return B;
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
template <class T> ostream &operator<<(ostream &os, const Tree<T> &v) {
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

template <typename Node, int NODES>
struct LinkCutTree_base {
  int n;
  Node *nodes;

  LinkCutTree_base(int n = 0) : n(n) {
    nodes = new Node[NODES];
    for(int i = 0; i < n; i++) nodes[i] = Node(i);
  }

  Node *operator[](int v) { return &nodes[v]; }

  // パスを表す splay tree の根になっているかどうか
  bool is_root(Node *c) { return state(c) == 0; }
  bool is_root(int c) { return state(&nodes[c]) == 0; }

  Node *get_root(Node *c) {
    expose(c);
    while (c->l) {
      c->push();
      c = c->l;
    }
    splay(c);
    return c;
  }

  int get_root(int c) { return get_root(&nodes[c])->idx; }

  // c の親を p にする。内部で evert するのでいつ呼んでも大丈夫。
  virtual void link(Node *c, Node *p) {
    evert(c);
    expose(p);
    c->p = p;
    p->r = c;
    p->update();
  }

  // c の親を p にする。内部で evert するのでいつ呼んでも大丈夫。
  virtual void link(int c, int p) { return link(&nodes[c], &nodes[p]); }

  void cut(Node *a, Node *b) {
    evert(a);
    expose(b);
    assert(!b->p);
    assert((b->l) == a);
    b->l->p = nullptr;
    b->l = nullptr;
    b->update();
  }

  void cut(int a, int b) { return cut(&nodes[a], &nodes[b]); }

  void evert(Node *c) {
    expose(c);
    c->reverse();
    c->push();
  }

  void evert(int c) { evert(&nodes[c]); }

  Node *lca(Node *u, Node *v) {
    assert(get_root(u) == get_root(v));
    expose(u);
    return expose(v);
  }

  int lca(int u, int v) { return lca(&nodes[u], &nodes[v])->idx; }

  // c と根までが繋がれている状態に変更して、根を return する
  virtual Node *expose(Node *c) {
    Node *now = c;
    Node *rp = nullptr; // 今まで作ったパス
    while (now) {
      splay(now);
      now->r = rp; // 子方向の変更
      now->update();
      rp = now;
      now = now->p;
    }
    splay(c);
    return rp;
  }

  int expose(int c) {
    Node *x = expose(&nodes[c]);
    if (!x) return -1;
    return x->idx;
  }

  Node *get_parent(Node *x) {
    expose(x);
    if (!x->l) return nullptr;
    x = x->l;
    while (x->r) x = x->r;
    return x;
  }

  int get_parent(int x) {
    Node *p = get_parent((*this)[x]);
    return (p ? p->idx : -1);
  }

  void debug() {
    for(int i = 0; i < n; i++) { nodes[i].debug(); }
  }

  virtual void rotate(Node *n) {
    // n を根に近づける
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

  inline int state(Node *n) {
    if (!n->p) return 0;
    if (n->p->l == n) return 1;
    if (n->p->r == n) return -1;
    return 0;
  }

  void splay(Node *c) {
    c->push();
    while (!is_root(c)) {
      Node *p = c->p;
      Node *pp = (p ? p->p : nullptr);
      if (state(p) == 0) {
        p->push(), c->push();
        rotate(c);
        if (p) p->update();
      }
      else if (state(c) == state(p)) {
        pp->push(), p->push(), c->push();
        rotate(p);
        rotate(c);
        if (pp) pp->update();
        if (p) p->update();
      }
      else {
        pp->push(), p->push(), c->push();
        rotate(c);
        rotate(c);
        if (p) p->update();
        if (pp) pp->update();
      }
    }
    c->update();
  }
};

struct LCT_Node_base {
  LCT_Node_base *l, *r, *p;
  int idx;
  bool rev;
  LCT_Node_base(int i = 0) : l(nullptr), r(nullptr), p(nullptr), idx(i) {}

  void update() {}

  void push() {
    if (rev) {
      if (l) l->reverse();
      if (r) r->reverse();
      rev = 0;
    }
  }

  void reverse() {
    rev ^= 1;
    swap(l, r);
  }
};

template <int NODES>
using LinkCutTree = LinkCutTree_base<LCT_Node_base, NODES>;
#line 2 "graph/ds/link_cut_path.hpp"

template <typename Node, int NODES>
struct LinkCutTree_Path_base : public LinkCutTree_base<Node, NODES> {
  using X = typename Node::X;

  LinkCutTree_Path_base(int n) : LinkCutTree_base<Node, NODES>(n) {}

  LinkCutTree_Path_base(vector<X> dat) : LinkCutTree_base<Node, NODES>(dat.size()) {
    for(int v = 0; v < dat.size(); v++) {
      Node *c = (*this)[v];
      set(c, dat[v]);
    }
  }

  template <typename F>
  LinkCutTree_Path_base(int n, F f) : LinkCutTree_base<Node, NODES>(n) {
    for(int v = 0; v < n; v++) {
      X x = f(v);
      Node *c = (*this)[v];
      set(c, x);
    }
  }

  void set(Node *c, X x) {
    this->evert(c);
    c->x = x;
    c->update();
  }

  void set(int c, X x) { set((*this)[c], x); }

  void multiply(Node *c, X x) { set(c, Node::Mono::op(c->x, x)); }

  void multiply(int c, X x) { multiply((*this)[c], x); }

  X prod_path(Node *a, Node *b) {
    this->evert(a);
    this->expose(b);
    return b->prod;
  }

  X prod_path(int a, int b) { return prod_path((*this)[a], (*this)[b]); }
};

template <typename Monoid>
struct LCT_Node_Monoid {
  using Mono = Monoid;
  using X = typename Monoid::value_type;
  LCT_Node_Monoid *l, *r, *p;
  int idx;
  X x, prod, rev_prod;
  bool rev;
  LCT_Node_Monoid(int i = 0)
      : l(nullptr),
        r(nullptr),
        p(nullptr),
        idx(i),
        x(Monoid::unit()),
        prod(Monoid::unit()),
        rev_prod(Monoid::unit()) {}

  void update() {
    prod = rev_prod = x;
    if (l) {
      prod = Monoid::op(l->prod, prod);
      rev_prod = Monoid::op(rev_prod, l->rev_prod);
    }
    if (r) {
      prod = Monoid::op(prod, r->prod);
      rev_prod = Monoid::op(r->rev_prod, rev_prod);
    }
  }

  void push() {
    if (rev) {
      if (l) l->reverse();
      if (r) r->reverse();
      rev = 0;
    }
  }

  void reverse() {
    rev ^= 1;
    swap(l, r);
    swap(prod, rev_prod);
  }

  void debug() {
    int li = (l ? l->idx : -1);
    int ri = (r ? r->idx : -1);
    int pi = (p ? p->idx : -1);
    print("idx", idx, "l", li, "r", ri, "p", pi, "x", x, "prod", prod,
          "rev_prod", rev_prod);
  }
};

template <typename Monoid>
struct LCT_Node_CommutativeMonoid {
  using Mono = Monoid;
  using X = typename Mono::value_type;
  LCT_Node_CommutativeMonoid *l, *r, *p;
  int idx;
  X x, prod;
  bool rev;
  LCT_Node_CommutativeMonoid(int i = 0)
      : l(nullptr),
        r(nullptr),
        p(nullptr),
        idx(i),
        x(Mono::unit()),
        prod(Mono::unit()) {}

  void update() {
    prod = x;
    if (l) { prod = Mono::op(l->prod, prod); }
    if (r) { prod = Mono::op(prod, r->prod); }
  }

  void push() {
    if (rev) {
      if (l) l->reverse();
      if (r) r->reverse();
      rev = 0;
    }
  }

  void reverse() {
    rev ^= 1;
    swap(l, r);
  }

  void debug() {
    int li = (l ? l->idx : -1);
    int ri = (r ? r->idx : -1);
    int pi = (p ? p->idx : -1);
    print("idx", idx, "l", li, "r", ri, "p", pi, "x", x, "prod", prod);
  }
};

template <typename Monoid, int NODES>
using LinkCutTree_Path = LinkCutTree_Path_base<LCT_Node_Monoid<Monoid>, NODES>;

template <typename Monoid, int NODES>
using LinkCutTree_Path_Commutative
    = LinkCutTree_Path_base<LCT_Node_CommutativeMonoid<Monoid>, NODES>;

template <typename X>
struct Monoid_Xor {
  using value_type = X;
  static X op(X x, X y) { return x ^ y; }
  static constexpr X inverse(const X &x) noexcept { return x; }
  static constexpr X power(const X &x, ll n) noexcept {
    return (n & 1 ? x : 0);
  }
  static constexpr X unit(){return X(0);};
  static constexpr bool commute = true;
};

void solve() {
    INT(n, m);
    VEC(int, a, n);
    LinkCutTree_Path<Monoid_Xor<int>, 500000> X(a);
    rep(_, m) {
        INT(op, x, y);
        if (op == 0) {
            x--, y--;
            print(X.prod_path(x, y));
        }
        if (op == 1) {
            x--, y--;
            if (X.get_root(x) == X.get_root(y)) continue;
            X.link(x, y);
        }
        if (op == 2) {
            x--, y--;
            X.evert(X[x]);
            X.expose(X[y]);
            if (X[x]->l == X[y] || X[x]->r == X[y] || X[y]->l == X[x] || X[y]->r == X[x])
                X.cut(x, y);
        }
        if (op == 3) {
            x--;
            X.multiply(x, a[x] ^ y);
            a[x] = y;
        }
    }

    
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
