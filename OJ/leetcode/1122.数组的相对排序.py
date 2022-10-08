# 题目：1122.数组的相对排序
# 难度：EASY
# 最后提交：2021-11-06 18:32:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in arr2:
            while i in arr1:
                res.append(i)
                arr1.remove(i)
        arr1.sort()
        res += arr1
        return res