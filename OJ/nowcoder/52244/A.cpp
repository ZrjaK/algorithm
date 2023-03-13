#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    map<int, int> M;
    for (auto& i: a) cin >> i, M[i]++;
    long long ans = 0;
    for (auto [k, v] : M) ans += 1ll * v * v;
    cout << ans << '\n';
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
