# 题目：739.每日温度
# 难度：MEDIUM
# 最后提交：2022-09-02 14:00:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans