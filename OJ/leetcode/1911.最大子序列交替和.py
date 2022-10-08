# 题目：1911.最大子序列交替和
# 难度：MEDIUM
# 最后提交：2022-03-25 17:58:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [0] + nums + [0]
        up = True
        ans = 0
        for i in range(1, len(nums)-1):
            if up:
                if nums[i] > nums[i+1]:
                    up = False
                    ans += nums[i]
            else:
                if nums[i] < nums[i+1]:
                    up = True
                    ans -= nums[i]
        return ans