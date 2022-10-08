# 题目：643.子数组最大平均数 I
# 难度：EASY
# 最后提交：2021-10-23 11:05:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        temp = s
        for i in range(k, len(nums)):
            temp += nums[i] - nums[i-k]
            s = max(s, temp)
        return float(s / k)