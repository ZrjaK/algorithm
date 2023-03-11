# 题目：2572.无平方子集计数
# 难度：MEDIUM
# 最后提交：2023-02-21 20:16:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        pr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        n = len(nums)
        ans = 0
        h = []
        ban = []
        for i in nums:
            t = 0
            for k in range(10):
                if i % pr[k] == 0:
                    t |= 1 << k
            h.append(t)
            if i % 4 == 0 or i % 9 == 0 or i % 25 == 0:
                ban.append(1)
            else:
                ban.append(0)
        M = int(1e9 + 7)
        dp = [[0] * (1<<11) for _ in range(n+1)]
        for j in range(1, 1<<11):
            dp[n][j] = 1
        for i in range(n-1, -1, -1):
            for j in range(1<<11):
                dp[i][j] += dp[i+1][j]
                if not ban[i]:
                    if h[i] & j == 0 and nums[i] != 1:
                        dp[i][j] += dp[i + 1][j | h[i]]
                    if nums[i] == 1:
                        dp[i][j] += dp[i + 1][j | 1 << 10]
                dp[i][j] %= M
        return dp[0][0]