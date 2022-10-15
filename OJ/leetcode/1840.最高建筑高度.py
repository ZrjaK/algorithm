# 题目：1840.最高建筑高度
# 难度：HARD
# 最后提交：2022-10-11 20:36:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        r = [[1, 0]] + sorted(restrictions)
        if r[-1][0] != n:
            r.append([n, n-1])
        n = len(r)
        for i in range(1, n):
            r[i][1] = min(r[i][1], r[i-1][1] + r[i][0] - r[i-1][0])
        for i in range(n-2, -1, -1):
            r[i][1] = min(r[i][1], r[i+1][1] + r[i+1][0] - r[i][0])
        ans = 0
        for i in range(1, n):
            ans = max(ans, (r[i][0] - r[i-1][0] + r[i-1][1] + r[i][1]) // 2)
        return ans