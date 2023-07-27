// stable sort
template <typename T>
vector<int> argsort(const vector<T> &A) {
  vector<int> ids(len(A));
  iota(ids.begin(), ids.end(), 0);
  sort(ids.begin(), ids.end(),
       [&](int i, int j) { return (A[i] == A[j] ? i < j : A[i] < A[j]); });
  return ids;
}

struct Mo_3d {
  vector<tuple<int, int, int>> query;

  void add_query(int t, int l, int r) { query.emplace_back(t, l, r); }

  vector<int> get_mo_order(long long block_sz) {
    constexpr long long K = 1 << 20;
    int Q = query.size();
    vector<int> key(Q);
    for(int q = 0; q < Q; q++) {
      auto [t, l, r] = query[q];
      t /= block_sz;
      l /= block_sz;
      long long x = r;
      if (l & 1) x = -x;
      x += l * K;
      if (t & 1) x = -x;
      x += t * K * K;
      key[q] = x;
    }
    vector<int> I = argsort(key);

    // ランダムケースで5パーセント程度

    auto cost = [&](int a, int b) -> int {
      auto [t1, x1, y1] = query[I[a]];
      auto [t2, x2, y2] = query[I[b]];
      return abs(t1 - t2) + abs(x1 - x2) + abs(y1 - y2);
    };
    for(int k = 0; k < Q - 5; k++) {
      if (cost(k, k + 2) + cost(k + 1, k + 3)
          < cost(k, k + 1) + cost(k + 2, k + 3)) {
        swap(I[k + 1], I[k + 2]);
      }
      if (cost(k, k + 3) + cost(k + 1, k + 4)
          < cost(k, k + 1) + cost(k + 3, k + 4)) {
        swap(I[k + 1], I[k + 3]);
      }
    }
    return I;
  }

  template <typename F1, typename F2, typename F3, typename F4, typename F5,
            typename F6, typename F7>
  void calc(F1 ADD_L, F2 ADD_R, F3 RM_L, F4 RM_R, F5 ADD_CHANGE, F6 RM_CHANGE,
            F7 CALC, long long block_sz = -1) {
    if (block_sz == -1) {
      long long Q = max(1ll, len(query));
      while (block_sz * block_sz * block_sz < Q * Q) { block_sz++; }
    }
    auto I = get_mo_order(block_sz);
    long long t = 0, l = 0, r = 0;
    for (auto&& qid: I) {
      auto [nt, nl, nr] = query[qid];
      while (l > nl) ADD_L(--l);
      while (r < nr) ADD_R(r++);
      while (l < nl) RM_L(l++);
      while (r > nr) RM_R(--r);
      while (t < nt) ADD_CHANGE(t++, l, r);
      while (t > nt) RM_CHANGE(--t, l, r);
      CALC(qid);
    }
  }
};