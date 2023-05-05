#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;

vector<int> z_function(vector<int>& s) {
  int n = (int)s.size();
  vector<int> z(n);
  for (int i = 1, l = 0, r = 0; i < n; ++i) {
    if (i <= r && z[i - l] < r - i + 1) {
      z[i] = z[i - l];
    } else {
      z[i] = max(0, r - i + 1);
      while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
    }
    if (i + z[i] - 1 > r) l = i, r = i + z[i] - 1;
  }
  return z;
}


void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto&& i : a) cin >> i;
    auto z = z_function(a);
    cout << accumulate(z.begin(), z.end(), 0ll) + n << "\n";
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
