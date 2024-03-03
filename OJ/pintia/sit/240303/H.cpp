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
template<class T> auto max(const T& a){ return *max_element(all(a)); }
template<class T> auto min(const T& a){ return *min_element(all(a)); }
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
#define INT(...) \
  int __VA_ARGS__; \
  IN(__VA_ARGS__)
#define LL(...) \
  ll __VA_ARGS__; \
  IN(__VA_ARGS__)
#define STR(...) \
  string __VA_ARGS__; \
  IN(__VA_ARGS__)
#define CHR(...) \
  char __VA_ARGS__; \
  IN(__VA_ARGS__)
#define DBL(...) \
  long double __VA_ARGS__; \
  IN(__VA_ARGS__)

#define VEC(type, name, size) \
  vector<type> name(size);    \
  read(name)
#define VV(type, name, h, w)                     \
  vector<vector<type>> name(h, vector<type>(w)); \
  read(name)

void read(int &a) { cin >> a; }
void read(long long &a) { cin >> a; }
void read(char &a) { cin >> a; }
void read(double &a) { cin >> a; }
void read(long double &a) { cin >> a; }
void read(string &a) { cin >> a; }
template <class T, class S> void read(pair<T, S> &p) { read(p.first), read(p.second); }
template <class T> void read(vector<T> &a) {for(auto &i : a) read(i);}
template <class T> void read(T &a) { cin >> a; }
void IN() {}
template <class Head, class... Tail> void IN(Head &head, Tail &...tail) {
  read(head);
  IN(tail...);
}

template <typename T, typename U>
ostream& operator<<(ostream& os, const pair<T, U>& A) {
  os << A.fi << " " << A.se;
  return os;
}

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& A) {
  for (size_t i = 0; i < A.size(); i++) {
    if(i) os << " ";
    os << A[i];
  }
  return os;
}

void print() {
  cout << "\n";
  cout.flush();
}

template <class Head, class... Tail>
void print(Head&& head, Tail&&... tail) {
  cout << head;
  if (sizeof...(Tail)) cout << " ";
  print(forward<Tail>(tail)...);
}

void YES(bool t = 1) { print(t ? "YES" : "NO"); }
void NO(bool t = 1) { YES(!t); }
void Yes(bool t = 1) { print(t ? "Yes" : "No"); }
void No(bool t = 1) { Yes(!t); }
void yes(bool t = 1) { print(t ? "yes" : "no"); }
void no(bool t = 1) { yes(!t); }
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

#line 2 "ds/segtree/dynamic_lazy_segtree.hpp"

template <typename ActedMonoid, bool PERSISTENT, int NODES>
struct Dynamic_Lazy_SegTree {
  using AM = ActedMonoid;
  using MX = typename AM::Monoid_X;
  using MA = typename AM::Monoid_A;
  using X = typename AM::X;
  using A = typename AM::A;
  using F = function<X(ll, ll)>;
  F default_prod;

  struct Node {
    Node *l, *r;
    X x;
    A lazy;
  };

  const ll L0, R0;
  Node *pool;
  int pid;
  using np = Node *;

  Dynamic_Lazy_SegTree(
      ll L0, ll R0, F default_prod = [](ll l, ll r) -> X { return MX::unit(); })
      : default_prod(default_prod), L0(L0), R0(R0), pid(0) {
    pool = new Node[NODES];
  }

  np new_root() { return new_node(L0, R0); }

  np new_node(const X x) {
    pool[pid].l = pool[pid].r = nullptr;
    pool[pid].x = x;
    pool[pid].lazy = MA::unit();
    return &(pool[pid++]);
  }

  np new_node(ll l, ll r) { return new_node(default_prod(l, r)); }
  np new_node() { return new_node(L0, R0); }

  np new_node(const vc<X> &dat) {
    assert(L0 == 0 && R0 == len(dat));
    auto dfs = [&](auto &dfs, ll l, ll r) -> Node * {
      if (l == r) return nullptr;
      if (r == l + 1) return new_node(dat[l]);
      ll m = (l + r) / 2;
      np l_root = dfs(dfs, l, m), r_root = dfs(dfs, m, r);
      X x = MX::op(l_root->x, r_root->x);
      np root = new_node(x);
      root->l = l_root, root->r = r_root;
      return root;
    };
    return dfs(dfs, 0, len(dat));
  }

  X prod(np root, ll l, ll r) {
    if (l == r || !root) return MX::unit();
    assert(pid && L0 <= l && l < r && r <= R0);
    X x = MX::unit();
    prod_rec(root, L0, R0, l, r, x, MA::unit());
    return x;
  }

  X prod_all(np root) { return prod(root, L0, R0); }

  np set(np root, ll i, const X &x) {
    assert(pid && L0 <= i && i < R0);
    return set_rec(root, L0, R0, i, x);
  }

  np multiply(np root, ll i, const X &x) {
    assert(pid && L0 <= i && i < R0);
    return multiply_rec(root, L0, R0, i, x);
  }

  np apply(np root, ll l, ll r, const A &a) {
    if (l == r) return root;
    assert(pid && L0 <= l && l < r && r <= R0);
    return apply_rec(root, L0, R0, l, r, a);
  }

  void reset() { pid = 0; }

private:
  np copy_node(np c) {
    if (!c || !PERSISTENT) return c;
    pool[pid].l = c->l, pool[pid].r = c->r;
    pool[pid].x = c->x;
    pool[pid].lazy = c->lazy;
    return &(pool[pid++]);
  }

  void prop(np c, ll l, ll r) {
    assert(r - l >= 2);
    ll m = (l + r) / 2;
    if (c->lazy == MA::unit()) return;
    c->l = (c->l ? copy_node(c->l) : new_node(l, m));
    c->l->x = AM::act(c->l->x, c->lazy, m - l);
    c->l->lazy = MA::op(c->l->lazy, c->lazy);
    c->r = (c->r ? copy_node(c->r) : new_node(m, r));
    c->r->x = AM::act(c->r->x, c->lazy, r - m);
    c->r->lazy = MA::op(c->r->lazy, c->lazy);
    c->lazy = MA::unit();
  }

  np set_rec(np c, ll l, ll r, ll i, const X &x) {
    if (r == l + 1) {
      c = copy_node(c);
      c->x = x;
      c->lazy = MA::unit();
      return c;
    }
    prop(c, l, r);
    ll m = (l + r) / 2;
    if (!c->l) c->l = new_node(l, m);
    if (!c->r) c->r = new_node(m, r);

    c = copy_node(c);
    if (i < m) {
      c->l = set_rec(c->l, l, m, i, x);
    } else {
      c->r = set_rec(c->r, m, r, i, x);
    }
    c->x = MX::op(c->l->x, c->r->x);
    return c;
  }

  np multiply_rec(np c, ll l, ll r, ll i, const X &x) {
    if (r == l + 1) {
      c = copy_node(c);
      c->x = MX::op(c->x, x);
      c->lazy = MA::unit();
      return c;
    }
    prop(c, l, r);
    ll m = (l + r) / 2;
    if (!c->l) c->l = new_node(l, m);
    if (!c->r) c->r = new_node(m, r);

    c = copy_node(c);
    if (i < m) {
      c->l = multiply_rec(c->l, l, m, i, x);
    } else {
      c->r = multiply_rec(c->r, m, r, i, x);
    }
    c->x = MX::op(c->l->x, c->r->x);
    return c;
  }

  void prod_rec(np c, ll l, ll r, ll ql, ll qr, X &x, A lazy) {
    chmax(ql, l);
    chmin(qr, r);
    if (ql >= qr) return;
    if (!c) {
      x = MX::op(x, AM::act(default_prod(ql, qr), lazy, qr - ql));
      return;
    }
    if (l == ql && r == qr) {
      x = MX::op(x, AM::act(c->x, lazy, r - l));
      return;
    }
    ll m = (l + r) / 2;
    lazy = MA::op(c->lazy, lazy);
    prod_rec(c->l, l, m, ql, qr, x, lazy);
    prod_rec(c->r, m, r, ql, qr, x, lazy);
  }

  np apply_rec(np c, ll l, ll r, ll ql, ll qr, const A &a) {
    if (!c) c = new_node(l, r);
    chmax(ql, l);
    chmin(qr, r);
    if (ql >= qr) return c;
    if (l == ql && r == qr) {
      c = copy_node(c);
      c->x = AM::act(c->x, a, r - l);
      c->lazy = MA::op(c->lazy, a);
      return c;
    }
    prop(c, l, r);
    ll m = (l + r) / 2;
    c = copy_node(c);
    c->l = apply_rec(c->l, l, m, ql, qr, a);
    c->r = apply_rec(c->r, m, r, ql, qr, a);
    c->x = MX::op(c->l->x, c->r->x);
    return c;
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
#line 2 "alg/acted_monoid/sum_add.hpp"

template <typename E>
struct ActedMonoid_Sum_Add {
  using Monoid_X = Monoid_Add<E>;
  using Monoid_A = Monoid_Add<E>;
  using X = typename Monoid_X::value_type;
  using A = typename Monoid_A::value_type;
  static constexpr X act(const X &x, const A &a, const ll &size) {
    return x + a * E(size);
  }
};

void solve() {
    LL(n, q);
    ll LIM = 1e12 + 10;
    Dynamic_Lazy_SegTree<ActedMonoid_Sum_Add<ll>, false, 10'000'000> seg(0, LIM);
    auto root = seg.new_root();
    rep(q) {
        INT(op);
        if (op == 1) {
            LL(t, a);
            root = seg.apply(root, t, t + 1, a);
        }
        if (op == 2) {
            LL(t, a);
            root = seg.apply(root, t + 1, t + 2, a);
            root = seg.apply(root, t + 2, LIM, 1);
        }
        if (op == 3) {
            LL(t);
            print(seg.prod(root, 0, t + 1));
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