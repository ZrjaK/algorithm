# 题目：1262.可被三整除的最大和
# 难度：MEDIUM
# 最后提交：2022-07-14 16:07:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, -1e99, -1e99] for _ in range(n+1)]
        for i in range(n):
            t = nums[i] % 3
            for j in range(3):
                dp[i][(t+j)%3] = max(dp[i-1][(t+j)%3], dp[i-1][j] + nums[i])
        return dp[n-1][0]