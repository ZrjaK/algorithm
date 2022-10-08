# 题目：81.搜索旋转排序数组 II
# 难度：MEDIUM
# 最后提交：2022-04-17 09:03:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = l+r >> 1
            print(l, r)
            if nums[mid] == nums[r]:
                r -= 1
                continue
            if nums[mid] >= nums[0]:
                l = mid+1
            else:
                r = mid
        maxi = l
        ans = 0
        isinleft = nums[0] <= target
        if isinleft:
            ans = bisect_left(nums[:maxi], target)
        else:
            ans = maxi+bisect_left(nums[maxi:], target)
        if maxi == 0 and ans == 0:
            ans = 1
        if maxi == 0 and len(nums) == 1 and nums[0] == target:
            return True
        # print(maxi,ans)
        if ans < len(nums) and nums[ans] == target:
            return True
        else:
            return False