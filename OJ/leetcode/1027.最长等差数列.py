# 题目：1027.最长等差数列
# 难度：MEDIUM
# 最后提交：2022-07-12 02:06:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1] * 1001 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = max(dp[i][d], dp[j][d]+1)
        return max(max(i) for i in dp)