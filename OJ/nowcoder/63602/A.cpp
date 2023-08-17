#include <bits/stdc++.h>

using namespace std;

void solve () {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto& i : a) cin >> i;
    vector h(31, vector<int>(n + 1));
    for (int bit = 0; bit < 31; bit++) {
        for (int i = 0; i < n; i++) {
            h[bit][i + 1] = h[bit][i] + (a[i] >> bit & 1);
        }
    }
    int q;
    cin >> q;
    while (q--) {
        int l, r;
        cin >> l >> r;
        int ans = 0;
        for (int bit = 0; bit < 31; bit++) {
            int c1 = h[bit][r] - h[bit][l - 1];
            int c0 = r - l + 1 - c1;
            if (c1 < c0) ans |= 1 << bit;
        }
        cout << ans << "\n";
    }
}

signed main () {
    int T = 1;
    // cin >> T;
    while (T--) solve();
    return 0;
}