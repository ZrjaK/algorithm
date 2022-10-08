# 题目：798.得分最高的最小轮调
# 难度：HARD
# 最后提交：2022-09-20 18:37:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * (n+1)
        for i in range(n):
            if nums[i] <= i:
                diff[0] += 1
                diff[i-nums[i]+1] -= 1
                diff[i+1] += 1
            else:
                diff[i+1] += 1
                diff[n-(nums[i]-i)+1] -= 1
        ans = ma = s = 0
        for i in range(n):
            s += diff[i]
            if s > ma:
                ans = i
                ma = s
        return ans