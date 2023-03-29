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
