#include <bits/stdc++.h>

using namespace std;

using ll = long long;

vector<ll> mul(vector<ll>& a, vector<ll>& b) {
    vector<ll> c(a.size(), -1e18);
    for (int i = 0; i < a.size(); i++) for (int j = 0; j < b.size(); j++)
        c[(i + j) % a.size()] = max(c[(i + j) % a.size()], a[i] + b[j]);
    return c;
}

vector<ll> pow(vector<ll> a, ll k) {
    vector<ll> res(a.size(), -1e18);
    res[0] = 0;
    while (k) {
        if (k % 2) res = mul(res, a);
        a = mul(a, a), k /= 2;
    }
    return res;
}

void solve() {
    int n;
    cin >> n;
    vector<ll> v(n);
    for (auto & i : v) cin >> i;
    vector<ll> f(n);
    for (auto & i : f) cin >> i;
    v.insert(v.begin(), v.back());
    v.pop_back();
    ll mxf = *max_element(f.begin(), f.end());
    ll mxv = *max_element(v.begin(), v.end());
    ll k = mxf / mxv;
    if (mxf % mxv || k < 1 || k > 1e9) {
        cout << -1;
        return;
    }
    if (pow(v, k) == f) cout << k;
    else cout << -1;

}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int T = 1;
    // cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}