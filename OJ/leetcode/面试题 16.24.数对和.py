# 题目：面试题 16.24.数对和
# 难度：MEDIUM
# 最后提交：2023-01-03 01:21:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        from sortedcontainers import SortedList
        ans = []
        sl = SortedList(nums)
        for i in nums:
            if not sl.count(i):
                continue
            if sl.count(target-i) > int(i == target-i):
                ans.append([i, target-i])
                sl.remove(i)
                sl.remove(target-i)
        return ans