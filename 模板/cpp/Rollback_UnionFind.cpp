template <typename T>
struct Rollback_Array {
  int N;
  vector<T> dat;
  vector<pair<int, T>> history;
 
  Rollback_Array(vector<T> x) : N(x.size()), dat(x) {}
  Rollback_Array(int N) : N(N), dat(N) {}
  template <typename F>
  Rollback_Array(int N, F f) : N(N) {
    dat.reserve(N);
    for (int i = 0; i < N; i++) dat.emplace_back(f(i));
  }
 
  int time() { return history.size(); }
  void rollback(int t) {
    for(int i = time() - 1; i >= t; i--) {
      auto& [idx, v] = history[i];
      dat[idx] = v;
    }
    history.resize(t);
  }
  T get(int idx) { return dat[idx]; }
  void set(int idx, T x) {
    history.emplace_back(idx, dat[idx]);
    dat[idx] = x;
  }
 
  vector<T> get_all() {
    vector<T> res(N);
    for (int i = 0; i < N; i++) res[i] = get(i);
    return res;
  }
};
 
struct Rollback_UnionFind {
  Rollback_Array<int> dat; // parent or size
 
  Rollback_UnionFind(int n) : dat(vector<int>(n, -1)) {}
 
  int operator[](int v) {
    while (dat.get(v) >= 0) v = dat.get(v);
    return v;
  }
 
  int size(int v) { return -dat.get((*this)[v]); }
  int time() { return dat.time(); }
  void rollback(int t) { dat.rollback(t); }
 
  bool merge(int a, int b) {
    a = (*this)[a], b = (*this)[b];
    if (a == b) return false;
    if (dat.get(a) > dat.get(b)) swap(a, b);
    dat.set(a, dat.get(a) + dat.get(b));
    dat.set(b, a);
    return true;
  }
};