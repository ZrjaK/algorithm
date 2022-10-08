# 题目：1124.表现良好的最长时间段
# 难度：MEDIUM
# 最后提交：2022-09-04 17:58:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        # 大于8小时计1分 小于等于8小时计-1分
        score = [0] * n
        for i in range(n):
            if hours[i] > 8:
                score[i] = 1
            else:
                score[i] = -1
        presum = [0] + list(accumulate(score))
        ans = 0
        stack = []
        for i in range(n + 1):
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i)
        for i in range(n, ans, -1):
            while stack and presum[stack[-1]] < presum[i]:
                ans = max(ans, i - stack.pop())
        return ans