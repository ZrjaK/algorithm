# 题目：2567.修改两个元素的最小分数
# 难度：MEDIUM
# 最后提交：2023-02-18 22:37:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(abs(nums[-1] - nums[2]), abs(nums[-2] - nums[1]), abs(nums[-3] - nums[0]))