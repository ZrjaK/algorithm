# 题目：611.有效三角形的个数
# 难度：MEDIUM
# 最后提交：2022-04-14 19:13:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n-1, -1, -1):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    ans += r-l
                    r -= 1
                else:
                    l += 1
        return ans