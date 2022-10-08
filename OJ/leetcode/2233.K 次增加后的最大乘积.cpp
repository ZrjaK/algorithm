// 题目：2233.K 次增加后的最大乘积
// 难度：MEDIUM
// 最后提交：2022-04-10 11:21:59 +0800 CST
// 语言：cpp
// 作者：ZrjaK

class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
        priority_queue<int,vector<int>,greater<int> >q;
        for(auto& i : nums) q.push(i);
        while(k!=0){
            int t = q.top();
            q.pop();
            q.push(t+1);
            k--;
        }
        long long s = 1;
        while(!q.empty()) {
            int t = q.top();
            q.pop();
            s *= t;
            s %= (1000000000+7);
        };
        return int(s % (1000000000+7));
    }
};