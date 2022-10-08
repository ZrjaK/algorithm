# 题目：34.在排序数组中查找元素的第一个和最后一个位置
# 难度：MEDIUM
# 最后提交：2022-04-17 08:51:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1,-1]
        return [left,right-1]