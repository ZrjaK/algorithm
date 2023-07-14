struct binary_tree {
    struct Node {
        int count;
        int son[2];
        Node(): count(0) {son[0] = son[1] = -1;}
    };
 
    binary_tree(int _limit = 30): root(0), next(1), limit(_limit - 1), pool(10) {}
     
    void clear() {
        vector<Node>().swap(pool);
    }
     
    int getid() {
        if (next == pool.size()) pool.resize(pool.size() * 2, Node());
        return next++;
    }
     
    void add(long long x) {
        int cur = root;
        for(int i = limit; i >= 0; i--) {
            int d = x >> i & 1;
            if (pool[cur].son[d] == -1) {
                int p = getid();
                pool[cur].son[d] = p;
            }
                 
            cur = pool[cur].son[d];
            pool[cur].count++;
        }
    }

    void del(long long x) {
        int cur = root;
        for(int i = limit; i >= 0; i--) {
            int d = x >> i & 1;
            cur = pool[cur].son[d];
            pool[cur].count--;
        }
    }
     
    long long max_xor(long long x) {
        int cur = root, ans = 0;
        for(int i = limit; i >= 0; i--) {
            if (cur == -1) break;
            int d = x >> i & 1;
            int nxt = pool[cur].son[!d];
            if (nxt != -1 && pool[nxt].count) {
                ans |= 1 << i;
                cur = pool[cur].son[!d];
            } else {
                cur = pool[cur].son[d];
            }
        }
        return ans;
    }
     
    int root, next, limit;
    vector<Node> pool;
};
