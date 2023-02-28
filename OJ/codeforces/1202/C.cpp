#include<bits/stdc++.h>
using namespace std;
string s;
int main(){
	int t;
	cin>>t;
    while(t--){
		cin>>s;
		int ma=0,md=0,mw=0,ms=0,cw=0,cd=0,sa=0,sd=0,sw=0,ss=0;
		for(int i=0;s[i];++i){
			if(s[i]=='W')++cw;
			if(s[i]=='S')--cw;
			if(s[i]=='D')++cd;
			if(s[i]=='A')--cd;
			mw=max(mw,cw);
			ms=min(ms,cw);
			md=max(md,cd);
			ma=min(ma,cd);
			sw=max(sw,cw-ms);
			ss=max(ss,mw-cw);
			sd=max(sd,cd-ma);
			sa=max(sa,md-cd);
		}
		long long x[2],y[2];
		x[0]=max(sw,ss) + 1;
		x[1]=max((long long)(sw || ss)+1,x[0]-(sw!=ss));
		y[0]=max(sd,sa)+1;
		y[1]=max((long long)(sd || sa)+1,y[0]-(sd!=sa));
        cout << x[1] << " " << y[1] << endl;
		cout<<min((x[0])*(y[1]),(x[1])*(y[0]))<<endl;
	}
	return 0;
}