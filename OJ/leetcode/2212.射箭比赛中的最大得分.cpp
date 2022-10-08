// 题目：2212.射箭比赛中的最大得分
// 难度：MEDIUM
// 最后提交：2022-04-19 09:01:42 +0800 CST
// 语言：cpp
// 作者：ZrjaK

class Solution {
public:
    int dp[12][100100];
    vector<int> maximumBobPoints(int numArrows, vector<int>& aliceArrows) {
        for(int i = 1;i < 12; i++) {
            for(int j = 0;j < numArrows+1;j++) {
                dp[i][j] = dp[i-1][j];
                if(j-aliceArrows[i]-1 >= 0)
                    dp[i][j] = max(dp[i][j], dp[i-1][j-aliceArrows[i]-1]+i);
            }
        }
        vector<int> res;
        int i = 11;
        int j = numArrows;
        while (i != 0) {
            res.push_back(j);
            int p1 = dp[i-1][j];
            int p2 = -1000000;
            if (j-aliceArrows[i]-1 >= 0)
                p2 = dp[i-1][j-aliceArrows[i]-1]+i;
            if (p1 < p2)
                j = j-aliceArrows[i]-1;
            i--;
        }
        res.push_back(0);
        vector<int> ans;
        for (int i = 0; i < res.size()-1;i++)
            ans.push_back(res[i]-res[i+1]);
        ans.push_back(0);
        reverse(ans.begin(), ans.end());
        return ans;
    }
};