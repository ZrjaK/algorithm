template <class T, class S>
inline bool chmax(T &a, const S &b) {
  return (a < b ? a = b, 1 : 0);
}
struct Mo {
  vector<pair<int, int>> LR;
  void add(int L, int R) { LR.emplace_back(L, R); }
 
  vector<int> get_mo_order() {
    int N = 1;
    for (auto &&[l, r]: LR) chmax(N, l), chmax(N, r);
    int Q = len(LR);
    int bs = N / min<int>(N, sqrt(Q));
    vector<int> I(Q);
    iota(all(I), 0);
    sort(all(I), [&](int a, int b) {
      int aa = LR[a].fi / bs, bb = LR[b].fi / bs;
      if (aa != bb) return aa < bb;
      return (aa & 1) ? LR[a].se > LR[b].se : LR[a].se < LR[b].se;
    });
 
    auto cost = [&](int a, int b) -> int {
      return abs(LR[I[a]].fi - LR[I[b]].fi) + abs(LR[I[a]].se - LR[I[b]].se);
    };
 
    // ランダムケースで数パーセント
    for (int k = 0; k < Q - 5; k++) {
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
 
  template <typename F1, typename F2, typename F3, typename F4, typename F5>
  void calc(F1 add_l, F2 add_r, F3 rm_l, F4 rm_r, F5 query) {
    auto I = get_mo_order();
    int l = 0, r = 0;
    for (auto idx: I) {
      while (l > LR[idx].fi) add_l(--l);
      while (r < LR[idx].se) add_r(r++);
      while (l < LR[idx].fi) rm_l(l++);
      while (r > LR[idx].se) rm_r(--r);
      query(idx);
    }
  }
};