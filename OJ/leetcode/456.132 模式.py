# 题目：456.132 模式
# 难度：MEDIUM
# 最后提交：2022-04-16 07:51:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        h = [1e99]
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack and h[stack[-1]] < nums[i]:
                return True
            stack.append(i)
            h.append(min(h[-1], nums[i]))
        return False