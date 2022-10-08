# 题目：153.寻找旋转排序数组中的最小值
# 难度：MEDIUM
# 最后提交：2022-08-16 19:03:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = l+r>>1
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]