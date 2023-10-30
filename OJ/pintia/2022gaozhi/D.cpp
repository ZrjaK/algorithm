#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
    ll A, B, C, L, R;
    cin >> A >> B >> C >> L >> R;
    ll x = A * L * L + B * L + C, y = A * R * R + B * R + C;
    if (A == 0) {
        cout << min(x, y) << " " << max(x, y) << "\n";
        return;
    }
    if (A < 0) {
        ll mn_ans = min(x, y);
        ll X = -B / 2 / A;
        ll ans = -2e18;
        for (ll i = X - 5; i <= X + 5; i++) {
            if (L <= i && i <= R) ans = max(ans, A * i * i + B * i + C);
        }
        cout << mn_ans << " " << max(ans, max(x, y)) << "\n";
    } else {
        ll mx_ans = max(x, y);
        ll X = -B / 2 / A;
        ll ans = 2e18;
        for (ll i = X - 5; i <= X + 5; i++) {
            if (L <= i && i <= R) ans = min(ans, A * i * i + B * i + C);
        }
        cout << min(ans, min(x, y)) << " " << mx_ans << "\n";

    }


}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int T = 1;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}