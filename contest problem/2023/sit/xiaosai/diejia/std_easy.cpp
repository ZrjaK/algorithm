#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;

void solve() {
    long long n, A, B, k1, k2;
    cin >> n >> A >> B >> k1 >> k2;
    string s;
    cin >> s;
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int x;
        cin >> x;
        x--;
        if (s[x] == '1') {
            s[x] = '0';
        } else {
            s[x] = '1';
        }
        long long a = A, b = B;
        for (int j = 0; j < n; j++) {
            if (s[j] == '0') {
                a = (k1 * a % MOD + b) % MOD;
            } else {
                b = (a + k2 * b % MOD) % MOD;
            }
        }
        cout << a << " " << b << "\n";
    }
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
