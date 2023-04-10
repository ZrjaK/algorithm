template <typename T = int, bool directed = false>
struct Graph {
    int n;
    using cost_type = T;
    using edge_type = tuple<int, int, cost_type, int>;
    vector<vector<pair<int, cost_type>>> g;

    vector<edge_type> edges;
    constexpr bool is_directed() { return directed; }

    Graph(int _n) : n(_n), g(_n) {}

    void add(int u, int v, cost_type cost, int i = -1) {
        assert(0 <= u && u < n && 0 <= v && v < n);
        edges.emplace_back(u, v, cost, i);
    }

    void read_tree() { read_graph(n - 1); }

    void read_graph(int m) {
        for (int i = 0; i < m; i++) {
            int a, b; cin >> a >> b;
            a--, b--;
            T cost; cin >> cost;
            add(a, b, cost, i);
        }
        build();
    }
    
    void build() {
        for (auto&& [u, v, cost, i] : edges) {
            g[u].emplace_back(v, cost);
            if (!directed) g[v].emplace_back(u, cost);
        }
    }

    vector<pair<int, cost_type>> operator[] (int i) {
        return g[i];
    }
};