#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<int> c(n);
    vector<int> cnt(n);
    for (auto& i : c) cin >> i, i--, cnt[i]++;
    vector<int> w(n);
    for (auto& i : w) cin >> i;
    vector<int> cc;
    vector<int> pos(n);
    for (int i = 0; i < n; i++) if (cnt[i] >= 2) pos[i] = cc.size(), cc.push_back(i);
    vector<vector<int>> d(n), g(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        d[u].push_back(v);
    }
    vector dp(n, vector<int>(1 << cc.size()));
    for (int i = 0; i < n; i++) for (int mask = 0; mask < 1 << cc.size(); mask++) {
        for (auto& j : d[i]) {
            dp[j][mask] = max(dp[j][mask], dp[i][mask]);
            if (cnt[c[i]] < 2) dp[j][mask] = max(dp[j][mask], dp[i][mask] + w[c[i]]);
            else if (!(mask >> pos[c[i]] & 1)) dp[j][mask | 1 << pos[c[i]]] = max(dp[j][mask | 1 << pos[c[i]]], dp[i][mask] + w[c[i]]);
        }
    }
    for (int i = 0; i < n; i++) {
        int ans = 0;
        if (cnt[c[i]] < 2) ans = max(ans, w[c[i]] + *max_element(dp[i].begin(), dp[i].end()));
        else for (int mask = 0; mask < 1 << cc.size(); mask++) {
            if (!(mask >> pos[c[i]] & 1)) ans = max(ans, dp[i][mask] + w[c[i]]);
        }
        cout << ans << "\n";
    }
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