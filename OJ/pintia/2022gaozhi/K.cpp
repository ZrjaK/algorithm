#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<ll> p(n);
    for (auto& i : p) cin >> i;
    vector d(n, vector(n, (int)1e9));
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        d[u][v] = min(d[u][v], w);
        d[v][u] = min(d[v][u], w);
    }
    for (int i = 0; i < n; i++) d[i][i] = 0;
    for (int k = 0; k < n; k++) for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    }
    ll ans = 1e18;
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) if (i != j) {
        ll s = 0;
        for (int x = 0; x < n; x++) s += min(d[i][x] * p[x], d[j][x] * p[x]);
        ans = min(ans, s);
    }
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