# 题目：697.数组的度
# 难度：EASY
# 最后提交：2021-10-23 15:29:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        a = {}
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]] = [i]
            else:
                a[nums[i]].append(i)
        m = 0
        for i in a:
            m = max(m, len(a[i])) 
        r = len(nums)
        for i in a:
            if len(a[i]) == m:
                r = min(r, a[i][-1] - a[i][0] + 1)
        return r