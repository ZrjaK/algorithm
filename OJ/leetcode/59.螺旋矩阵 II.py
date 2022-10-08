# 题目：59.螺旋矩阵 II
# 难度：MEDIUM
# 最后提交：2022-09-11 19:07:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        rows, columns = n, n
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        t = 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                res[top][column] = t
                t += 1
            for row in range(top + 1, bottom + 1):
                res[row][right] = t
                t += 1
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    res[bottom][column] = t
                    t += 1
                for row in range(bottom, top, -1):
                    res[row][left] = t
                    t += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res