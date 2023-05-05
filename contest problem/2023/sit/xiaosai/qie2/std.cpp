#include <bits/stdc++.h>

using namespace std;

template <class T, T (*func)(T, T)>
struct RangeQuery {
    vector<vector<T>> data;
    RangeQuery(vector<T>& init) {
        data = vector<vector<T>>();
        data.push_back(vector(init));
        int n = init.size();
        for (int i = 1; 2 * i <= n; i <<= 1) {
            auto pre = data.back();
            vector<T> tmp;
            for (int j = 0; j < n - 2 * i + 1; j++) {
                tmp.push_back(func(pre[j], pre[j+i]));
            }
            data.push_back(tmp);
        }
    }

    // [start, stop)
    T query(int start, int stop) {
        int depth = __lg(stop - start);
        return func(data[depth][start], data[depth][stop - (1 << depth)]);
    }
};

int op1(int a, int b) {
    return min(a, b);
}

int op2(int a, int b) {
    return max(a, b);
}

void solve() {
    int n, m, s;
    cin >> n >> m >> s;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    
    RangeQuery<int, op1> min_rmq(a);
    RangeQuery<int, op2> max_rmq(a);

    auto calc = [&] (int l, int r) -> long long {
        int mn = min_rmq.query(l, r + 1);
        int mx = max_rmq.query(l, r + 1);
        return 1ll * (r - l + 1) * ((mn + mx) / 2) + s;
    };

    vector<long long> dp(n + 1, LONG_LONG_MAX);
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i && j <= m; j++) {
            dp[i] = min(dp[i], dp[i - j] + calc(i - j + 1, i));
        }
    }

    cout << dp[n];
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
