# 题目：376.摆动序列
# 难度：MEDIUM
# 最后提交：2022-07-01 21:17:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up = down + 1
            if nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)