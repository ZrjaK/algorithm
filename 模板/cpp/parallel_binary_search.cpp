/*
並列二分探索。(Q, ok, ng, init, upd, check)。
check が成り立つぎりぎりの upd回数を返す。
・void upd(t)：t 回目の update
・bool check(q)：クエリ q の判定
*/
template <typename F1, typename F2, typename F3>
vc<int> parallel_binary_search(int Q, int ok, int ng, F1 init, F2 upd,
                               F3 check) {
  int T = max(ok, ng);
  vc<int> OK(Q, ok), NG(Q, ng);
  int flag = 1;
  while (flag) {
    flag = 0;
    init();
    vc<vc<int>> C(T);
    FOR(q, Q) if (abs(OK[q] - NG[q]) > 1) {
      C[(OK[q] + NG[q]) / 2].eb(q);
    }
    FOR(t, T) {
      flag |= !C[t].empty();
      upd(t);
      for (auto&& q : C[t]) {
        if (check(q)) OK[q] = t;
        else NG[q] = t;
      }
    }
  }
  return OK;
}