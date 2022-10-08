# 题目：1425.带限制的子序列和
# 难度：HARD
# 最后提交：2022-09-15 22:26:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        q = deque([0])
        for i in range(n):
            dp[i] = max(nums[i], nums[i] + dp[q[0]])
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] == i-k:
                q.popleft()
        return max(dp)