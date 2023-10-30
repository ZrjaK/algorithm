#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    if (n % 2) {
        cout << "No";
        return;
    }
    int f = 0;
    int c = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') f++;
        else f--;
        if (f == -1) f = 1, c++;
    }
    if (f == 2) c++, f -= 2;
    if (f || c > 1) cout << "No";
    else cout << "Yes";

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