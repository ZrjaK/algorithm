# 题目：238.除自身以外数组的乘积
# 难度：MEDIUM
# 最后提交：2022-04-13 09:49:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        h1, h2 = [1] * n, [1] * n
        for i in range(1,n):
            h1[i] = h1[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            h2[i] = h2[i+1] * nums[i+1]
        res = [0] * n
        for i in range(n):
            res[i] = h1[i] * h2[i]
        return res