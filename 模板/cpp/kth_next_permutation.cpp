#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/tag_and_trait.hpp>
using namespace __gnu_pbds;

// お手軽だけど、座圧＋BITとかの方がかなり速いので注意！
template <typename KEY>
using pbds_set = tree<KEY, null_type, less<KEY>, rb_tree_tag,
                      tree_order_statistics_node_update>;

// P の要素は distinct。
// k 個先がなければ P が empty になる
// いじった項数を返す
// https://codeforces.com/contest/1443/problem/E
template <typename T>
int kth_next_permutation(vc<T>& P, ll k) {
  static vc<int> rk;
  vc<T> Q;
  pbds_set<T> s;
  while (k && len(P)) {
    int n = len(rk) + 1;
    int p = P.back();
    int now = s.order_of_key(p);
    k += now;
    int r = k % n;
    k /= n;
    rk.eb(r);
    Q.eb(P.back());
    s.insert(P.back());
    P.pop_back();
  }

  if (k) return len(rk);
  int res = len(rk);

  while (len(rk)) {
    int r = rk.back();
    rk.pop_back();
    auto it = s.find_by_order(r);
    P.eb((*it));
    s.erase(it);
  }
  return res;
}