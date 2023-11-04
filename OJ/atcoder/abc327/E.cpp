#include<bits/stdc++.h>

using namespace std;

void solve () {
    int n;
    cin >> n;
    vector<int> P(n);
    for (auto& i : P) cin >> i;
    reverse(P.begin(), P.end());
    vector<double> p9 = {1};
    for (int i = 0; i < n; i++) p9.push_back(p9.back() * 0.9);
    vector<double> dp(n + 1, -1e18);
    dp[0] = 0;
    for (int i = 0; i < n; i++) {
        vector<double> ndp(dp.begin(), dp.end());
        for (int j = 0; j < n; j++) {
            ndp[j + 1] = max(ndp[j + 1], dp[j] + p9[j] * P[i]);
        }
        dp = ndp;
    }
    double s = 0;
    double ans = -1e18;
    for (int i = 1; i <= n; i++) {
        s += p9[i - 1];
        ans = max(ans, dp[i] / s - 1200 / sqrt(i));
    }
    cout << ans;
    


}

signed main () {
    cout << fixed << setprecision(15);
    solve();
    return 0;
}