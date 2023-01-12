#include <bits/stdc++.h>
#define long long ll;
using namespace std;

vector<int> sl, q;

signed main() {
    int n, x;
    cin >> n;
    string op;
    while(n--) {
        cin >> op;
        if(op == "Push") {
            cin >> x;
            q.push_back(x);
            auto it = lower_bound(sl.begin(), sl.end(), x);
            sl.insert(it, x);
        } else if(op == "Pop") {
            if(!q.size()) cout << "Invalid" << "\n";
            else {
                x = q.back();
                cout << x << "\n";
                q.pop_back();
                auto it = lower_bound(sl.begin(), sl.end(), x);
                sl.erase(it);
            }
        } else {
            x = (q.size() - 1) / 2;
            if(q.size() && x < q.size()) cout << sl[x] << "\n";
            else  cout << "Invalid" << "\n";
        }
    }
}