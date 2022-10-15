# 题目：920.播放列表的数量
# 难度：HARD
# 最后提交：2022-10-14 13:25:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [[0] * (n+1) for _ in range(goal+1)]
        dp[0][0] = 1
        for i in range(1, goal+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j-1] * (n-j+1)
                if j > k:
                    dp[i][j] += dp[i-1][j] * (j-k)
        return dp[-1][-1] % int(1e9+7)