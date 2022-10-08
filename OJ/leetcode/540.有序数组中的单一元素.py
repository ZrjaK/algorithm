# 题目：540.有序数组中的单一元素
# 难度：MEDIUM
# 最后提交：2022-05-01 20:04:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l+r>>1
            mid -= mid & 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]