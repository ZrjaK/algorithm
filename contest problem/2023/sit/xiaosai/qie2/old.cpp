// 连续子序列打包 总price最小 只过了72%
#include <bits/stdc++.h>
using namespace std;
#define int long long
const int N = 1e4+10;

int n,m,s;
int a[N];
int dp[N];


int tot = 0;
int price(int l,int r){
	int u=0,v=1e9;
	for(int i=l;i<=r;i++){
		u=max(u,a[i]);
		v=min(v,a[i]);
		tot++;
	}
	return (r-l+1)*floor((u+v)/2)+s;
}

signed main()
{
	cin>>n>>m>>s;
	for(int i=1;i<=n;i++) cin >> a[i];
	
	
	memset(dp,0x3f,sizeof dp);
	dp[0]=0;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=i&&j<=m;j++){
			dp[i]=min(dp[i],dp[i-j]+price(i-j+1,i));
		}
	}
	cout<<dp[n] << "\n";
	cout << tot;
	
    return 0;
}

/*
一段序列 分割 每段<=m  参数s
n个数 m 

一些东西打包 包的容量是m 一整段
length * ((max + min) / 2) + s

1E4  感觉O(n) 这里O(n ^ 2)

样例：
6 4 3
1 4 5 1 4 1
输出：
21

*/