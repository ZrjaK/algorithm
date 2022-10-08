# 题目：2267.检查是否有合法括号字符串路径
# 难度：HARD
# 最后提交：2022-05-08 11:18:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        if grid[0][0] == ")" or (n+m-1) % 2 == 1 or grid[-1][-1] == "(":
            return False
        @lru_cache(None)
        def p(i, j, l, r):
            # print(i, j, l, r)
            if r > l:
                return False
            if i == n-1 and j == m-1 and l == r+1:
                return True
            if grid[i][j] == "(":
                l += 1
            else:
                r += 1
            p1 = False
            p2 = False
            if i < n-1:
                p1 = p(i+1, j, l, r)
            if j < m-1:
                p2 = p(i, j+1, l, r)
            return p1 or p2
        i = j = 0
        p1 = False
        p2 = False
        if i < n-1:
            p1 = p(i+1, j, 1, 0)
        if j < m-1:
            p2 = p(i, j+1, 1, 0)
        return p1 or p2