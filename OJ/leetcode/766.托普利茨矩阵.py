# 题目：766.托普利茨矩阵
# 难度：EASY
# 最后提交：2021-10-24 12:45:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(matrix[i][:-1] == matrix[i+1][1:] for i in range(len(matrix)-1))
        