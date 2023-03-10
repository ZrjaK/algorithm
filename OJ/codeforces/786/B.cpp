#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
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
#define ll long long
#define i128 __int128
#define ld long double
#define ui unsigned int
#define ull unsigned long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define vi vector<int>
#define vvi vector<vector<int>>
#define vll vector<ll>
#define vvll vector<vector<ll>>
#define vpii vector<pii>
#define vpll vector<pll>
#define lb lower_bound
#define ub upper_bound
#define pb push_back
#define pf push_front
#define eb emplace_back
#define fi first
#define se second
#define rep(i, a, b) for(int i = a; i < b; ++i)
#define per(i, a, b) for(int i = a; i > b; --i)
#define each(x, v) for(auto& x: v)
#define len(x) (int)x.size()
#define elif else if
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define mst(x, a) memset(x, a, sizeof(x))
#define lowbit(x) (x & (-x))
#define bitcnt(x) (__builtin_popcountll(x))
#define endl "\n"
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
template <class T, class S> ostream &operator<<(ostream &os, const pair<T, S> &p) {
    os << p.first << " " << p.second;
    return os;
}
ll gcd(ll x,ll y) {
    if(!x) return y;
    if(!y) return x;
    int t = __builtin_ctzll(x | y);
    x >>= __builtin_ctzll(x);
    do {
        y >>= __builtin_ctzll(y);
        if(x > y) swap(x, y);
        y -= x;
    } while(y);
    return x<<t;
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
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 1e6 + 10;

struct SegTree_for_graph {
    vector<vector<pair<int, int>>> G;
    int rt1,rt2,tot;
    int maxn;
    vector<int> ls, rs;
    vector<int> in, out;

    SegTree_for_graph(int n) {
        rt1 = rt2 = tot = 0;
        maxn = n;
        ls = vector<int>(maxn * 30);
        rs = vector<int>(maxn * 30);
        in = vector<int>(maxn * 30);
        out = vector<int>(maxn * 30);
        G = vector<vector<pair<int, int>>>(maxn * 30);
        build_in(rt1, 1, maxn);
        build_out(rt2, 1, maxn);
        for (int i = 1; i <= n; i++) {
            _add(in[i], out[i], 0);
            _add(out[i], in[i], 0);
        }
    }

    void add(int u,int v,int val){
        _add(in[u], out[v], val);
    }

    void _add(int u,int v,int val){
        G[u].emplace_back(pair<int, int>{v, val});
    }

    #define ls ls[rt]
    #define rs rs[rt]   

    void build_in(int &rt,int l,int r){
        rt=++tot;
        if(l==r){
            in[l]=rt;
            return;
        }

        int mid=(l+r)>>1;
        build_in(ls,l,mid);
        build_in(rs,mid+1,r);
 
        _add(ls,rt,0);_add(rs,rt,0);
    }

    void build_out(int &rt,int l,int r){
        rt=++tot;
        if(l==r){
            out[l]=rt;
            return;
        }

        int mid=(l+r)>>1;
        build_out(ls,l,mid);
        build_out(rs,mid+1,r);
 
        _add(rt,ls,0);_add(rt,rs,0);
    }

    // 区间到点
    // st.modify_in(l, r, v, w);
    void modify_in(int ql, int qr, int pos, int val) {
        _modify_in(rt1, 1, maxn, ql, qr, out[pos], val);
    }

    void _modify_in(int rt,int l,int r,int ql,int qr,int pos,int val){
        if(ql>r||qr<l)return;
        if(ql<=l&&qr>=r){
            _add(rt,pos,val);
            return;
        }
        int mid=(l+r)>>1;
        _modify_in(ls,l,mid,ql,qr,pos,val);
        _modify_in(rs,mid+1,r,ql,qr,pos,val);
    }


    // 点到区间
    // st.modify_out(l, r, u, w);
    void modify_out(int ql, int qr, int pos, int val) {
        _modify_out(rt2, 1, maxn, ql, qr, in[pos], val);
    }
    void _modify_out(int rt,int l,int r,int ql,int qr,int pos,int val){
        if(ql>r||qr<l)return;
        if(ql<=l&&qr>=r){
            _add(pos,rt,val);
            return;
        }
        int mid=(l+r)>>1;
        _modify_out(ls,l,mid,ql,qr,pos,val);
        _modify_out(rs,mid+1,r,ql,qr,pos,val);
    }
};

void solve() {
    int n, m, s;
    cin >> n >> m >> s;
    SegTree_for_graph st(n);
    rep(_, 0, m) {
        int op;
        cin >> op;
        if (op == 1) {
            int u, v, w;
            cin >> u >> v >> w;
            st.add(u, v, w);
        }
        if (op == 2) {
            int u, l, r, w;
            cin >> u >> l >> r >> w;
            st.modify_out(l, r, u, w);
        }
        if(op==3){
            int v, l, r, w;
            cin >> v >> l >> r >> w;
            st.modify_in(l, r, v, w);
        }
    }
    s = st.in[s];
    auto& d = st.G;
    heapq<pair<ll, int>> pq;
    vll dist(n * 30, LINF);
    dist[s] = 0;
    pq.push({0, s});
    while (!pq.empty()) {
        auto [_, i] = pq.top();
        pq.pop();
        if (_ != dist[i]) continue;
        for (auto& [j, w] : d[i]) {
            if (dist[j] > dist[i] + w) {
                dist[j] = dist[i] + w;
                pq.push({dist[j], j});
            }
        }
    }
    rep(i, 1, n + 1) {
        cout << (dist[st.out[i]] != LINF ? dist[st.out[i]] : -1) << " \n"[i==n];
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
