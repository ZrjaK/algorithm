// 题目：1289.下降路径最小和  II
// 难度：HARD
// 最后提交：2022-10-24 11:56:43 +0800 CST
// 语言：cpp
// 作者：ZrjaK

class Solution {
public:
    int dp[200][200];
    int minFallingPathSum(vector<vector<int>>& grid) {
        memset(dp, 0x3f3f3f3f, sizeof(dp));
        int m = grid.size();
        int n = grid[0].size();
        for(int j = 0; j < n; j++) dp[n-1][j] = grid[n-1][j];
        for(int i = m-2; i >= 0; i--) 
            for(int j = 0;j < n; j++) 
                for(int k = 0; k < n; k++)
                    if (k != j) dp[i][j] = min(dp[i][j], grid[i][j] + dp[i+1][k]);
        int ans = 0x3f3f3f3f;
        for(int j = 0; j < n; j++) ans = min(ans, dp[0][j]);
        return ans;
    }
};