# 题目：面试题 01.08.零矩阵
# 难度：MEDIUM
# 最后提交：2022-09-30 08:03:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    lst.append([i, j])
        for i, j in lst:
            for x in range(m):
                matrix[x][j] = 0
            for y in range(n):
                matrix[i][y] = 0