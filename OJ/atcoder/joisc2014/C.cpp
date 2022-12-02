#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define i128 __int128
#define ld long double
#define ui unsigned int
#define ull unsigned long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define vi vector<int>
#define vvi vector<vector<int> >
#define vll vector<ll>
#define vvll vector<vector<ll> >
#define lb lower_bound
#define ub upper_bound
#define pb push_back
#define pf push_front
#define ppf pop_front
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define rep(i, a, b) for(ll i = a; i < b; ++i)
#define per(i, a, b) for(ll i = a; i > b; --i)
#define each(x, v) for(auto& x: v)
#define len(x) x.size()
#define elif else if
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define mst(x, a) memset(x, a, sizeof(x))
#ifndef lowbit
#define lowbit(x) (x & (-x))
#endif
#define bitcnt(x) (__builtin_popcountll(x))
#define _up(x) (int)ceil(1.0*x)
#define _down(x) (int)floor(1.0*x)
#define endl "\n"
mt19937 rng( chrono::steady_clock::now().time_since_epoch().count() );
#define Ran(a, b) rng() % ( (b) - (a) + 1 ) + (a)
template <class T>
using pq = priority_queue<T>;
template <class T>
using pqg = priority_queue<T, vector<T>, greater<T> >;
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
		if (y & 1)	res = res * cur % mod;
		cur = ONE * cur * cur % mod;
		y >>= 1;
	}
	return res % mod;
}
ll probabilityMod(ll x, ll y, ll mod) {
	return x * pow(y, mod-2, mod) % mod;
}
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 1e5 + 10;

ll a[N], num[N], ans[N], cnt[N], clear[N], belong[N];
int n, m, sq;
struct query {
    int l, r, i;
    bool operator<(const query &o) const {
        if(belong[l] != belong[o.l]) return belong[l] < belong[o.l];
        else return r < o.r;
    }
} Q[N];

void solve() {
	cin >> n >> m;
    sq = sqrt(n);   
    rep(i, 1, n+1) cin >> a[i], num[i] = a[i], belong[i] = (i-1) / sq + 1;
    sort(num+1, num+1+n);
    int un = unique(num+1, num+1+n) - num - 1;
    rep(i, 1, n+1) a[i] = lb(num+1, num+1+un, a[i]) - num;
    rep(i, 0, m) cin >> Q[i].l >> Q[i].r, Q[i].i = i;
    sort(Q, Q + m);
    int i = 0;
    rep(j, 1, belong[n]+1) {
        int br = min(n, sq * j);
        int l = br + 1, r = br, clearnum = 0;
        ll aans = 0;
        for(; belong[Q[i].l] == j; i++) {
            if(belong[Q[i].r] == j) {
                ll ccnt[N];
                rep(k, Q[i].l, Q[i].r+1) ccnt[a[k]] = 0;
                rep(k, Q[i].l, Q[i].r+1) {
                    ccnt[a[k]]++;
                    ans[Q[i].i] = max(ans[Q[i].i], ccnt[a[k]] * num[a[k]]);
                }
                continue;
            }
            while(r < Q[i].r) {
                r++;
                if(!cnt[a[r]]) clear[clearnum++] = a[r];
                cnt[a[r]]++;
                aans = max(aans, cnt[a[r]] * num[a[r]]);
            }
            ll t = aans;
            while(l > Q[i].l) {
                cnt[a[--l]]++;
                aans = max(aans, cnt[a[l]] * num[a[l]]);
            }
            ans[Q[i].i] = aans;
            aans = t;
            while(l <= br) --cnt[a[l++]];
        }
        rep(k, 0, clearnum) cnt[clear[k]] = 0;
    }
    rep(i, 0, m) cout << ans[i] << endl;
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
