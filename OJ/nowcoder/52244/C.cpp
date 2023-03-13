#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, T;
    cin >> n >> T;
    unordered_map<int, int> L1, L2, L3, L4;
    for (int _ = 0; _ < T; _++) {
        int x, y;
        cin >> x >> y;
        if (L1[x] || L2[y] || L3[x + y] || L4[-x + y]) {
            cout << "No" << "\n";
        } else {
            L1[x] = 1;
            L2[y] = 1;
            L3[x + y] = 1;
            L4[-x + y] = 1;
            cout << "Yes" << '\n';
        }
    }
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
