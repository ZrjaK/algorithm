# 题目：84.柱状图中最大的矩形
# 难度：HARD
# 最后提交：2022-10-06 19:33:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [-1]
        n = len(heights)
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                ans = max(ans, heights[stack.pop()] * (i-stack[-1]-1))
            stack.append(i)
        while stack[-1] != -1:
            t = stack.pop()
            ans = max(ans, heights[t] * (n-stack[-1]-1))
        return ans