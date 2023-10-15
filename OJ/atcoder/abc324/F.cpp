#include<bits/stdc++.h>

using namespace std;

void solve () {
    int n, m;
    cin >> n >> m;
    vector<vector<tuple<int, int, int>>> d(n);
    for (int i = 0; i < m; i++) {
        int u, v, b, c;
        cin >> u >> v >> b >> c;
        u--, v--;
        d[u].emplace_back(v, b, c);
    }
    using T = tuple<double, long long, long long, int>;
    double l = 0, r = 1e4;
    for (int _ = 0; _ < 100; _++) {
        double mid = (l + r) / 2;
        vector<double> dist(n, -1e18);
        dist[0] = 0;
        for (int i = 0; i < n; i++) {
            for (auto& [j, b, c] : d[i]) {
                dist[j] = max(dist[j], dist[i] + b - c * mid);
            }
        }
        if (dist[n - 1] >= 0) l = mid;
        else r = mid;
    }
    cout << l;




}

signed main () {
    cout << fixed << setprecision(15);
    solve();
    return 0;
}