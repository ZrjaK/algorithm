# 题目：1696.跳跃游戏 VI
# 难度：MEDIUM
# 最后提交：2022-05-24 22:37:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-1e99] * n
        dp[0] = nums[0]
        d = deque([0])
        for i in range(1, n):
            dp[i] = dp[d[0]] + nums[i]
            while d and dp[d[-1]] <= dp[i]:
                d.pop()
            d.append(i)
            if d and d[0] <= i-k:
                d.popleft()
        return dp[-1]