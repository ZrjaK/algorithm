# 题目：2411.按位或最大的最小子数组长度
# 难度：MEDIUM
# 最后提交：2022-09-17 23:02:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = 0
        for i in nums:
            target |= i
        h = [[0] * (n+1) for _ in range(33)]
        for i in range(32):
            for j in range(n):
                h[i][j] = h[i][j-1] + (nums[j]>>i & 1)
        res = [0] * n
        for i in range(n):
            t = i
            for j in range(32):
                if target >>j & 1 and h[j][n-1] != h[j][i-1]:
                    t = max(t, bisect_left(h[j], h[j][i-1]+1))
                    t = min(t, n-1)
            res[i] = t-i+1
        return res
                
        