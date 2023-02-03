# 题目：2536.子矩阵元素加 1
# 难度：MEDIUM
# 最后提交：2023-01-15 10:35:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n+10) for _ in range(n+10)]
        for x1, y1, x2, y2 in queries:
            diff[x1][y1] += 1
            diff[x2+1][y1] -= 1
            diff[x1][y2+1] -= 1
            diff[x2+1][y2+1] += 1
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                diff[i][j] += diff[i-1][j] + diff[i][j-1] - diff[i-1][j-1]
        for i in range(n):
            for j in range(n):
                ans[i][j] = diff[i][j]
        return ans