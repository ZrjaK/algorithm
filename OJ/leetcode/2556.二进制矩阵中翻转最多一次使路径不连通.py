# 题目：2556.二进制矩阵中翻转最多一次使路径不连通
# 难度：MEDIUM
# 最后提交：2023-02-10 20:57:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPossibleToCutPath(self, g: List[List[int]]) -> bool:
        m, n = len(g), len(g[0])
        def dfs(x: int, y: int) -> bool:  # 返回能否到达终点
            if x == m - 1 and y == n - 1: return True
            g[x][y] = 0  # 直接修改
            return x < m - 1 and g[x + 1][y] and dfs(x + 1, y) or \
                   y < n - 1 and g[x][y + 1] and dfs(x, y + 1)
        return not dfs(0, 0) or not dfs(0, 0)