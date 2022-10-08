# 题目：1037.有效的回旋镖
# 难度：EASY
# 最后提交：2021-11-05 22:09:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        A,B,C=points
        return (A[0]-B[0])*(B[1]-C[1])-(A[1]-B[1])*(B[0]-C[0])!=0