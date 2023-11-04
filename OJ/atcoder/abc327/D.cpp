#include<bits/stdc++.h>

using namespace std;

struct DSU {
    std::vector<int> f, siz;
    
    DSU() {}
    DSU(int n) {
        init(n);
    }
    
    void init(int n) {
        f.resize(n);
        std::iota(f.begin(), f.end(), 0);
        siz.assign(n, 1);
    }
    
    int find(int x) {
        while (x != f[x]) {
            x = f[x] = f[f[x]];
        }
        return x;
    }
    
    bool same(int x, int y) {
        return find(x) == find(y);
    }
    
    bool merge(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) {
            return false;
        }
        siz[x] += siz[y];
        f[y] = x;
        return true;
    }
    
    int size(int x) {
        return siz[find(x)];
    }
};

void solve () {
    int n, m;
    cin >> n >> m;
    vector<int> a(m), b(m);
    for (auto& i : a) cin >> i, i--;
    for (auto& i : b) cin >> i, i--;
    DSU dsu(2 * n);
    for (int i = 0; i < m; i++) {
        dsu.merge(a[i], b[i] + n);
        dsu.merge(a[i] + n, b[i]);
    }
    for (int i = 0; i < n; i++) if (dsu.same(i, i + n)) {
        cout << "No";
        return;
    }
    cout << "Yes";

    


}

signed main () {
    solve();
    return 0;
}