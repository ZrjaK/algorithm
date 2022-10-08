# 题目：1646.获取生成数组中的最大值
# 难度：EASY
# 最后提交：2022-07-11 20:16:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + i % 2 * nums[i // 2 + 1]
        return max(nums)