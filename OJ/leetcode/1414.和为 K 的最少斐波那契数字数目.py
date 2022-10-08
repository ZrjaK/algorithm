# 题目：1414.和为 K 的最少斐波那契数字数目
# 难度：MEDIUM
# 最后提交：2022-09-07 08:51:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

h = [1, 1]
while len(h) < 50:
    h.append(h[-1] + h[-2])
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        ans = 0
        while k:
            t = bisect_left(h, k)
            if h[t] == k:
                return ans + 1
            k -= h[t-1]
            ans += 1
        return ans