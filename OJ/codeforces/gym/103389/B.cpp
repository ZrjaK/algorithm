#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, m;
    cin >> m >> n;
    string s;
    cin >> s;
    vector<vector<int>> pos(m);
    for (int i = 0; i < n; i++) pos[s[i] - 97].push_back(i);
    for (int i = 0; i < m; i++) pos[i].push_back(n);
    vector<vector<int>> nxt(20, vector<int>(n + 1));
    nxt[0][n] = n;
    for (int i = 0; i < n; i++) {
        int x = i;
        for (int j = 0; j < m; j++) {
            auto it = upper_bound(pos[j].begin(), pos[j].end(), i);
            assert(it != pos[j].end());
            x = max(x, *it);
        }
        nxt[0][i] = x;
    }
    for (int bit = 1; bit < 20; bit++) {
        for (int i = 0; i <= n; i++) {
            nxt[bit][i] = nxt[bit - 1][nxt[bit - 1][i]];
        }
    }
    int q;
    cin >> q;
    while (q--) {
        int l, r;
        cin >> l >> r;
        l--;
        auto calc = [&] (int X) -> int {
            if (X >= r) return 0;
            int res = 1;
            int x = X;
            for (int bit = 19; bit >= 0; bit--) {
                if (nxt[bit][x] < r) x = nxt[bit][x], res += 1 << bit;
            }
            return res;
        };
        int ans = 1e9;
        for (int i = 0; i < m; i++) 
            ans = min(ans, calc(*lower_bound(pos[i].begin(), pos[i].end(), l)));
        cout << ans + 1 << "\n";
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