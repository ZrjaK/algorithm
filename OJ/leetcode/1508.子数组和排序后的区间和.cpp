// 题目：1508.子数组和排序后的区间和
// 难度：MEDIUM
// 最后提交：2022-05-07 09:27:39 +0800 CST
// 语言：cpp
// 作者：ZrjaK

class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (int i = 0; i < n; i++) pq.emplace(nums[i], i);
        long long ans = 0;
        for (int i = 1; i <= right; i++) {
            auto c = pq.top();
            pq.pop();
            if (i >= left)
                ans = (ans + c.first) % int(1e9+7);
            if (c.second < n-1)
                pq.emplace(c.first + nums[c.second+1], c.second+1);
        }
        return ans;
    }
};