# 题目：2304.网格中的最小路径代价
# 难度：MEDIUM
# 最后提交：2022-06-12 10:44:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @cache
        def p(i, j):
            if i == m-1:
                return grid[i][j]
            res = 1e99
            for k in range(n):
                res = min(res, p(i+1, k)+moveCost[grid[i][j]][k]+grid[i][j])
            return res
            
            
        res = 1e99
        for i in range(n):
            res = min(res, p(0, i))
        return res
        