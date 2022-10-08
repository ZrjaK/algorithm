# 题目：219.存在重复元素 II
# 难度：EASY
# 最后提交：2021-10-21 12:04:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if k == 1 and i < len(nums)-1 and nums[i] == nums[i+1]:
                return True
            if nums[i] in nums[i+1:i+k+1]:
                return True
        return False