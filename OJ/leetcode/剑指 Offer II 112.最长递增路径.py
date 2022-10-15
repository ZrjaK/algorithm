# 题目：剑指 Offer II 112.最长递增路径
# 难度：HARD
# 最后提交：2022-10-10 17:06:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def p(i, j):
            next1, next2, next3, next4 = 0, 0, 0, 0
            if i > 0 and matrix[i-1][j] > matrix[i][j]:
                next1 = p(i-1, j)
            if i+1 < m and matrix[i+1][j] > matrix[i][j]:
                next2 = p(i+1, j)
            if j > 0 and matrix[i][j-1] > matrix[i][j]:
                next3 = p(i, j-1)
            if j+1 < n and matrix[i][j+1] > matrix[i][j]:
                next4 = p(i, j+1)
            return max([next1, next2, next3, next4]) + 1
 
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, p(i, j))
        return ans