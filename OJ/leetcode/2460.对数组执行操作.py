# 题目：2460.对数组执行操作
# 难度：EASY
# 最后提交：2022-11-06 10:31:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        ans = []
        h = []
        for i in nums:
            if i:
                ans.append(i)
            else:
                h.append(i)
        return ans + h