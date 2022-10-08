# 题目：1664.生成平衡数组的方案数
# 难度：MEDIUM
# 最后提交：2022-07-19 19:16:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        sumOdd = sumEven = 0
        for i in range(n):
            if i % 2:
                sumOdd += nums[i]
            else:
                sumEven += nums[i]
        ans = 0
        for i in range(n-1, -1, -1):
            if i % 2:
                sumOdd -= nums[i]
                if sumOdd == sumEven:
                    ans += 1
                sumEven += nums[i]
            else:
                sumEven -= nums[i]
                if sumOdd == sumEven:
                    ans += 1
                sumOdd += nums[i]
        return ans
        