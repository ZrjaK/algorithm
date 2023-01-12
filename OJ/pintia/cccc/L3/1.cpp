#include <bits/stdc++.h>
#define long long ll;
using namespace std;

const int N = 1e4 + 10;
int a[N];
int n, m;
int memo[N][110];

int dp(int i, int rest) {
    if(rest < 0) return -2;
    if(i == n) return (rest == 0) ? 0: -2;
    if(memo[i][rest] != -1) return memo[i][rest];
    int res1 = dp(i+1, rest);
    int res2 = dp(i+1, rest-a[i]);
    if(res2 != -2) memo[i][rest] = 1;
    else if(res1 != -2) memo[i][rest] = 0;
    else memo[i][rest] = -2;
    return memo[i][rest];
}
vector<int> ans;

signed main() {
    memset(memo, -1, sizeof(memo));
    cin >> n >> m;
    for(int i = 0; i < n; i++) cin >> a[i];
    sort(a, a+n);
    if(dp(0, m) == -2) cout << "No Solution" << endl;
    else {
        for(int i = 0; i < n; i++)
            if(dp(i, m) == 1) ans.push_back(a[i]), m -= a[i];
    }
    for(int i = 0; i < ans.size(); i++)
        cout << ans[i] << " \n"[i==ans.size()-1];
    return 0;
}