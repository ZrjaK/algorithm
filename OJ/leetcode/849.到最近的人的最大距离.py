# 题目：849.到最近的人的最大距离
# 难度：MEDIUM
# 最后提交：2022-05-22 01:02:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        h1 = [0] * n
        h2 = [0] * n
        c = -1e9
        for i in range(n):
            if seats[i] == 1:
                h1[i] = 1e99
                c = i
                continue
            h1[i] = i - c
        c = 1e9
        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                h2[i] = 1e99
                c = i
                continue
            h2[i] = c - i
        ans = 1
        for i, j in zip(h1, h2):
            if i == 1e99:
                continue
            ans = max(ans, min(i, j))
        return ans
            