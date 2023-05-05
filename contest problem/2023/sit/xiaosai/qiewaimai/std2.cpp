#include <bits/stdc++.h>

using namespace std;

mt19937 rng( chrono::steady_clock::now().time_since_epoch().count() );

const int base = 13331;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto&& i : a) cin >> i;
    map<int, uint64_t> M;
    for (auto&& i : a) M[i] = rng();
    vector<uint64_t> h(n + 1);
    for (int i = 0; i < n; i++) h[i+1] = h[i] * base + M[a[i]];
    vector<uint64_t> power = {1};
    for (int i = 0; i < n; i++) power.push_back(power.back() * base);
    auto calc = [&] (int l, int r) -> uint64_t {
        return h[r] - h[l - 1] * power[r - l + 1];
    };
    long long ans = 0;
    for (int i = 1; i <= n; i++) {
        int l = i - 1, r = n + 1;
        while (l + 1 < r) {
            int mid = l + r >> 1;
            if (calc(i, mid) == calc(1, mid - i + 1)) l = mid;
            else r = mid;
        }
        ans += l - i + 1;
    }
    cout << ans << "\n";
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
