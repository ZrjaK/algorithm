# 题目：304.二维区域和检索 - 矩阵不可变
# 难度：MEDIUM
# 最后提交：2022-05-05 15:25:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i + 1][j + 1] = _sums[i][j + 1] + _sums[i + 1][j] - _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums

        return _sums[row2 + 1][col2 + 1] - _sums[row1][col2 + 1] - _sums[row2 + 1][col1] + _sums[row1][col1]