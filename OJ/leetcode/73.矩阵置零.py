# 题目：73.矩阵置零
# 难度：MEDIUM
# 最后提交：2022-09-11 19:09:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = set()
        c = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    r.add(i)
                    c.add(j)
        for i in r:
            for j in range(n):
                matrix[i][j] = 0
        for j in c:
            for i in range(m):
                matrix[i][j] = 0
        