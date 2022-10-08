# 题目：1567.乘积为正数的最长子数组长度
# 难度：MEDIUM
# 最后提交：2022-05-08 17:31:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        max1 = [0] * n
        max1[0] = 1 if nums[0] > 0 else 0
        max2 = [0] * n
        max2[0] = 1 if nums[0] < 0 else 0
        ans = max1[0]
        for i in range(1, n):
            if nums[i] > 0:
                max1[i] = max1[i-1] + 1
                max2[i] = max2[i-1] + 1 if max2[i-1] > 0 else 0
            elif nums[i] < 0:
                max1[i] = max2[i-1] + 1 if max2[i-1] > 0 else 0
                max2[i] = max1[i-1] + 1
            if nums[i] == 0:
                max1[i] = 0
                max2[i] = 0
            ans = max(ans, max1[i])
            # print(max1, max2)
        return ans
