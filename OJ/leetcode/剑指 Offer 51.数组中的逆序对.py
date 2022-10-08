# 题目：剑指 Offer 51.数组中的逆序对
# 难度：HARD
# 最后提交：2022-10-03 18:50:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        from sortedcontainers import SortedList
        s = SortedList()
        for i in nums[::-1]:
            ans += s.bisect_left(i)
            s.add(i)
        return ans