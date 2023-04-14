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

// S: return type, op: how to merge at return, e: S default constructor
// F: value type of lazy value
// mapping: called on apply() to each item, mapping(F f, S item)
// composition: called on apply() to lazy value of a seg, composition(F f, F lazy)
// id: default falue of lazy value
template <class S,
          S (*op)(S, S),
          S (*e)(),
          class F,
          S (*mapping)(F, S),
          F (*composition)(F, F),
          F (*id)()>
struct lazy_segtree {
  public:
    lazy_segtree() : lazy_segtree(0) {}
    explicit lazy_segtree(int n) : lazy_segtree(std::vector<S>(n, e())) {}
    explicit lazy_segtree(const std::vector<S>& v) : _n(int(v.size())) {
        log = 0;
        while ((1 << log) < _n) ++log;
        size = 1 << log;
        d = std::vector<S>(2 * size, e());
        lz = std::vector<F>(size, id());
        for (int i = 0; i < _n; i++) d[size + i] = v[i];
        for (int i = size - 1; i >= 1; i--) {
            update(i);
        }
    }

    void set(int p, S x) {
        assert(0 <= p && p < _n);
        p += size;
        for (int i = log; i >= 1; i--) push(p >> i);
        d[p] = x;
        for (int i = 1; i <= log; i++) update(p >> i);
    }

    S get(int p) {
        assert(0 <= p && p < _n);
        p += size;
        for (int i = log; i >= 1; i--) push(p >> i);
        return d[p];
    }

    S prod(int l, int r) {
        assert(0 <= l && l <= r && r <= _n);
        if (l == r) return e();

        l += size;
        r += size;

        for (int i = log; i >= 1; i--) {
            if (((l >> i) << i) != l) push(l >> i);
            if (((r >> i) << i) != r) push((r - 1) >> i);
        }

        S sml = e(), smr = e();
        while (l < r) {
            if (l & 1) sml = op(sml, d[l++]);
            if (r & 1) smr = op(d[--r], smr);
            l >>= 1;
            r >>= 1;
        }

        return op(sml, smr);
    }

    S all_prod() { return d[1]; }

    void apply_single(int p, F f) {
        assert(0 <= p && p < _n);
        p += size;
        for (int i = log; i >= 1; i--) push(p >> i);
        d[p] = mapping(f, d[p]);
        for (int i = 1; i <= log; i++) update(p >> i);
    }
    void apply(int l, int r, F f) {
        assert(0 <= l && l <= r && r <= _n);
        if (l == r) return;

        l += size;
        r += size;

        for (int i = log; i >= 1; i--) {
            if (((l >> i) << i) != l) push(l >> i);
            if (((r >> i) << i) != r) push((r - 1) >> i);
        }

        {
            int l2 = l, r2 = r;
            while (l < r) {
                if (l & 1) all_apply(l++, f);
                if (r & 1) all_apply(--r, f);
                l >>= 1;
                r >>= 1;
            }
            l = l2;
            r = r2;
        }

        for (int i = 1; i <= log; i++) {
            if (((l >> i) << i) != l) update(l >> i);
            if (((r >> i) << i) != r) update((r - 1) >> i);
        }
    }

    template <bool (*g)(S)> int max_right(int l) {
        return max_right(l, [](S x) { return g(x); });
    }
    template <class G> int max_right(int l, G g) {
        assert(0 <= l && l <= _n);
        assert(g(e()));
        if (l == _n) return _n;
        l += size;
        for (int i = log; i >= 1; i--) push(l >> i);
        S sm = e();
        do {
            while (l % 2 == 0) l >>= 1;
            if (!g(op(sm, d[l]))) {
                while (l < size) {
                    push(l);
                    l = (2 * l);
                    if (g(op(sm, d[l]))) {
                        sm = op(sm, d[l]);
                        l++;
                    }
                }
                return l - size;
            }
            sm = op(sm, d[l]);
            l++;
        } while ((l & -l) != l);
        return _n;
    }

    template <bool (*g)(S)> int min_left(int r) {
        return min_left(r, [](S x) { return g(x); });
    }
    template <class G> int min_left(int r, G g) {
        assert(0 <= r && r <= _n);
        assert(g(e()));
        if (r == 0) return 0;
        r += size;
        for (int i = log; i >= 1; i--) push((r - 1) >> i);
        S sm = e();
        do {
            r--;
            while (r > 1 && (r % 2)) r >>= 1;
            if (!g(op(d[r], sm))) {
                while (r < size) {
                    push(r);
                    r = (2 * r + 1);
                    if (g(op(d[r], sm))) {
                        sm = op(d[r], sm);
                        r--;
                    }
                }
                return r + 1 - size;
            }
            sm = op(d[r], sm);
        } while ((r & -r) != r);
        return 0;
    }

  private:
    int _n, size, log;
    std::vector<S> d;
    std::vector<F> lz;

    void update(int k) { d[k] = op(d[2 * k], d[2 * k + 1]); }
    void all_apply(int k, F f) {
        d[k] = mapping(f, d[k]);
        if (k < size) lz[k] = composition(f, lz[k]);
    }
    void push(int k) {
        all_apply(2 * k, lz[k]);
        all_apply(2 * k + 1, lz[k]);
        lz[k] = id();
    }
};

ll op(ll a, ll b) {
    return max(a, b);
}

ll e() {
    return 0;
}

void solve() {
    INT(n);
    auto a = ndvector(n, array<int, 5>{});
    rep(i, n) cin >> a[i][0] >> a[i][1] >> a[i][2] >> a[i][3], a[i][4] = i;
    vi nums;
    each(i, a) nums.pb(i[2]);
    UNIQUE(nums);
    int m = len(nums);
    rep(i, n) a[i][2] = LB(nums, a[i][2]);
    sort(all(a));
    lazy_segtree<ll, op, e, ll, op, op, e> seg(m);
    vll dp(n);
    rep(i, n) dp[a[i][4]] = a[i][3];
    auto cdq = [&] (auto cdq, int l, int r) -> void {
        if (l == r) return;
        int mid = l + r >> 1;
        cdq(cdq, l, mid);

        auto h = ndvector(0, array<int, 6>{});
        rep(i, l, mid + 1) h.pb({a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], 1});
        rep(i, mid + 1, r + 1) h.pb({a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], 2});
        sort(all(h), [&] (auto const& i, auto const& j) {
            return pii{i[1], -i[5]} < pii{j[1], -j[5]};
        });
        for (auto [x, y, z, w, id, op] : h) {
            if (op == 1) {
                if (x != a[mid+1][0]) seg.apply_single(z, dp[id]);
            } else {
                if (x == a[mid+1][0]) chmax(dp[id], seg.prod(0, z) + w);
            }
        }
        for (auto [x, y, z, w, id, op] : h) seg.set(z, 0);

        for (auto [x, y, z, w, id, op] : h) {
            if (op == 1) {
                seg.apply_single(z, dp[id]);
            } else {
                if (x != a[mid+1][0]) chmax(dp[id], seg.prod(0, z) + w);
            }
        }
        for (auto [x, y, z, w, id, op] : h) seg.set(z, 0);
        
        cdq(cdq, mid + 1, r);
    };
    cdq(cdq, 0, n - 1);
    print(max(dp));
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
