# 题目：945.使数组唯一的最小增量
# 难度：MEDIUM
# 最后提交：2022-08-30 01:41:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        v = set()
        nums = [0] + nums
        ans = 0
        c = []
        for i in range(1, len(nums)):
            if nums[i] not in v:
                v.add(nums[i])
            else:
                c.append(nums[i])
            j = nums[i-1] + 1
            while c and j < nums[i]:
                ans += j - c.pop()
                j += 1
        if c:
            j = nums[-1] + 1
            while c:
                ans += j - c.pop()
                j += 1
        return ans