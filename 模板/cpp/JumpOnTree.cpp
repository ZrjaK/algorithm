struct JumpOnTree {
    int n, logn, root = 0;
    vi depth;
    vvi edges, parent;
    JumpOnTree (vvi &e): edges(e), n(len(e)) {
        logn = n > 1 ? __lg(n - 1) + 1 : 0;
        depth = vi(n, -1), depth[root] = 0;
        parent = vvi(logn, vi(n, -1));
        dfs(), doubling();
    };
    JumpOnTree (vvi &e, int rt): edges(e), n(len(e)) {
        root = rt;
        logn = n > 1 ? __lg(n - 1) + 1 : 0;
        depth = vi(n, -1), depth[root] = 0;
        parent = vvi(logn, vi(n, -1));
        dfs(), doubling();
    };
    void dfs() {
        vi q = {root};
        while (!q.empty()) {
            int u = q.back();
            q.pop_back();
            each(v, edges[u]) if (depth[v] == -1) {
                depth[v] = depth[u] + 1;
                parent[0][v] = u;
                q.pb(v);
            }
        }
    }

    void doubling() {
        rep(i, 1, logn) rep(u, 0, n) {
            int p = parent[i - 1][u];
            if (p != -1) parent[i][u] = parent[i - 1][p];
        }
    }

    int lca(int u, int v) {
        int du = depth[u], dv = depth[v];
        if (du > dv) swap(du, dv), swap(u, v);
        int d = dv - du;
        for(int d = dv - du, i = 0; d > 0; d >>= 1, i++) {
            if (d & 1) v = parent[i][v];
        }
        if (u == v) return u;
        int lgn = du > 1 ? __lg(du - 1) + 1 : 0;
        per(i, lgn, -1) {
            int pu = parent[i][u];
            int pv = parent[i][v];
            if (pu != pv) u = pu, v = pv;
        }
        return parent[0][u];
    }

    int jump(int u, int v, int k) {
        if (!k) return u;
        int p = lca(u, v);
        int d1 = depth[u] - depth[p], d2 = depth[v] - depth[p];
        if (d1 + d2 < k) return -1;
        int d;
        if (k <= d1) d = k;
        else u = v, d = d1 + d2 - k;
        for(int i = 0; d > 0; d >>= 1, i++) {
            if (d & 1) u = parent[i][u];
        }
        return u;
    }

    int dist(int u, int v) {
        return depth[u] + depth[v] - 2 * depth[lca(u, v)];
    }
};
