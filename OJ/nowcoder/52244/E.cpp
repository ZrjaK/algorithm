#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector dp(n + 1, vector(30, vector(30, vector(30, -0x3f3f3f3f))));
    dp[0][0][0][0] = 0;
    for (int i = 0; i < n; i++) {
        int A, B, C, D;
        cin >> A >> B >> C >> D;
        for (int a = 0; a <= n / 4; a++) 
            for (int b = 0; b <= n / 4; b++)
                for (int c = 0; c <= n / 4; c++) {
                    dp[i+1][a+1][b][c] = max(dp[i+1][a+1][b][c], dp[i][a][b][c] + A);
                    dp[i+1][a][b+1][c] = max(dp[i+1][a][b+1][c], dp[i][a][b][c] + B);
                    dp[i+1][a][b][c+1] = max(dp[i+1][a][b][c+1], dp[i][a][b][c] + C);
                    dp[i+1][a][b][c] = max(dp[i+1][a][b][c], dp[i][a][b][c] + D);
        }
    }
    cout << dp[n][n/4][n/4][n/4] << '\n';
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
