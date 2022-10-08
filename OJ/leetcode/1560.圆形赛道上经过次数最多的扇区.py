# 题目：1560.圆形赛道上经过次数最多的扇区
# 难度：EASY
# 最后提交：2022-05-07 23:56:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mostVisited(self, n: int, A: List[int]) -> List[int]:
        return list(range(A[0], A[-1] + 1)) or list(range(1, A[-1] + 1)) + list(range(A[0], n + 1))