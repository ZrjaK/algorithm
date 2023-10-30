#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
    int n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for(auto& i : a) cin >> i;
    vector<ll> h;
    for (int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        x--, y--;
        h.push_back(min(a[x], a[y]));
    }
    sort(begin(h), end(h));
    ll ans = 0;
    ans += 1ll * *min_element(a.begin(), a.end()) * k;
    while (k--) h.pop_back();
    ans += accumulate(begin(h), end(h), 0ll);
    cout << ans;
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