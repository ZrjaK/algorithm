# 题目：867.转置矩阵
# 难度：EASY
# 最后提交：2021-10-25 15:56:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(x) for x in zip(*matrix)]