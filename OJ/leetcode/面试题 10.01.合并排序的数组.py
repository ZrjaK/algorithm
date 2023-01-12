# 题目：面试题 10.01.合并排序的数组
# 难度：EASY
# 最后提交：2022-12-09 08:51:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        A[m:] = B
        A.sort()