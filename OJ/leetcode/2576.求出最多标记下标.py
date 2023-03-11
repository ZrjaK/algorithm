# 题目：2576.求出最多标记下标
# 难度：MEDIUM
# 最后提交：2023-02-26 11:26:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        nums.sort()
        sl = SortedList(nums[len(nums)//2:])
        ans = 0
        for i in nums[:len(nums)//2]:
            t = sl.bisect_left(2 * i)
            if t < len(sl):
                sl.pop(t)
                ans += 1
        return ans * 2