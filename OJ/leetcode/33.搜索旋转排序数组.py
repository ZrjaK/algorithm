# 题目：33.搜索旋转排序数组
# 难度：MEDIUM
# 最后提交：2022-04-17 08:48:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        isinleft = nums[0] < target
        if nums[0] == target:
            return 0
        if nums[-1] > nums[0]:
            ans =  bisect_left(nums, target)
            if ans < len(nums) and nums[ans] == target:
                return ans
            else:
                return -1
        l, r = 0, len(nums)-1
        while l < r:
            mid = l+r>>1
            if nums[mid] > nums[0]:
                l = mid+1
            else:
                r = mid
        maxi = l
        ans = 0
        if isinleft:
            ans = bisect_left(nums[:maxi], target)
        else:
            ans = maxi+bisect_left(nums[maxi:], target)
        print(ans, maxi)
        if maxi == 0 and ans == 0:
            ans = 1
        if ans < len(nums) and nums[ans] == target:
            return ans
        else:
            return -1