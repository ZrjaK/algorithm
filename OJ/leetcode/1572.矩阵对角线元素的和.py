# 题目：1572.矩阵对角线元素的和
# 难度：EASY
# 最后提交：2021-10-20 11:04:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        i = 0
        j = len(mat)-1
        while i < len(mat):
            if i != j:
                sum += mat[i][i] + mat[i][j]
            else:
                sum += mat[i][i]
            i += 1
            j -= 1
        return sum