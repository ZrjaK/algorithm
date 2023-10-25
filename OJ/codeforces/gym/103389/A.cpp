#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, x, y;
    cin >> n >> x >> y;
    x--, y--;
    vector<int> k(n);
    for(auto& i : k) cin >> i;
    int m;
    cin >> m;
    vector<int> p(m);
    for(auto& i : p) cin >> i;
    vector<int> X1, X2;
    for (int i = x + 1; i < n; i++) X1.push_back(k[i]);
    for (int i = x - 1; i >= 0; i--) X2.push_back(k[i]);
    if (x > y) swap(X1, X2);
    X1.resize(abs(x - y));
    if (m > X1.size()) {
        cout << "Wrong";
        return;
    }
    for (int i = 0; i < m; i++) if (X1[i] != p[i]) {
        cout << "Wrong";
        return;
    }
    if (m > X2.size()) {
        cout << "Right";
        return;
    }
    for (int i = 0; i < m; i++) if (X2[i] != p[i]) {
        cout << "Right";
        return;
    }
    cout << "Unsure";

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