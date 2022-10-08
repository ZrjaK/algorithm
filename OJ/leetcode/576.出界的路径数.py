# 题目：576.出界的路径数
# 难度：MEDIUM
# 最后提交：2022-07-06 00:45:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def p(i, j, rest):
            if not (0 <= i < m and 0 <= j < n):
                return 1
            if not rest:
                return 0
            res = p(i-1, j, rest-1) + p(i+1, j, rest-1) + p(i, j-1, rest-1) + p(i, j+1, rest-1)
            return res
        return p(startRow, startColumn, maxMove) % int(1e9+7)