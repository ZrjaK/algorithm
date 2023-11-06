#include <bits/stdc++.h>

using namespace std;

using ll = long long;

template <typename F>
ll binary_search(F check, ll ok, ll ng, bool check_ok = true) {
  if (check_ok) assert(check(ok));
  while (abs(ok - ng) > 1) {
    auto x = (ng + ok) / 2;
    tie(ok, ng) = (check(x) ? make_pair(x, ng) : make_pair(ok, x));
  }
  return ok;
}

void solve() {
    ll n, m, k;
    cin >> n >> m >> k;
    if (k == 1) return cout << m << "\n", void();
    if (k % 2) {
        auto check = [&] (ll x) -> bool {
            return n - x + 2 * m >= x * (k - 1);
        };
        ll x = binary_search(check, 0, n + 1);
        n -= x;
        k -= 1;
        ll s = n + 2 * m - x * k;
        ll ans = min(s / 2, m);
        s -= 2 * ans;
        ans += s;
        cout << ans << "\n";
    } else {
        ll s = n + 2 * m;
        s %= k;
        ll ans = min(s / 2, m);
        s -= 2 * ans;
        ans += s;
        cout << ans << "\n";
    }
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