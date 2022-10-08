# 题目：1913.两个数对之间的最大乘积差
# 难度：EASY
# 最后提交：2022-03-25 18:04:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = SortedList()
        b = SortedList()
        for i in nums:
            if len(a) < 2:
                a.add(i)
            else:
                if i > a[0]:
                    a.pop(0)
                    a.add(i)
            if len(b) < 2:
                b.add(i)
            else:
                if i < b[-1]:
                    b.pop()
                    b.add(i)
        return a[0]*a[1]-b[0]*b[1]