# 题目：962.最大宽度坡
# 难度：MEDIUM
# 最后提交：2022-09-02 21:46:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        ans = 0
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        for i in range(n-1, ans-1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                ans = max(ans, i-stack.pop())
        return ans