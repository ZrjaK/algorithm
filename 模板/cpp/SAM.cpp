template <int sigma = 26>
struct Suffix_Automaton {
  struct Node {
    array<int, sigma> next; // automaton の遷移先
    int link;               // suffix link
    int size;               // node が受理する最長文字列の長さ
    Node(int link, int size) : link(link), size(size) { fill(next.begin(), next.end(), -1); }
  };

  vector<Node> nodes;
  int last; // 文字列全体を入れたときの行き先

  Suffix_Automaton() {
    nodes.emplace_back(Node(-1, 0));
    last = 0;
  }

  void add(int c0, int off = 'a') {
    int c = c0 - off;
    if (nodes[last].next[c] != -1) { // general-sam
        int p = last, q = nodes[p].next[c];
        if (nodes[p].size + 1 == nodes[q].size) return last = q, void();
        int new_node = nodes.size();
        nodes.emplace_back(Node(-1, nodes[p].size + 1));
        nodes.back().next = nodes[q].next;
        while (p != -1 && nodes[p].next[c] == q) {
            nodes[p].next[c] = new_node;
            p = nodes[p].link;
        }
        nodes[new_node].link = nodes[q].link;
        nodes[q].link = new_node;
        last = new_node;
        return;
    }
    int new_node = nodes.size();
    nodes.emplace_back(Node(-1, nodes[last].size + 1));
    int p = last;
    while (p != -1 && nodes[p].next[c] == -1) {
      nodes[p].next[c] = new_node;
      p = nodes[p].link;
    }
    int q = (p == -1 ? 0 : nodes[p].next[c]);
    if (p == -1 || nodes[p].size + 1 == nodes[q].size) {
      nodes[new_node].link = q;
    } else {
      int new_q = nodes.size();
      nodes.emplace_back(Node(nodes[q].link, nodes[p].size + 1));
      nodes.back().next = nodes[q].next;
      nodes[q].link = new_q;
      nodes[new_node].link = new_q;
      while (p != -1 && nodes[p].next[c] == q) {
        nodes[p].next[c] = new_q;
        p = nodes[p].link;
      }
    }
    last = new_node;
  }

  vector<vector<int>> calc_DAG() {
    int n = nodes.size();
    vector<vector<int>> G(n);
    for (int v = 0; v < n; v++) {
      for (auto&& to: nodes[v].next)
        if (to != -1) { G[v].emplace_back(to); }
    }
    return G;
  }

  vector<vector<int>> calc_tree() {
    int n = nodes.size();
    vector<vector<int>> G(n);
    for (int v = 1; v < n; v++) {
      int p = nodes[v].link;
      G[p].emplace_back(v);
    }
    return G;
  }

  int count_substring_at(int p) {
    // あるノードについて、最短と最長の文字列長が分かればよい。
    // 最長は size が持っている
    // 最短は、suffix link 先の最長に 1 を加えたものである。
    if (p == 0) return 0;
    return nodes[p].size - nodes[nodes[p].link].size;
  }

  long long count_substring() {
    long long ANS = 0;
    for (int i = 0; i < nodes.size(); i++) ANS += count_substring_at(i);
    return ANS;
  }
};
