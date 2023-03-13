#include <bits/stdc++.h>

using namespace std;

template <class T> using heapq = std::priority_queue<T, vector<T>, greater<T>>;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<pair<int, int>>> G(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        G[u].push_back({v, w});
        G[v].push_back({u, w});
    }
    heapq<pair<pair<long long, long long>, int>> pq;
    vector<pair<long long, long long>> dist(n, {INT64_MAX, INT64_MAX});
    pq.push({{1, 0}, 0});
    dist[0] = {1, 0};
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        for (auto& [v, w] : G[u]) {
            pair<long long, long long> nd = {d.first + 1, d.second + w};
            if (dist[v] > nd) {
                dist[v] = nd;
                pq.push({dist[v], v});
            }
        }
    }
    cout << dist[n-1].first << " " << dist[n-1].second << '\n';

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
