# 题目：334.递增的三元子序列
# 难度：MEDIUM
# 最后提交：2022-09-05 10:38:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        from sortedcontainers import SortedList
        s = SortedList()
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            left[i] = s.bisect_left(nums[i])
            s.add(nums[i])
        s.clear()
        for i in range(n-1, -1, -1):
            right[i] = len(s) - s.bisect_right(nums[i])
            s.add(nums[i])
        for i in range(n):
            if left[i] and right[i]:
                return True
        return False