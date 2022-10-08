# 题目：704.二分查找
# 难度：EASY
# 最后提交：2021-10-23 21:03:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1