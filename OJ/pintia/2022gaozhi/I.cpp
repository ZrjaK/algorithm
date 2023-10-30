#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
    ll n;
    cin >> n;
    ll sq = sqrt(n);
    if (sq * sq <= n && n < sq * sq + sq) cout << "Alice" << "\n";
    else cout << "Bob" << "\n";

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