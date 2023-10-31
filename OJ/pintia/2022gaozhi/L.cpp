#include <bits/stdc++.h>

using namespace std;

using ll = long long;

const long long inf = 1e18;

void solve() {
    int n;
    cin >> n;
    vector<ll> a(n);
    for (auto& i : a) cin >> i;
    vector<vector<int>> d(n);
    for (int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        x--, y--;
        d[x].push_back(y);
        d[y].push_back(x);
    }
    vector<int> sz(n, 1);
    vector dp1(n, vector(n + 1, -inf));
    vector dp2(n, vector(n + 1, inf));
    vector<ll> ans1(n + 1, -inf), ans2(n + 1, inf);
    auto dfs = [&] (auto dfs, int x, int fa) -> void {
        dp1[x][0] = dp2[x][0] = 0;
        if (a[x]) dp1[x][1] = dp2[x][1] = ans1[1] = ans2[1] = 0;
        for (auto& y : d[x]) if (y != fa) {
            auto ndp1 = dp1[x], ndp2 = dp2[x];
            dfs(dfs, y, x);
            for (int i = 0; i <= sz[x]; i++) for (int j = 1; j <= sz[y]; j++) {
                ndp1[i + j] = max(ndp1[i + j], dp1[x][i] + dp1[y][j] + 2);
                ndp2[i + j] = min(ndp2[i + j], dp2[x][i] + dp2[y][j] + 2);
                if (i) {
                    ans1[i + j] = max(ans1[i + j], dp1[x][i] + dp1[y][j] + 2);
                    ans2[i + j] = min(ans2[i + j], dp2[x][i] + dp2[y][j] + 2);
                }
            }
            dp1[x] = ndp1, dp2[x] = ndp2;
            sz[x] += sz[y];
        }
    };
    dfs(dfs, 0, -1);
    for (int i = 1; i <= n; i++) {
        if (ans1[i] >= 0) cout << ans1[i] << " " << ans2[i] << "\n";
        else cout << "-1 -1\n";
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