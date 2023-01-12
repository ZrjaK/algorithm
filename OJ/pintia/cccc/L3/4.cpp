#include <bits/stdc++.h>
#define rep(i, a, b) for(int i = a; i < b; i++)
using namespace std;

const int N = 1e6 + 10;
int parent[N];
int _size[N];
int nums_set;

int find(int i) {
    if (parent[i] != i) {
        parent[i] = find(parent[i]);
    }
    return parent[i];
}

void _union(int i, int j) {
    i = find(i), j = find(j);
    parent[i] = j;
    _size[j] += i;
    nums_set--;
}

int m, n, l, t;
int a[65][1300][130];
map<int, int> mp;

int f(int x, int y, int z) {
    return z * m * n + x * n + y;
}

int check(int x, int y, int z) {
    return 0 <= x && x < m && 0 <= y && y < n && 0 <= z && z < l;
}

signed main() {
    cin >> m >> n >> l >> t;
    for(int i = 0; i < n * m * l; i++) parent[i] = i;
    for(int i = 0; i < n * m * l; i++) _size[i] = 1;
    nums_set = n * m * l;
    rep(k, 0, l) rep(i, 0, m) rep(j, 0, n) cin >> a[k][i][j];
    int d[2] = {-1, 1};
    rep(x, 0, m) rep(y, 0, n) rep(z, 0, l) rep(k, 0, 2) {
        if(a[z][x][y] && check(x+d[k], y, z) && a[z][x+d[k]][y]) _union(f(x, y, z), f(x+d[k], y, z));
        if(a[z][x][y] && check(x, y+d[k], z) && a[z][x][y+d[k]]) _union(f(x, y, z), f(x, y+d[k], z));
        if(a[z][x][y] && check(x, y, z+d[k]) && a[z+d[k]][x][y]) _union(f(x, y, z), f(x, y, z+d[k]));
    }
    rep(i, 0, m) rep(j, 0, n) rep(k, 0, l) if(a[k][i][j]) mp[find(f(i, j, k))]++;
    int ans = 0;
    for(auto it = mp.begin(); it != mp.end(); it = next(it))
        if(it->second >= t) ans += it->second;
    cout << ans << endl;
}