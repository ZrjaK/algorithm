# 题目：1649.通过指令创建有序数组
# 难度：HARD
# 最后提交：2022-08-24 01:46:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        from sortedcontainers import SortedList
        s = SortedList()
        ans = 0
        for i in instructions:
            if s:
                ans += min(s.bisect_left(i), len(s)-s.bisect_right(i))
            s.add(i)
        return ans % int(1e9+7)