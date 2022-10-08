# 题目：396.旋转函数
# 难度：MEDIUM
# 最后提交：2022-04-22 06:02:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        pre = 0
        for i in range(n):
            pre += i * nums[i]
        ans = pre
        for i in range(1,n):
            cur = pre + s - n * nums[-i]
            pre = cur
            ans = max(ans, cur)
        return ans