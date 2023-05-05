#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto&& i : a) cin >> i;
    auto check = [&] (int l, int r) -> bool {
        for (int i = 0; l <= r; i++, l++) {
            if (a[i] != a[l]) return false;
        }
        return true;
    };
    long long ans = 0;
    for (int i = 0; i < n; i++) for (int j = i; j < n; j++) {
        if (check(i, j)) ans++;
        else break;
    }
    cout << ans << "\n";
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
