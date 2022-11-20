# 题目：775.全局倒置与局部倒置
# 难度：MEDIUM
# 最后提交：2022-11-16 09:48:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        from sortedcontainers import SortedList
        n = len(nums)
        s = SortedList()
        ans = 0
        for i in nums[::-1]:
            ans += s.bisect_left(i)
            s.add(i)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                ans -= 1
        return ans == 0