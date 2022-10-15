# 题目：1388.3n 块披萨
# 难度：HARD
# 最后提交：2022-10-14 14:16:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def calculate(s):
            n = len(s)
            choose = (n + 1) // 3
            dp = [[0] * (choose + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, choose + 1):
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 2][j - 1] if i - 2 >= 0 else 0) + s[i - 1])
            return dp[n][choose]
        return max(calculate(slices[1:]), calculate(slices[:-1]))