#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> a(n);
    for (auto& i : a) cin >> i.first >> i.second;
    sort(a.begin(), a.end(), [&] (const pair<int, int>& A, const pair<int, int>& B){
        return A.first - A.second < B.first - B.second;
    });
    int ans = 0;
    for (int i = 0; i < k; i++) ans += a[i].second;
    for (int i = k; i < n; i++) ans += a[i].first;
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
