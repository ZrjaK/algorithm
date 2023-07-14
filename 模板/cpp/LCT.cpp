
template <typename Node, int NODES>
struct LinkCutTree_base {
  int n;
  Node *nodes;

  LinkCutTree_base(int n = 0) : n(n) {
    nodes = new Node[NODES];
    for(int i = 0; i < n; i++) nodes[i] = Node(i);
  }

  Node *operator[](int v) { return &nodes[v]; }

  // パスを表す splay tree の根になっているかどうか
  bool is_root(Node *c) { return state(c) == 0; }
  bool is_root(int c) { return state(&nodes[c]) == 0; }

  Node *get_root(Node *c) {
    expose(c);
    while (c->l) {
      c->push();
      c = c->l;
    }
    splay(c);
    return c;
  }

  int get_root(int c) { return get_root(&nodes[c])->idx; }

  // c の親を p にする。内部で evert するのでいつ呼んでも大丈夫。
  virtual void link(Node *c, Node *p) {
    evert(c);
    expose(p);
    c->p = p;
    p->r = c;
    p->update();
  }

  // c の親を p にする。内部で evert するのでいつ呼んでも大丈夫。
  virtual void link(int c, int p) { return link(&nodes[c], &nodes[p]); }

  void cut(Node *a, Node *b) {
    evert(a);
    expose(b);
    assert(!b->p);
    assert((b->l) == a);
    b->l->p = nullptr;
    b->l = nullptr;
    b->update();
  }

  void cut(int a, int b) { return cut(&nodes[a], &nodes[b]); }

  void evert(Node *c) {
    expose(c);
    c->reverse();
    c->push();
  }

  void evert(int c) { evert(&nodes[c]); }

  Node *lca(Node *u, Node *v) {
    assert(get_root(u) == get_root(v));
    expose(u);
    return expose(v);
  }

  int lca(int u, int v) { return lca(&nodes[u], &nodes[v])->idx; }

  // c と根までが繋がれている状態に変更して、根を return する
  virtual Node *expose(Node *c) {
    Node *now = c;
    Node *rp = nullptr; // 今まで作ったパス
    while (now) {
      splay(now);
      now->r = rp; // 子方向の変更
      now->update();
      rp = now;
      now = now->p;
    }
    splay(c);
    return rp;
  }

  int expose(int c) {
    Node *x = expose(&nodes[c]);
    if (!x) return -1;
    return x->idx;
  }

  Node *get_parent(Node *x) {
    expose(x);
    if (!x->l) return nullptr;
    x = x->l;
    while (x->r) x = x->r;
    return x;
  }

  int get_parent(int x) {
    Node *p = get_parent((*this)[x]);
    return (p ? p->idx : -1);
  }

  void debug() {
    for(int i = 0; i < n; i++) { nodes[i].debug(); }
  }

  virtual void rotate(Node *n) {
    // n を根に近づける
    Node *pp, *p, *c;
    p = n->p;
    pp = p->p;

    if (p->l == n) {
      c = n->r;
      n->r = p;
      p->l = c;
    } else {
      c = n->l;
      n->l = p;
      p->r = c;
    }

    if (pp && pp->l == p) pp->l = n;
    if (pp && pp->r == p) pp->r = n;
    n->p = pp;
    p->p = n;
    if (c) c->p = p;
  }

  inline int state(Node *n) {
    if (!n->p) return 0;
    if (n->p->l == n) return 1;
    if (n->p->r == n) return -1;
    return 0;
  }

  void splay(Node *c) {
    c->push();
    while (!is_root(c)) {
      Node *p = c->p;
      Node *pp = (p ? p->p : nullptr);
      if (state(p) == 0) {
        p->push(), c->push();
        rotate(c);
        if (p) p->update();
      }
      else if (state(c) == state(p)) {
        pp->push(), p->push(), c->push();
        rotate(p);
        rotate(c);
        if (pp) pp->update();
        if (p) p->update();
      }
      else {
        pp->push(), p->push(), c->push();
        rotate(c);
        rotate(c);
        if (p) p->update();
        if (pp) pp->update();
      }
    }
    c->update();
  }
};

struct LCT_Node_base {
  LCT_Node_base *l, *r, *p;
  int idx;
  bool rev;
  LCT_Node_base(int i = 0) : l(nullptr), r(nullptr), p(nullptr), idx(i) {}

  void update() {}

  void push() {
    if (rev) {
      if (l) l->reverse();
      if (r) r->reverse();
      rev = 0;
    }
  }

  void reverse() {
    rev ^= 1;
    swap(l, r);
  }
};

template <int NODES>
using LinkCutTree = LinkCutTree_base<LCT_Node_base, NODES>;
#line 2 "graph/ds/link_cut_path.hpp"

template <typename Node, int NODES>
struct LinkCutTree_Path_base : public LinkCutTree_base<Node, NODES> {
  using X = typename Node::X;

  LinkCutTree_Path_base(int n) : LinkCutTree_base<Node, NODES>(n) {}

  LinkCutTree_Path_base(vector<X> dat) : LinkCutTree_base<Node, NODES>(dat.size()) {
    for(int v = 0; v < dat.size(); v++) {
      Node *c = (*this)[v];
      set(c, dat[v]);
    }
  }

  template <typename F>
  LinkCutTree_Path_base(int n, F f) : LinkCutTree_base<Node, NODES>(n) {
    for(int v = 0; v < n; v++) {
      X x = f(v);
      Node *c = (*this)[v];
      set(c, x);
    }
  }

  void set(Node *c, X x) {
    this->evert(c);
    c->x = x;
    c->update();
  }

  void set(int c, X x) { set((*this)[c], x); }

  void multiply(Node *c, X x) { set(c, Node::Mono::op(c->x, x)); }

  void multiply(int c, X x) { multiply((*this)[c], x); }

  X prod_path(Node *a, Node *b) {
    this->evert(a);
    this->expose(b);
    return b->prod;
  }

  X prod_path(int a, int b) { return prod_path((*this)[a], (*this)[b]); }
};

template <typename Monoid>
struct LCT_Node_Monoid {
  using Mono = Monoid;
  using X = typename Monoid::value_type;
  LCT_Node_Monoid *l, *r, *p;
  int idx;
  X x, prod, rev_prod;
  bool rev;
  LCT_Node_Monoid(int i = 0)
      : l(nullptr),
        r(nullptr),
        p(nullptr),
        idx(i),
        x(Monoid::unit()),
        prod(Monoid::unit()),
        rev_prod(Monoid::unit()) {}

  void update() {
    prod = rev_prod = x;
    if (l) {
      prod = Monoid::op(l->prod, prod);
      rev_prod = Monoid::op(rev_prod, l->rev_prod);
    }
    if (r) {
      prod = Monoid::op(prod, r->prod);
      rev_prod = Monoid::op(r->rev_prod, rev_prod);
    }
  }

  void push() {
    if (rev) {
      if (l) l->reverse();
      if (r) r->reverse();
      rev = 0;
    }
  }

  void reverse() {
    rev ^= 1;
    swap(l, r);
    swap(prod, rev_prod);
  }

  void debug() {
    int li = (l ? l->idx : -1);
    int ri = (r ? r->idx : -1);
    int pi = (p ? p->idx : -1);
    print("idx", idx, "l", li, "r", ri, "p", pi, "x", x, "prod", prod,
          "rev_prod", rev_prod);
  }
};

template <typename Monoid>
struct LCT_Node_CommutativeMonoid {
  using Mono = Monoid;
  using X = typename Mono::value_type;
  LCT_Node_CommutativeMonoid *l, *r, *p;
  int idx;
  X x, prod;
  bool rev;
  LCT_Node_CommutativeMonoid(int i = 0)
      : l(nullptr),
        r(nullptr),
        p(nullptr),
        idx(i),
        x(Mono::unit()),
        prod(Mono::unit()) {}

  void update() {
    prod = x;
    if (l) { prod = Mono::op(l->prod, prod); }
    if (r) { prod = Mono::op(prod, r->prod); }
  }

  void push() {
    if (rev) {
      if (l) l->reverse();
      if (r) r->reverse();
      rev = 0;
    }
  }

  void reverse() {
    rev ^= 1;
    swap(l, r);
  }

  void debug() {
    int li = (l ? l->idx : -1);
    int ri = (r ? r->idx : -1);
    int pi = (p ? p->idx : -1);
    print("idx", idx, "l", li, "r", ri, "p", pi, "x", x, "prod", prod);
  }
};

template <typename Monoid, int NODES>
using LinkCutTree_Path = LinkCutTree_Path_base<LCT_Node_Monoid<Monoid>, NODES>;

template <typename Monoid, int NODES>
using LinkCutTree_Path_Commutative
    = LinkCutTree_Path_base<LCT_Node_CommutativeMonoid<Monoid>, NODES>;

template <typename X>
struct Monoid_Add {
  using value_type = X;
  static constexpr X op(const X &x, const X &y) noexcept { return x + y; }
  static constexpr X inverse(const X &x) noexcept { return -x; }
  static constexpr X power(const X &x, ll n) noexcept { return X(n) * x; }
  static constexpr X unit() { return X(0); }
  static constexpr bool commute = true;
};