# 题目：42.接雨水
# 难度：HARD
# 最后提交：2022-04-15 09:28:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0]*n, [0]*n
        for i in range(1,n):
            left[i] = max(left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        ans = 0
        for i in range(n):
            ans += max(0, min(left[i], right[i]) - height[i])
        return ans