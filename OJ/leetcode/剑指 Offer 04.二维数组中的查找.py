# 题目：剑指 Offer 04.二维数组中的查找
# 难度：MEDIUM
# 最后提交：2022-09-30 10:57:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
            else:
                return True
        return False