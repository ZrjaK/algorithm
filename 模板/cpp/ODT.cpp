class ODT {
public:
    struct node {
    int l, r;
    mutable ll val;
    bool operator<(const node &a)const {return l < a.l;}
    node(int L, int R, ll Val) : l(L), r(R), val(Val){}
    node(int L): l(L) {}
    };

    set<node> s;
    using si = set<node>::iterator;
    ODT() { s.insert(node(0, 1e9, 0)); }
    ~ODT() {}

    si split(int pos){
        si it = s.lower_bound(node(pos));
        if(it != s.end() && it->l == pos) return it;
        --it;
        int l = it->l, r = it->r;
        ll val = it->val;
        s.erase(it);
        s.insert(node(l, pos-1, val));
        return s.insert(node(pos, r, val)).first;
    }

    void assign(int l,int r,ll val){
        si itr=split(r+1),itl=split(l);
        s.erase(itl,itr);
        s.insert(node(l,r,val));
    }
};
