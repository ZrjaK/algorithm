/*
・時刻 t に x を追加する
・時刻 t に x を削除する
があるときに、
・時刻 [l, r) に x を追加する
に変換する。
クエリが時系列順に来ることが分かっているときは monotone = true の方が高速。
*/
template <typename X, bool monotone>
struct Add_Remove_Query {
  map<X, int> MP;
  vector<tuple<int, int, X>> dat;
  map<X, vector<int>> ADD;
  map<X, vector<int>> RM;

  void add(int time, X x) {
    if (monotone) return add_monotone(time, x);
    ADD[x].emplace_back(time);
  }
  void remove(int time, X x) {
    if (monotone) return remove_monotone(time, x);
    RM[x].emplace_back(time);
  }

  // すべてのクエリが終わった現在時刻を渡す
  vector<tuple<int, int, X>> calc(int time) {
    if (monotone) return calc_monotone(time);
    vector<tuple<int, int, X>> dat;
    for (auto&& [x, A]: ADD) {
      vector<int> B;
      if (RM.count(x)) {
        B = RM[x];
        RM.erase(x);
      }
      while (B.size() < A.size()) B.eb(time);
      assert(A.size() == B.size());

      sort(A.begin(), A.end());
      sort(B.begin(), B.end());
      for (int i = 0; i < A.size(); i++) {
        assert(A[i] <= B[i]);
        if (A[i] < B[i]) dat.emplace_back(A[i], B[i], x);
      }
    }
    assert(RM.size() == 0);
    return dat;
  }

private:
  void add_monotone(int time, X x) {
    assert(!MP.count(x));
    MP[x] = time;
  }
  void remove_monotone(int time, X x) {
    auto it = MP.find(x);
    assert(it != MP.end());
    int t = (*it).second;
    MP.erase(it);
    if (t == time) return;
    dat.emplace_back(t, time, x);
  }
  vector<tuple<int, int, X>> calc_monotone(int time) {
    for (auto&& [x, t]: MP) {
      if (t == time) continue;
      dat.emplace_back(t, time, x);
    }
    return dat;
  }
};
    
    // Add_Remove_Query<pii, false> X;
    //
    // // add and remove
    //
    // auto upd = X.calc(Q);
    // vector<int> I(len(upd));
    // iota(all(I), 0);

    // auto dfs = [&] (auto& dfs, vector<int>& upd_query_I, int begin, int end) -> void {
    //     if (begin == end) return;
    //     // snapshot
    //
    //
    //
    //     vector<int> IL, IR;
    //     int mid = (begin + end) / 2;
    //     for (auto&& i: upd_query_I) {
    //         auto [a, b, XX] = upd[i];
    //         // get data in XX
    //
    //
    //         if (a <= begin && end <= b) {
    //             // X で表される update query を処理する
    //             
    //             
    //             
    //         } else {
    //             if (a < mid) IL.eb(i);
    //             if (mid < b) IR.eb(i);
    //         }
    //     }
    //     if (begin + 1 == end) {
    //         // 求値クエリ
    //         int qid = begin;
    //
    //
    //
    //         // ここで出力してしまってもよい
    //     } else {
    //         dfs(dfs, IL, begin, mid);
    //         dfs(dfs, IR, mid, end);
    //     }
    //     // rollback
    //     
    //     
    //     
    // };
    // dfs(dfs, I, 0, Q);