# 题目：2210.统计数组中峰和谷的数量
# 难度：EASY
# 最后提交：2022-04-18 14:39:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        a = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                a.append(nums[i])
        ans = 0
        for i in range(1,len(a)-1):
            if a[i] > a[i-1] and a[i] > a[i+1]:
                ans += 1
            if a[i] < a[i-1] and a[i] < a[i+1]:
                ans += 1
        return ans