struct SegTree_for_graph {
    vector<vector<pair<int, int>>> G;
    int rt1,rt2,tot;
    int maxn;
    vector<int> ls, rs;
    vector<int> in, out;

    SegTree_for_graph(int n) {
        rt1 = rt2 = tot = 0;
        maxn = n;
        ls = vector<int>(maxn * 30);
        rs = vector<int>(maxn * 30);
        in = vector<int>(maxn * 30);
        out = vector<int>(maxn * 30);
        G = vector<vector<pair<int, int>>>(maxn * 30);
        build_in(rt1, 1, maxn);
        build_out(rt2, 1, maxn);
        for (int i = 1; i <= n; i++) {
            _add(in[i], out[i], 0);
            _add(out[i], in[i], 0);
        }
    }

    void add(int u,int v,int val){
        _add(in[u], out[v], val);
    }

    void _add(int u,int v,int val){
        G[u].emplace_back(pair<int, int>{v, val});
    }

    #define ls ls[rt]
    #define rs rs[rt]   

    void build_in(int &rt,int l,int r){
        rt=++tot;
        if(l==r){
            in[l]=rt;
            return;
        }

        int mid=(l+r)>>1;
        build_in(ls,l,mid);
        build_in(rs,mid+1,r);
 
        _add(ls,rt,0);_add(rs,rt,0);
    }

    void build_out(int &rt,int l,int r){
        rt=++tot;
        if(l==r){
            out[l]=rt;
            return;
        }

        int mid=(l+r)>>1;
        build_out(ls,l,mid);
        build_out(rs,mid+1,r);
 
        _add(rt,ls,0);_add(rt,rs,0);
    }

    // 区间到点
    // st.modify_in(l, r, v, w);
    void modify_in(int ql, int qr, int pos, int val) {
        _modify_in(rt1, 1, maxn, ql, qr, out[pos], val);
    }

    void _modify_in(int rt,int l,int r,int ql,int qr,int pos,int val){
        if(ql>r||qr<l)return;
        if(ql<=l&&qr>=r){
            _add(rt,pos,val);
            return;
        }
        int mid=(l+r)>>1;
        _modify_in(ls,l,mid,ql,qr,pos,val);
        _modify_in(rs,mid+1,r,ql,qr,pos,val);
    }


    // 点到区间
    // st.modify_out(l, r, u, w);
    void modify_out(int ql, int qr, int pos, int val) {
        _modify_out(rt2, 1, maxn, ql, qr, in[pos], val);
    }
    void _modify_out(int rt,int l,int r,int ql,int qr,int pos,int val){
        if(ql>r||qr<l)return;
        if(ql<=l&&qr>=r){
            _add(pos,rt,val);
            return;
        }
        int mid=(l+r)>>1;
        _modify_out(ls,l,mid,ql,qr,pos,val);
        _modify_out(rs,mid+1,r,ql,qr,pos,val);
    }
};
