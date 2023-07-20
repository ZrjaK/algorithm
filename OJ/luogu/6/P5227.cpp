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

/*
・時刻 t に x を追加する
・時刻 t に x を削除する
があるときに、
・時刻 [l, r) に x を追加する
に変換する。
クエリが時系列順に来ることが分かっているときは monotone = true の方が高速。
*/
template <typename X, bool monotone>
struct Add_Remove_Query {
  map<X, int> MP;
  vector<tuple<int, int, X>> dat;
  map<X, vector<int>> ADD;
  map<X, vector<int>> RM;

  void add(int time, X x) {
    if (monotone) return add_monotone(time, x);
    ADD[x].emplace_back(time);
  }
  void remove(int time, X x) {
    if (monotone) return remove_monotone(time, x);
    RM[x].emplace_back(time);
  }

  // すべてのクエリが終わった現在時刻を渡す
  vector<tuple<int, int, X>> calc(int time) {
    if (monotone) return calc_monotone(time);
    vector<tuple<int, int, X>> dat;
    for (auto&& [x, A]: ADD) {
      vector<int> B;
      if (RM.count(x)) {
        B = RM[x];
        RM.erase(x);
      }
      while (B.size() < A.size()) B.eb(time);
      assert(A.size() == B.size());

      sort(A.begin(), A.end());
      sort(B.begin(), B.end());
      for (int i = 0; i < A.size(); i++) {
        assert(A[i] <= B[i]);
        if (A[i] < B[i]) dat.emplace_back(A[i], B[i], x);
      }
    }
    assert(RM.size() == 0);
    return dat;
  }

private:
  void add_monotone(int time, X x) {
    assert(!MP.count(x));
    MP[x] = time;
  }
  void remove_monotone(int time, X x) {
    auto it = MP.find(x);
    assert(it != MP.end());
    int t = (*it).second;
    MP.erase(it);
    if (t == time) return;
    dat.emplace_back(t, time, x);
  }
  vector<tuple<int, int, X>> calc_monotone(int time) {
    for (auto&& [x, t]: MP) {
      if (t == time) continue;
      dat.emplace_back(t, time, x);
    }
    return dat;
  }
};

template <typename T>
struct Rollback_Array {
  int N;
  vector<T> dat;
  vector<pair<int, T>> history;
 
  Rollback_Array(vector<T> x) : N(x.size()), dat(x) {}
  Rollback_Array(int N) : N(N), dat(N) {}
  template <typename F>
  Rollback_Array(int N, F f) : N(N) {
    dat.reserve(N);
    for (int i = 0; i < N; i++) dat.emplace_back(f(i));
  }
 
  int time() { return history.size(); }
  void rollback(int t) {
    for(int i = time() - 1; i >= t; i--) {
      auto& [idx, v] = history[i];
      dat[idx] = v;
    }
    history.resize(t);
  }
  T get(int idx) { return dat[idx]; }
  void set(int idx, T x) {
    history.emplace_back(idx, dat[idx]);
    dat[idx] = x;
  }
 
  vector<T> get_all() {
    vector<T> res(N);
    for (int i = 0; i < N; i++) res[i] = get(i);
    return res;
  }
};
 
struct Rollback_UnionFind {
  Rollback_Array<int> dat; // parent or size
 
  Rollback_UnionFind(int n) : dat(vector<int>(n, -1)) {}
 
  int operator[](int v) {
    while (dat.get(v) >= 0) v = dat.get(v);
    return v;
  }
 
  int size(int v) { return -dat.get((*this)[v]); }
  int time() { return dat.time(); }
  void rollback(int t) { dat.rollback(t); }
 
  bool merge(int a, int b) {
    a = (*this)[a], b = (*this)[b];
    if (a == b) return false;
    if (dat.get(a) > dat.get(b)) swap(a, b);
    dat.set(a, dat.get(a) + dat.get(b));
    dat.set(b, a);
    return true;
  }
};

void solve() {
    INT(n, m);
    Add_Remove_Query<pii, false> X;
    vpii E;
    rep(_, m) {
        INT(x, y);
        x--, y--;
        E.eb(x, y);
        X.add(0, pii{x, y});
    }
    INT(k);
    int time = 1;
    rep(i, 1, k + 1) {
        INT(c);
        VEC(int, a, c);
        each(_, a) {
            _--;
            auto [x, y] = E[_];
            X.remove(i, pii{x, y});
            X.add(i + 1, pii{x, y});
        }
    }
    auto upd = X.calc(k + 1);
    Rollback_UnionFind uf(n);
    vi I(len(upd));
    iota(all(I), 0);
    vi ANS(k + 1);

    auto dfs = [&](auto& dfs, vector<int>& upd_query_I, int begin, int end) -> void {
        if (begin == end) return;
        // snapshot
        int uf_time = uf.time();

        vi IL, IR;
        int mid = (begin + end) / 2;
        for (auto&& i: upd_query_I) {
            auto [a, b, XX] = upd[i];
            auto [x, y] = XX;
            if (a <= begin && end <= b) {
                // X で表される update query を処理する
                uf.merge(x, y);
            } else {
                if (a < mid) IL.eb(i);
                if (mid < b) IR.eb(i);
            }
        }
        if (begin + 1 == end) {
            // 求値クエリ
            int qid = begin;
            ANS[qid] = uf.size(0) == n;
            // ここで出力してしまってもよい
        } else {
            dfs(dfs, IL, begin, mid);
            dfs(dfs, IR, mid, end);
        }
        // rollback
        uf.rollback(uf_time);
    };
    dfs(dfs, I, 0, k + 1);
    rep(i, 1, k + 1) print(ANS[i] ? "Connected" : "Disconnected");
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
