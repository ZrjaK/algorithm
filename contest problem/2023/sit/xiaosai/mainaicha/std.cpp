#include <bits/stdc++.h>

using namespace std;

const int N = 1e6 + 10;

int fact[N];
int init = [] () {
    for (int i = 1; i < N; i++) {
        for(int j = i; j < N; j += i) {
            fact[j]++;
        }
    }

    for (int i = 1; i < N; i++) {
        fact[i] += fact[i-1];
    }
    
    return 0;
} ();

void solve() {
    int n;
    cin >> n;
    cout << fact[n]<< "\n";
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
