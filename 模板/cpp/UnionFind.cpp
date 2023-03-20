struct UnionFind {
    vi parent, size;
	int part;
	UnionFind (int n) : part(n) {
        parent = vi(n), size = vi(n);
		rep(i, 0, n) parent[i] = i, size[i] = 1;
	};
	~UnionFind() {}

	int find(int i) {
		if (parent[i] != i) {
			parent[i] = find(parent[i]);
		}
		return parent[i];
	}

	void _union(int i, int j) {
		int x = find(i), y = find(j);
		if (x != y) {
			size[y] += size[x];
			parent[x] = parent[y];
			part -= 1;
		}
	}
};

void solve() {
	int n;
	cin >> n;
	rep(i, 0, n) {
	}

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
