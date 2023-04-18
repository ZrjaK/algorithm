struct SuffixDataStructure {
  const std::vector<int> &a;
  std::vector<int> sa;
  std::vector<int> isa;
  std::vector<int> lcp;
  std::vector<int> lg;
  std::vector<std::vector<int>> rmq;
 
  // a[i]>=0
  SuffixDataStructure(const std::vector<int> &a) : a(a) {
    sa = suffix_array(a);
    sa.insert(sa.begin(), a.size());
    build_lcp();
    build_rmq();
  }
 
  int get_lcp(int i, int j) {
    if (i == j) {
      return a.size() - std::max(i, j);
    }
    i = isa[i];
    j = isa[j];
    if (i > j) {
      std::swap(i, j);
    }
    int k = __lg(j - i);
    return std::min(rmq[k][i], rmq[k][j - (1 << k)]);
  }
 
  vector<int> suffix_array(vector<int> a) {
    const int n = a.size();
    if (n == 0) return {};
    const int H = *max_element(begin(a), end(a)) + 1;
    vector<bool> s(n);
    vector<int> next(n), ss;
    for (int i = n - 2; i >= 0; i--) {
      s[i] = a[i] == a[i + 1] ? s[i + 1] : a[i] < a[i + 1];
      if (!s[i] && s[i + 1]) ss.push_back(i + 1);
    }
    reverse(ss.begin(), ss.end());
    for (int i = 0; i < ss.size(); i++) {
      next[ss[i]] = i + 1 < ss.size() ? ss[i + 1] : n;
    }
    auto induced_sort = [&]() {
      vector<int> sa(n, -1), L(H + 1);
      for (int i = 0; i < n; i++) L[a[i] + 1]++;
      for (int i = 0; i < H; i++) L[i + 1] += L[i];
      auto S = L;
      for (int i = (int)ss.size() - 1; i >= 0; i--) {
        int j = ss[i];
        sa[--S[a[j] + 1]] = j;
      }
      S = L;
      sa[L[a[n - 1]]++] = n - 1;
      for (int i = 0; i < n; i++) {
        int j = sa[i] - 1;
        if (j >= 0 && !s[j]) sa[L[a[j]]++] = j;
      }
      for (int i = n - 1; i >= 0; i--) {
        int j = sa[i] - 1;
        if (j >= 0 && s[j]) sa[--S[a[j] + 1]] = j;
      }
      return sa;
    };
    vector<int> rank(n);
    int j = -1;
    for (int i : induced_sort()) {
      if (0 < i && s[i] && !s[i - 1]) {
        if (j != -1) rank[i] = rank[j] + (next[i] - i != next[j] - j || !equal(a.begin() + i, a.begin() + next[i], a.begin() + j));
        j = i;
      }
    }
    vector<int> b;
    for (int i : ss) b.push_back(rank[i]);
    vector<int> tmp(ss);
    ss.clear();
    for (int i : suffix_array(b)) ss.push_back(tmp[i]);
    return induced_sort();
  }
 
  void build_lcp() {
    const int n = a.size();
    isa.resize(n + 1);
    lcp.assign(n + 1, 0);
    for (int i = 0; i <= n; i++) {
      isa[sa[i]] = i;
    }
    int k = 0;
    for (int i = 0; i < n; i++) {
      int j = sa[isa[i] - 1];
      k = std::max(0, k - 1);
      while (i + k < n && j + k < n && a[i + k] == a[j + k]) {
        k++;
      }
      lcp[isa[i] - 1] = k;
    }
  }
 
  void build_rmq() {
    const int n = lcp.size();
    lg.resize(n + 1);
    for (int i = 2; i <= n; i++) {
      lg[i] = lg[i / 2] + 1;
    }
    const int m = lg[n];
    rmq.assign(m + 1, std::vector<int>(n));
    for (int i = 0; i < n; i++) {
      rmq[0][i] = lcp[i];
    }
    for (int i = 0; i < m; i++) {
      for (int j = 0; j + (1 << i) < n; j++) {
        rmq[i + 1][j] = std::min(rmq[i][j], rmq[i][j + (1 << i)]);
      }
    }
  }
};
 