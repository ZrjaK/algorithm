#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
    map<int, vector<int>> pos;
    pos[2].push_back(1);
    pos[3].push_back(2);
    pos[4].push_back(3);
    map<int, int> cur;
    cur[1] = 2, cur[2] = 3, cur[3] = 4;
    for (int i = 0; i < 12; i++) {
        int a, b;
        cin >> a >> b;
        int x = cur[a];
        vector<int> h;
        while (pos[x].back() != a) h.push_back(pos[x].back()), pos[x].pop_back();
        assert(pos[x].size() && pos[x].back() == a);
        h.push_back(pos[x].back()), pos[x].pop_back();
        while (h.size()) {
            pos[x + b].push_back(h.back());
            cur[h.back()] = x + b;
            h.pop_back();
        }
    }
    if (pos[9].size() == 3) cout << "Y\n";
    else cout << "N\n";

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