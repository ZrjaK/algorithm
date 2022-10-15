# 题目：剑指 Offer II 100.三角形中最小路径之和
# 难度：MEDIUM
# 最后提交：2022-10-10 10:01:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def p(i, j):
            if i == n:
                return 0
            return triangle[i][j] + min(p(i+1, j), p(i+1, j+1))
        return p(0, 0)