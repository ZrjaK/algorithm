# 题目：74.搜索二维矩阵
# 难度：MEDIUM
# 最后提交：2022-04-24 20:58:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = bisect_left([i[-1] for i in matrix], target)
        if 0 <= r < len(matrix):
            t = matrix[r]
            c = bisect_left(t, target)
            return matrix[r][c] == target
        return False