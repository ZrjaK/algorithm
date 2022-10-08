# 题目：162.寻找峰值
# 难度：MEDIUM
# 最后提交：2022-04-23 21:50:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = l+r>>1
            ln = nums[mid-1] if mid-1>=0 else -1e99
            rn = nums[mid+1] if mid+1< n else -1e99
            if nums[mid] > ln and nums[mid] > rn:
                return mid
            if nums[mid] < rn:
                l = mid + 1
            else:
                r = mid - 1
        return 0 if nums[0] > nums[-1] else n-1