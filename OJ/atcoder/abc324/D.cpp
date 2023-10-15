#include<bits/stdc++.h>

using namespace std;

void solve () {
    int n;
    string s;
    cin >> n >> s;
    vector<int> C(10);
    for(auto& i : s) C[i - 48]++;
    int ans = 0;
    for (int i = 0; i <= 4e6; i++) {
        string t = to_string(1ll * i * i);
        while (t.size() < s.size()) t.push_back('0');
        vector<int> cnt(10);
        for(auto& x : t) cnt[x - 48]++;
        if (C == cnt) ans++;
    }
    cout << ans;


}

signed main () {
    solve();
    return 0;
}