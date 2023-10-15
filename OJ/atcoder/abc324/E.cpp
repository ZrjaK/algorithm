#include<bits/stdc++.h>

using namespace std;

template <typename T>
struct Fenwick {
    int n;
    std::vector<T> a;
    
    Fenwick(int n = 0) {
        init(n);
    }
    
    void init(int n) {
        this->n = n;
        a.assign(n, T());
    }
    
    void add(int x, T v) {
        for (int i = x + 1; i <= n; i += i & -i) {
            a[i - 1] += v;
        }
    }
    
    T sum(int x) {
        auto ans = T();
        for (int i = x; i > 0; i -= i & -i) {
            ans += a[i - 1];
        }
        return ans;
    }
    
    T rangeSum(int l, int r) {
        return sum(r) - sum(l);
    }
    
    int kth(T k) {
        int x = 0;
        for (int i = 1 << std::__lg(n); i; i /= 2) {
            if (x + i <= n && k >= a[x + i - 1]) {
                x += i;
                k -= a[x - 1];
            }
        }
        return x;
    }
};

void solve () {
    int n;
    string T;
    cin >> n >> T;
    vector<int> a;
    Fenwick<int> X(T.size() + 10);
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        int p = 0;
        for (auto& x : s) {
            if (p < T.size() && T[p] == x) p++;
        }
        a.push_back(p);
        reverse(s.begin(), s.end());
        p = 0;
        for (auto& x : s) {
            if (p < T.size() && end(T)[~p] == x) p++;
        }
        X.add(p, 1);
    }
    long long ans = 0;
    for (auto& i : a) {
        ans += X.rangeSum(T.size() - i, T.size() + 10);
    }
    cout << ans;




}

signed main () {
    solve();
    return 0;
}