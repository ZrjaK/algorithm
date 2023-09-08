#line 2 "graph/base.hpp"

template <typename T>
struct Edge {
  int frm, to;
  T cost;
  int id;
};

template <typename T = int, bool directed = false>
struct Graph {
  int N, M;
  using cost_type = T;
  using edge_type = Edge<T>;
  vector<edge_type> edges;
  vector<int> indptr;
  vector<edge_type> csr_edges;
  vc<int> vc_deg, vc_indeg, vc_outdeg;
  bool prepared;

  class OutgoingEdges {
  public:
    OutgoingEdges(const Graph* G, int l, int r) : G(G), l(l), r(r) {}

    const edge_type* begin() const {
      if (l == r) { return 0; }
      return &G->csr_edges[l];
    }

    const edge_type* end() const {
      if (l == r) { return 0; }
      return &G->csr_edges[r];
    }

  private:
    const Graph* G;
    int l, r;
  };

  bool is_prepared() { return prepared; }
  constexpr bool is_directed() { return directed; }

  Graph() : N(0), M(0), prepared(0) {}
  Graph(int N) : N(N), M(0), prepared(0) {}

  void build(int n) {
    N = n, M = 0;
    prepared = 0;
    edges.clear();
    indptr.clear();
    csr_edges.clear();
    vc_deg.clear();
    vc_indeg.clear();
    vc_outdeg.clear();
  }

  void add(int frm, int to, T cost = 1, int i = -1) {
    assert(!prepared);
    assert(0 <= frm && 0 <= to && to < N);
    if (i == -1) i = M;
    auto e = edge_type({frm, to, cost, i});
    edges.eb(e);
    ++M;
  }

  // wt, off
  void read_tree(bool wt = false, int off = 1) { read_graph(N - 1, wt, off); }

  void read_graph(int M, bool wt = false, int off = 1) {
    for (int m = 0; m < M; ++m) {
      INT(a, b);
      a -= off, b -= off;
      if (!wt) {
        add(a, b);
      } else {
        T c;
        read(c);
        add(a, b, c);
      }
    }
    build();
  }

  void build() {
    assert(!prepared);
    prepared = true;
    indptr.assign(N + 1, 0);
    for (auto&& e: edges) {
      indptr[e.frm + 1]++;
      if (!directed) indptr[e.to + 1]++;
    }
    for (int v = 0; v < N; ++v) { indptr[v + 1] += indptr[v]; }
    auto counter = indptr;
    csr_edges.resize(indptr.back() + 1);
    for (auto&& e: edges) {
      csr_edges[counter[e.frm]++] = e;
      if (!directed)
        csr_edges[counter[e.to]++] = edge_type({e.to, e.frm, e.cost, e.id});
    }
  }

  OutgoingEdges operator[](int v) const {
    assert(prepared);
    return {this, indptr[v], indptr[v + 1]};
  }

  vc<int> deg_array() {
    if (vc_deg.empty()) calc_deg();
    return vc_deg;
  }

  pair<vc<int>, vc<int>> deg_array_inout() {
    if (vc_indeg.empty()) calc_deg_inout();
    return {vc_indeg, vc_outdeg};
  }

  int deg(int v) {
    if (vc_deg.empty()) calc_deg();
    return vc_deg[v];
  }

  int in_deg(int v) {
    if (vc_indeg.empty()) calc_deg_inout();
    return vc_indeg[v];
  }

  int out_deg(int v) {
    if (vc_outdeg.empty()) calc_deg_inout();
    return vc_outdeg[v];
  }

  void debug() {
    print("Graph");
    if (!prepared) {
      print("frm to cost id");
      for (auto&& e: edges) print(e.frm, e.to, e.cost, e.id);
    } else {
      print("indptr", indptr);
      print("frm to cost id");
      FOR(v, N) for (auto&& e: (*this)[v]) print(e.frm, e.to, e.cost, e.id);
    }
  }

  vc<int> new_idx;
  vc<bool> used_e;

  // G における頂点 V[i] が、新しいグラフで i になるようにする
  // {G, es}
  pair<Graph<T, directed>, vc<int>> rearrange(vc<int> V) {
    if (len(new_idx) != N) new_idx.assign(N, -1);
    if (len(used_e) != M) used_e.assign(M, 0);
    int n = len(V);
    FOR(i, n) new_idx[V[i]] = i;
    Graph<T, directed> G(n);
    vc<int> es;
    FOR(i, n) {
      for (auto&& e: (*this)[V[i]]) {
        if (used_e[e.id]) continue;
        int a = e.frm, b = e.to;
        if (new_idx[a] != -1 && new_idx[b] != -1) {
          used_e[e.id] = 1;
          G.add(new_idx[a], new_idx[b], e.cost);
          es.eb(e.id);
        }
      }
    }
    FOR(i, n) new_idx[V[i]] = -1;
    for (auto&& eid: es) used_e[eid] = 0;
    G.build();
    return {G, es};
  }

private:
  void calc_deg() {
    assert(vc_deg.empty());
    vc_deg.resize(N);
    for (auto&& e: edges) vc_deg[e.frm]++, vc_deg[e.to]++;
  }

  void calc_deg_inout() {
    assert(vc_indeg.empty());
    vc_indeg.resize(N);
    vc_outdeg.resize(N);
    for (auto&& e: edges) { vc_indeg[e.to]++, vc_outdeg[e.frm]++; }
  }
};
#line 2 "graph/bipartite_vertex_coloring.hpp"

#line 2 "ds/unionfind/unionfind.hpp"

struct UnionFind {
  int n, n_comp;
  vc<int> dat; // par or (-size)
  UnionFind(int n = 0) { build(n); }

  void build(int m) {
    n = m, n_comp = m;
    dat.assign(n, -1);
  }

  void reset() { build(n); }

  int operator[](int x) {
    while (dat[x] >= 0) {
      int pp = dat[dat[x]];
      if (pp < 0) { return dat[x]; }
      x = dat[x] = pp;
    }
    return x;
  }

  ll size(int x) {
    x = (*this)[x];
    return -dat[x];
  }

  bool merge(int x, int y) {
    x = (*this)[x], y = (*this)[y];
    if (x == y) return false;
    if (-dat[x] < -dat[y]) swap(x, y);
    dat[x] += dat[y], dat[y] = x, n_comp--;
    return true;
  }
};
#line 5 "graph/bipartite_vertex_coloring.hpp"

// 二部グラフでなかった場合には empty

template <typename Graph>
vc<int> bipartite_vertex_coloring(Graph& G) {
  assert(G.is_prepared());

  int n = G.N;
  UnionFind uf(2 * n);
  for (auto&& e: G.edges) {
    int u = e.frm, v = e.to;
    if (e.cost == 0) uf.merge(u, v), uf.merge(u + n, v + n);
    if (e.cost != 0) uf.merge(u + n, v), uf.merge(u, v + n);
  }

  vc<int> color(2 * n, -1);
  FOR(v, n) if (uf[v] == v && color[uf[v]] < 0) {
    color[uf[v]] = 0;
    color[uf[v + n]] = 1;
  }
  FOR(v, n) color[v] = color[uf[v]];
  color.resize(n);
  FOR(v, n) if (uf[v] == uf[v + n]) return {};
  return color;
}
#line 3 "graph/strongly_connected_component.hpp"

template <typename Graph>
pair<int, vc<int>> strongly_connected_component(Graph& G) {
  assert(G.is_directed());
  assert(G.is_prepared());
  int N = G.N;
  int C = 0;
  vc<int> comp(N);
  vc<int> low(N);
  vc<int> ord(N, -1);
  vc<int> visited;
  int now = 0;

  auto dfs = [&](auto self, int v) -> void {
    low[v] = now;
    ord[v] = now;
    ++now;
    visited.eb(v);
    for (auto&& [frm, to, cost, id]: G[v]) {
      if (ord[to] == -1) {
        self(self, to);
        chmin(low[v], low[to]);
      } else {
        chmin(low[v], ord[to]);
      }
    }
    if (low[v] == ord[v]) {
      while (1) {
        int u = visited.back();
        visited.pop_back();
        ord[u] = N;
        comp[u] = C;
        if (u == v) break;
      }
      ++C;
    }
  };
  FOR(v, N) {
    if (ord[v] == -1) dfs(dfs, v);
  }
  FOR(v, N) comp[v] = C - 1 - comp[v];
  return {C, comp};
}

template <typename GT>
Graph<int, 1> scc_dag(GT& G, int C, vc<int>& comp) {
  Graph<int, 1> DAG(C);
  vvc<int> edges(C);
  for (auto&& e: G.edges) {
    int x = comp[e.frm], y = comp[e.to];
    if (x == y) continue;
    edges[x].eb(y);
  }
  FOR(c, C) {
    UNIQUE(edges[c]);
    for (auto&& to: edges[c]) DAG.add(c, to);
  }
  DAG.build();
  return DAG;
}
#line 4 "flow/bipartite.hpp"

template <typename GT>
struct BipartiteMatching {
  int N;
  GT& G;
  vc<int> color;
  vc<int> dist, match;
  vc<int> vis;

  BipartiteMatching(GT& G) : N(G.N), G(G), dist(G.N, -1), match(G.N, -1) {
    if (N == 0) return;
    color = bipartite_vertex_coloring(G);
    assert(!color.empty());
    while (1) {
      bfs();
      vis.assign(N, false);
      int flow = 0;
      FOR(v, N) if (!color[v] && match[v] == -1 && dfs(v))++ flow;
      if (!flow) break;
    }
  }

  BipartiteMatching(GT& G, vc<int> color)
      : N(G.N), G(G), color(color), dist(G.N, -1), match(G.N, -1) {
    while (1) {
      bfs();
      vis.assign(N, false);
      int flow = 0;
      FOR(v, N) if (!color[v] && match[v] == -1 && dfs(v))++ flow;
      if (!flow) break;
    }
  }

  void bfs() {
    dist.assign(N, -1);
    queue<int> que;
    FOR(v, N) if (!color[v] && match[v] == -1) que.emplace(v), dist[v] = 0;
    while (!que.empty()) {
      int v = que.front();
      que.pop();
      for (auto&& e: G[v]) {
        dist[e.to] = 0;
        int w = match[e.to];
        if (w != -1 && dist[w] == -1) dist[w] = dist[v] + 1, que.emplace(w);
      }
    }
  }

  bool dfs(int v) {
    vis[v] = 1;
    for (auto&& e: G[v]) {
      int w = match[e.to];
      if (w == -1 || (!vis[w] && dist[w] == dist[v] + 1 && dfs(w))) {
        match[e.to] = v, match[v] = e.to;
        return true;
      }
    }
    return false;
  }

  vc<pair<int, int>> matching() {
    vc<pair<int, int>> res;
    FOR(v, N) if (v < match[v]) res.eb(v, match[v]);
    return res;
  }

  vc<int> vertex_cover() {
    vc<int> res;
    FOR(v, N) if (color[v] ^ (dist[v] == -1)) { res.eb(v); }
    return res;
  }

  vc<int> independent_set() {
    vc<int> res;
    FOR(v, N) if (!(color[v] ^ (dist[v] == -1))) { res.eb(v); }
    return res;
  }

  vc<int> edge_cover() {
    vc<bool> done(N);
    vc<int> res;
    for (auto&& e: G.edges) {
      if (done[e.frm] || done[e.to]) continue;
      if (match[e.frm] == e.to) {
        res.eb(e.id);
        done[e.frm] = done[e.to] = 1;
      }
    }
    for (auto&& e: G.edges) {
      if (!done[e.frm]) {
        res.eb(e.id);
        done[e.frm] = 1;
      }
      if (!done[e.to]) {
        res.eb(e.id);
        done[e.to] = 1;
      }
    }
    sort(all(res));
    return res;
  }

  /* Dulmage–Mendelsohn decomposition
  https://en.wikipedia.org/wiki/Dulmage%E2%80%93Mendelsohn_decomposition
  http://www.misojiro.t.u-tokyo.ac.jp/~murota/lect-ouyousurigaku/dm050410.pdf
  https://hitonanode.github.io/cplib-cpp/graph/dulmage_mendelsohn_decomposition.hpp.html
  - 最大マッチングとしてありうる iff 同じ W を持つ
  - 辺 uv が必ず使われる：同じ W を持つ辺が唯一
  - color=0 から 1 への辺：W[l] <= W[r]
  - color=0 の点が必ず使われる：W=1,2,...,K
  - color=1 の点が必ず使われる：W=0,1,...,K-1
  */
  pair<int, vc<int>> DM_decomposition() {
    // 非飽和点からの探索

    vc<int> W(N, -1);
    vc<int> que;
    auto add = [&](int v, int x) -> void {
      if (W[v] == -1) {
        W[v] = x;
        que.eb(v);
      }
    };
    FOR(v, N) if (match[v] == -1 && color[v] == 0) add(v, 0);
    FOR(v, N) if (match[v] == -1 && color[v] == 1) add(v, infty<int>);
    while (len(que)) {
      auto v = POP(que);
      if (match[v] != -1) add(match[v], W[v]);
      if (color[v] == 0 && W[v] == 0) {
        for (auto&& e: G[v]) { add(e.to, W[v]); }
      }
      if (color[v] == 1 && W[v] == infty<int>) {
        for (auto&& e: G[v]) { add(e.to, W[v]); }
      }
    }
    // 残った点からなるグラフを作って強連結成分分解

    vc<int> V;
    FOR(v, N) if (W[v] == -1) V.eb(v);
    int n = len(V);
    Graph<bool, 1> DG(n);
    FOR(i, n) {
      int v = V[i];
      if (match[v] != -1) {
        int j = LB(V, match[v]);
        DG.add(i, j);
      }
      if (color[v] == 0) {
        for (auto&& e: G[v]) {
          if (W[e.to] != -1 || e.to == match[v]) continue;
          int j = LB(V, e.to);
          DG.add(i, j);
        }
      }
    }
    DG.build();
    auto [K, comp] = strongly_connected_component(DG);
    K += 1;
    // 答

    FOR(i, n) { W[V[i]] = 1 + comp[i]; }
    FOR(v, N) if (W[v] == infty<int>) W[v] = K;
    return {K, W};
  }

  void debug() {
    print("match", match);
    print("min vertex covor", vertex_cover());
    print("max indep set", independent_set());
    print("min edge cover", edge_cover());
  }
};