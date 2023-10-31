#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
    ll n, m, k;
    cin >> n >> m >> k;
    vector<array<ll, 7>> Q;
    for (int _ = 0; _ < m; _++) {
        ll i, j, op, a, b, d, v;
        cin >> i >> j >> op >> a >> b >> d >> v;
        i--, j--;
        Q.push_back({i, j, op, a, b, d, v});
    }

    if (n == 2) {
        ll ans = 0;
        for (ll A = 0; A <= k; A++) 
            for (ll B = 0; B <= k; B++) {
            vector<ll> h = {A, B};
            ll res = 0;
            for (auto& [i, j, op, a, b, d, v] : Q) {
                if (op == 0 && a * h[i] + b * h[j] <= d) res += v;
                if (op == 1 && a * h[i] + b * h[j] >= d) res += v;
            }
            ans = max(ans, res);
        }
        cout << ans;
    }
    if (n == 3) {
        ll ans = 0;
        for (ll A = 0; A <= k; A++) 
            for (ll B = 0; B <= k; B++) 
                for (ll C = 0; C <= k; C++) {
            vector<ll> h = {A, B, C};
            ll res = 0;
            for (auto& [i, j, op, a, b, d, v] : Q) {
                if (op == 0 && a * h[i] + b * h[j] <= d) res += v;
                if (op == 1 && a * h[i] + b * h[j] >= d) res += v;
            }
            ans = max(ans, res);
        }
        cout << ans;
    }
    if (n == 4) {
        ll ans = 0;
        for (ll A = 0; A <= k; A++) 
            for (ll B = 0; B <= k; B++) 
                for (ll C = 0; C <= k; C++) 
                    for (ll D = 0; D <= k; D++) {
            vector<ll> h = {A, B, C, D};
            ll res = 0;
            for (auto& [i, j, op, a, b, d, v] : Q) {
                if (op == 0 && a * h[i] + b * h[j] <= d) res += v;
                if (op == 1 && a * h[i] + b * h[j] >= d) res += v;
            }
            ans = max(ans, res);
        }
        cout << ans;
    }
    if (n == 5) {
        ll ans = 0;
        for (ll A = 0; A <= k; A++) 
            for (ll B = 0; B <= k; B++) 
                for (ll C = 0; C <= k; C++) 
                    for (ll D = 0; D <= k; D++) 
                        for (ll E = 0; E <= k; E++) {
            vector<ll> h = {A, B, C, D, E};
            ll res = 0;
            for (auto& [i, j, op, a, b, d, v] : Q) {
                if (op == 0 && a * h[i] + b * h[j] <= d) res += v;
                if (op == 1 && a * h[i] + b * h[j] >= d) res += v;
            }
            ans = max(ans, res);
        }
        cout << ans;
    }
    if (n == 6) {
        ll ans = 0;
        for (ll A = 0; A <= k; A++) 
            for (ll B = 0; B <= k; B++) 
                for (ll C = 0; C <= k; C++) 
                    for (ll D = 0; D <= k; D++) 
                        for (ll E = 0; E <= k; E++)
                            for (ll F = 0; F <= k; F++) {
            vector<ll> h = {A, B, C, D, E, F};
            ll res = 0;
            for (auto& [i, j, op, a, b, d, v] : Q) {
                if (op == 0 && a * h[i] + b * h[j] <= d) res += v;
                if (op == 1 && a * h[i] + b * h[j] >= d) res += v;
            }
            ans = max(ans, res);
        }
        cout << ans;
    }
    
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