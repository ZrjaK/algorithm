template <typename GT>
pair<int, int> find_centroids(GT& G) {
    int n = G.n;
    vector<int> parent(n, -1);
    vector<int> sz(n);
    vector<int> q = {0};
    for (int i = 0; i < q.size(); i++) {
        int u = q[i];
        for (auto&& [v, w]: G[u])
        if (v != parent[u]) {
            parent[v] = u;
            q.emplace_back(v);
        }
    }
    for (int i = n - 1; i >= 0; i--) {
        int v = q[i];
        sz[v] += 1;
        int p = parent[v];
        if (p != -1) sz[p] += sz[v];
    }

    int m = n / 2;
    auto check = [&](int u) -> bool {
        if (n - sz[u] > m) return false;
        for (auto&& [v, w]: G[u]) {
            if (v != parent[u] && sz[v] > m) return false;
        }
        return true;
    };
    pair<int, int> ans = {-1, -1};
    for (int i = 0; i < n; i++) if (check(i)) {
        if (ans.first != -1) {
            ans.second = i;
        } else {
            ans.first = i;
        }
    }
    return ans;
}

template <typename GT>
struct Centroid_Decomposition {
    using edge_type = typename GT::edge_type;
    GT& G;
    int n;
    vector<int> sz;
    vector<int> parent;
    vector<int> cdep; // depth in centroid tree

    bool calculated;

    Centroid_Decomposition(GT& G)
        : G(G), n(G.n), sz(G.n), parent(G.n), cdep(G.n, -1) {
        calculated = 0;
        build();
    }

private:
  int find(int u) {
    vector<int> q = {u};
    parent[u] = -1;
    int p = 0;
    while (p < q.size()) {
      int u = q[p++];
      sz[u] = 0;
      for (auto&& [v, w] : G[u]) {
        if (v == parent[u] || cdep[v] != -1) continue;
        parent[v] = u;
        q.emplace_back(v);
      }
    }
    while (q.size()) {
        int u = q.back();
        q.pop_back();
        sz[u] += 1;
        if (p - sz[u] <= p / 2) return u;
        sz[parent[u]] += sz[u];
    }
    return -1;
  }
  void build() {
    assert(!calculated);
    calculated = 1;

    vector<pair<int, int>> st;
    st.emplace_back(0, 0);
    while (!st.empty()) {
        auto [lv, v] = st.back();
        st.pop_back();
        auto c = find(v);
        cdep[c] = lv;
        for (auto&& [to, w] : G[c]) {
            if (cdep[to] == -1) { st.emplace_back(lv + 1, to); }
        }
    }
  }

public:
  // vector of pairs (v, path data v)

  template <typename E, typename F>
  vector<vector<pair<int, E>>> collect(int root, E root_val, F f) {
    vector<vector<pair<int, E>>> res = {{{root, root_val}}};
    for (auto&& [nxt, w] : G[root]) {
      if (cdep[nxt] < cdep[root]) continue;
      vector<pair<int, E>> dat;
      int p = 0;
      dat.eb(nxt, f(root_val, tuple<int, int, E>{root, nxt, w}));
      parent[nxt] = root;
      while (p < len(dat)) {
        auto [u, val] = dat[p++];
        for (auto&& [v, w] : G[u]) {
          if (v == parent[u]) continue;
          if (cdep[v] < cdep[root]) continue;
          parent[v] = u;
          dat.emplace_back(v, f(val, tuple<int, int, E>{u, v, w}));
        }
      }
      res.emplace_back(dat);
      res[0].insert(res[0].end(), dat.begin(), dat.end());
    }
    return res;
  }

  vector<vector<pair<int, int>>> collect_dist(int root) {
    auto f = [&](int x, auto e) -> int { return x + 1; };
    return collect(root, 0, f);
  }

  // (V, H), (V[i] in G) = (i in H).

  // 0,1,2... is a dfs order in H.

  pair<vector<int>, Graph<typename GT::cost_type, true>> get_subgraph(int root) {
    static vector<int> conv;
    while (len(conv) < n) conv.emplace_back(-1);

    vector<int> q;
    using cost_type = typename GT::cost_type;
    vector<tuple<int, int, cost_type>> edges;

    auto dfs = [&](auto& dfs, int u, int p) -> void {
      conv[u] = len(q);
      q.emplace_back(u);
      for (auto&& [v, cost] : G[u]) {
        if (v == p) continue;
        if (cdep[v] < cdep[root]) continue;
        dfs(dfs, v, u);
        edges.emplace_back(conv[u], conv[v], cost);
      }
    };
    dfs(dfs, root, -1);
    int n = len(q);
    Graph<typename GT::cost_type, true> H(n);
    for (auto&& [a, b, c]: edges) H.add(a, b, c);
    H.build();
    for (auto&& v: q) conv[v] = -1;
    return {q, H};
  }
};