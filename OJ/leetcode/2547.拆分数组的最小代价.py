# 题目：2547.拆分数组的最小代价
# 难度：HARD
# 最后提交：2023-01-22 14:18:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def p(i):
            if i == n:
                return 0
            res = 1e99
            d = defaultdict(int)
            q = 0
            for j in range(i, n):
                if d[nums[j]] == 1:
                    q -= 1
                d[nums[j]] += 1
                if d[nums[j]] == 1:
                    q += 1
                res = min(res, k + j - i + 1 - q + p(j+1))
            return res
        return p(0)