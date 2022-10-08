# 题目：1685.有序数组中差绝对值之和
# 难度：MEDIUM
# 最后提交：2022-04-10 07:09:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lsum, rsum = [0] * n, [0] * n
        for i in range(1, n):
            lsum[i] = lsum[i-1] + nums[i-1]
        for i in range(n-2, -1, -1):
            rsum[i] = rsum[i+1] + nums[i+1]
        res = [0] * n
        for i in range(n):
            res[i] = (nums[i] * i - lsum[i]) + (rsum[i] - nums[i] * (n-1-i))
        return res