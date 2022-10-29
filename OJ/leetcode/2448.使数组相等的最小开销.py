# 题目：2448.使数组相等的最小开销
# 难度：HARD
# 最后提交：2022-10-23 11:45:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        h = [[i, j] for i, j in zip(nums, cost)]
        h.sort(key=lambda x:x[0])
        t = sum((i-h[0][0]) * j for i, j in h)
        ans = t
        lc = 0
        rc = sum(cost)
        j = 0
        for i in range(min(nums)+1, max(nums)+1):
            while i > h[j][0]:
                lc += h[j][1]
                rc -= h[j][1]
                j += 1
            t += lc - rc
            ans = min(ans, t)
        return ans