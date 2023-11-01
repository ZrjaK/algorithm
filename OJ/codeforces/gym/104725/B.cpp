#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

using namespace std;

using ll = long long;


void solve() {
    ll d;
    cin >> d;
    if (d == 0) exit(0);
    ll x = 0, y = 0;
    ll X = 0, Y = 0;
    ll SX = 343, SY = 45;
#ifndef ONLINE_JUDGE
    d = (X - SX) * (X - SX) + (Y - SY) * (Y - SY);
#endif
    int c = 0;
    auto ask = [&] (ll dx, ll dy) -> ll {
        c++;
        // assert(c <= 30);
        assert(-2000 <= x + dx && x + dx <= 2000 && -2000 <= y + dy && y + dy <= 2000);
        cout << x + dx << " " << y + dy << "\n";
        X += x + dx, Y += y + dy;
        x = -dx, y = -dy;
        cout.flush();
#ifndef ONLINE_JUDGE
    return (X - SX) * (X - SX) + (Y - SY) * (Y - SY);
#endif
        ll res;
        cin >> res;
        if (res == 0) exit(0);
        return res;
    };
    {
        ll d1 = ask(-1, 0), d2 = ask(1, 0);
        if (d > d1 || d > d2) {
            if (d1 < d2) {
                int l = 0, r = 2001;
                while (l + 1 < r) {
                    int mid = (l + r) / 2;
                    if (ask(-mid, 0) >= d) r = mid;
                    else l = mid;
                }
                d = ask(-abs((X + r + X) / 2 - X), 0);
            } else {
                int l = 0, r = 2001;
                while (l + 1 < r) {
                    int mid = (l + r) / 2;
                    if (ask(mid, 0) >= d) r = mid;
                    else l = mid;
                }
                d = ask(abs((X + r + X) / 2 - X), 0);
            }
        } else {
            x = 0;
            ask(-1, 0);
        }
    }
    x = 0;
    {
        ll d1 = ask(0, -1), d2 = ask(0, 1);
        if (d > d1 || d > d2) {
            if (d1 < d2) {
                int l = 0, r = 2001;
                while (l + 1 < r) {
                    int mid = (l + r) / 2;
                    if (ask(0, -mid) >= d) r = mid;
                    else l = mid;
                }
                d = ask(0, -abs((Y + r + Y) / 2 - Y));
            } else {
                int l = 0, r = 2001;
                while (l + 1 < r) {
                    int mid = (l + r) / 2;
                    if (ask(0, mid) >= d) r = mid;
                    else l = mid;
                }
                d = ask(0, abs((Y + r + Y) / 2 - Y));
            }
        } else {
            y = 0;
            ask(0, -1);
        }
    }
#ifndef ONLINE_JUDGE
    cout << X << "-----------" << Y;
    assert(X == SX && Y == SY);
#endif
    
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int T = 1;
    // cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}