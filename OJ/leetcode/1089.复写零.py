# 题目：1089.复写零
# 难度：EASY
# 最后提交：2021-11-06 16:03:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1