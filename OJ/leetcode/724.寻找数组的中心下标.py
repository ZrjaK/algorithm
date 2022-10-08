# 题目：724.寻找数组的中心下标
# 难度：EASY
# 最后提交：2021-10-23 21:51:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        for i in range(len(nums)):
            if sum(nums[:i]) * 2 + nums[i] == s:
                return i
        return -1