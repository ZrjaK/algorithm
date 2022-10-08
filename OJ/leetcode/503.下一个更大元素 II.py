# 题目：503.下一个更大元素 II
# 难度：MEDIUM
# 最后提交：2022-09-02 13:28:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans