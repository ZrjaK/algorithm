# 题目：287.寻找重复数
# 难度：MEDIUM
# 最后提交：2022-05-01 19:48:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 1, n-1
        while l <= r:
            mid = l+r>>1
            c = 0
            for i in nums:
                if i <= mid:
                    c += 1
            if c > mid:
                r = mid-1
            else:
                l = mid+1
        return l