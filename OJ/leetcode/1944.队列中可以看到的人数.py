# 题目：1944.队列中可以看到的人数
# 难度：HARD
# 最后提交：2022-09-19 14:15:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                ans[i] += 1
            if stack:
                ans[i] += 1
            stack.append(heights[i])
        return ans