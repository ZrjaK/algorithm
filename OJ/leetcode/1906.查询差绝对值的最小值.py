# 题目：1906.查询差绝对值的最小值
# 难度：MEDIUM
# 最后提交：2022-09-21 11:47:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        h = [[0] * 101 for _ in range(n+1)]
        for i in range(n):
            for j in range(101):
                h[i][j] = h[i-1][j] + (j == nums[i])
        ans = []
        for l, r in queries:
            t = []
            c = 1e99
            for j in range(101):
                if h[r][j] - h[l-1][j]:
                    t.append(j)
            if len(t) == 1:
                ans.append(-1)
                continue
            for i in range(1, len(t)):
                c = min(c, t[i]-t[i-1])
            ans.append(c)
        return ans