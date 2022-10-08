# 题目：剑指 Offer II 013.二维子矩阵的和
# 难度：MEDIUM
# 最后提交：2022-10-04 17:06:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        h = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                h[i][j] = h[i-1][j] + h[i][j-1] - h[i-1][j-1] + matrix[i][j]
        self.h = h


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        h = self.h
        return h[row2][col2] - h[row1-1][col2] - h[row2][col1-1] + h[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)