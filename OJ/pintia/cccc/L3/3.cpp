#include <bits/stdc++.h>
#define rep(i, a, b) for(int i = a; i < b; i++)
using namespace std;

const int N = 1e3 + 10;
int parent[N];

int find(int i) {
    if (parent[i] != i) {
        parent[i] = find(parent[i]);
    }
    return parent[i];
}

void _union(int i, int j) {
    parent[find(i)] = find(j);
}

int n;
vector<int> d[N];
map<int, int> m;
vector<int> ans;

signed main() {
    for(int i = 0; i < N; i++) parent[i] = i;
    cin >> n;
    string s;
    rep(i, 0, n) {
        cin >> s;
        s.pop_back();
        int k = atoi(s.c_str());
        int x;
        rep(j, 0, k) cin >> x, d[x].push_back(i);
    }
    rep(i, 0, N) rep(j, 1, d[i].size()) _union(d[i][j], d[i][0]);
    rep(i, 0, n) m[find(i)]++;
    for(auto it = m.begin(); it != m.end(); it = next(it)) ans.push_back(it->second);
    sort(ans.begin(), ans.end(), greater<>());
    cout << ans.size() << "\n";
    rep(i, 0, ans.size()) cout << ans[i] << " \n"[i==ans.size()-1];
}