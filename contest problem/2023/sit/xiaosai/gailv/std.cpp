#include <bits/stdc++.h>

using namespace std;

__int128_t fac[25];

int init = [] () {
    fac[0] = 1;
    for (int i = 1; i <= 24; i++) fac[i] = fac[i-1] * i;
    return 0;
} ();

long long C(int n, int m) {
    return fac[n] / (fac[m] * fac[n - m]);
}

long double P(int a, int b) {
    return (long double) C(8, a) * C(8, b) * C(8, 12 - a - b) / C(24, 12);
}

void solve() {
    long double ans = 0;
    for (int a = 0; a <= 8; a++) {
        for (int b = 0; b <= 8 && b <= 12 - a; b++) {
            int c = 12 - a - b;
            if (c < 0 || c > 8) continue;
            vector<int> tmp = {a, b, c};
            sort(tmp.begin(), tmp.end(), greater<>());
            if (tmp == vector{8, 4, 0}) {
                ans += P(a, b) * 100;
            }
            if (tmp == vector{7, 5, 0}) {
                ans += P(a, b) * 20;
            }
            if (tmp == vector{8, 2, 2}) {
                ans += P(a, b) * 10;
            }
            if (tmp == vector{8, 3, 1}) {
                ans += P(a, b) * 10;
            }
            if (tmp == vector{6, 6, 0}) {
                ans += P(a, b) * 20;
            }
            if (tmp == vector{5, 4, 3}) {
                ans += P(a, b) * -10;
            }
            if (tmp == vector{7, 3, 2}) {
                ans += P(a, b) * 2;
            }
            if (tmp == vector{7, 4, 1}) {
                ans += P(a, b) * 2;
            }
            if (tmp == vector{6, 4, 2}) {
                ans += P(a, b) * 1;
            }
            if (tmp == vector{5, 5, 2}) {
                ans += P(a, b) * 1;
            }
            if (tmp == vector{6, 5, 1}) {
                ans += P(a, b) * 1;
            }
            if (tmp == vector{6, 3, 3}) {
                ans += P(a, b) * 1;
            }
            if (tmp == vector{4, 4, 4}) {
                ans += P(a, b) * 1;
            }
        }
    }
    cout << setprecision(12) << ans;
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
