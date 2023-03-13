#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, T;
    cin >> n;
    long long a1, b1, c1;
    cin >> a1 >> b1 >> c1;
    long long a2, b2, c2;
    cin >> a2 >> b2 >> c2;
    vector<int> ans(4);
    for (int i = 0; i < n ; i++) {
        long long  x, y;
        cin >> x >> y;
        long long d1 = a1 * x + b1 * y + c1;
        long long d2 = a2 * x + b2 * y + c2;
        if (d1 > 0 && d2 > 0) ans[0]++;
        if (d1 < 0 && d2 > 0) ans[1]++;
        if (d1 > 0 && d2 < 0) ans[2]++;
        if (d1 < 0 && d2 < 0) ans[3]++;
    }
    sort(ans.begin(), ans.end());
    for (int i = 0; i < 4; i++) cout << ans[i] << " \n"[i==n-1];
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
