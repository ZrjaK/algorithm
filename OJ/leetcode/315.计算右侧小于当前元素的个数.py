# 题目：315.计算右侧小于当前元素的个数
# 难度：HARD
# 最后提交：2022-04-11 20:45:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()
        res = []
        for i in nums[::-1]:
            res.append(s.bisect_left(i))
            s.add(i)
        return res[::-1]