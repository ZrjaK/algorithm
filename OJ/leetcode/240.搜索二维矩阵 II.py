# 题目：240.搜索二维矩阵 II
# 难度：MEDIUM
# 最后提交：2022-04-25 06:36:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = 0, -1
        while x < len(matrix) and y >= -len(matrix[0]):
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
        return False