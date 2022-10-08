# 题目：1130.叶值的最小代价生成树
# 难度：MEDIUM
# 最后提交：2022-07-13 03:22:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        @cache
        def p(i, j):
            if i == j:
                return 0
            res = 1e99
            for k in range(i, j):
                res = min(res, p(i, k)+p(k+1, j) + max(arr[i:k+1])*max(arr[k+1:j+1]))
            return res
        return p(0, n-1)