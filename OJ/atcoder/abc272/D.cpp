#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int>PII;
priority_queue<PII,vector<PII>,greater<PII>> q;
int f[200010];
int main()
{
    int n, m;
    cin>>n>>m;
    vector<PII> h;
    for(int i = 0; i <= (int)sqrt(m); i++){
        float t = sqrt(m-i*i);
        if ((int)t == t) {
            h.push_back({i, (int)t});
            h.push_back({-i, -(int)t});
            h.push_back({-i, (int)t});
            h.push_back({i, -(int)t});
        }
    }
    memset(f,0x3f3f3f3f,sizeof(f));
    f[0]=0;
    q.push({0,0});
    while(!q.empty())
    {
        PII k=q.top();
        q.pop();
        int x = k.second / 400;
        int y = k.second % 400;
        int s = k.first;
        for(int i = 0; i < h.size(); i++) {
            int nx = x + h[i].first;
            int ny = y + h[i].second;
            if (nx>=0 && nx < n && ny>=0 && ny<n && s+1 < f[nx*400+ny]) {
                f[nx*400+ny] = s + 1;
                q.push({s+1, nx*400+ny});
            }
        }
    }
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if (f[i*400+j] == 0x3f3f3f3f) {
                cout << -1 << " ";
            } else {
                cout << f[i*400+j] << " ";
            }
        }
        cout << endl;
    }
    return 0;
}