# 题目：剑指 Offer II 075.数组相对排序
# 难度：EASY
# 最后提交：2022-10-08 14:26:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        h = [i for i in arr1 if i not in arr2]
        arr1 = sorted([i for i in arr1 if i in arr2], key=lambda x: arr2.index(x))
        return arr1 + sorted(h)