# 题目：48.旋转图像
# 难度：MEDIUM
# 最后提交：2022-09-10 09:52:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]