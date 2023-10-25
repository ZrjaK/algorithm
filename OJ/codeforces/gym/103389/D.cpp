#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for(auto& i : a) cin >> i;
    ll ans = 0;
    for (int i = 1 ; i < n; i++) ans += max(a[i - 1], a[i]);
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