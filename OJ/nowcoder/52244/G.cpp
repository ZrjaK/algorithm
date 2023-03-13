#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n;
    cin >> n;
    int N = (1 << 17) - 1;
    vector<int> cnt(N + 1);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cnt[x]++;
    }
    vector<long long> f(N + 1, cnt[0]);
    for (int i = 0; i <= N; i++) {
        for (int j = i; j; j = (j - 1) & i) 
            f[i] += cnt[j];
    }
    long long ans = 0;
    for (int i = 0; i <= N; i++) 
        ans += 1ll * cnt[i] * f[N ^ i];
    cout << ans << '\n';
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
