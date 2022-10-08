# 题目：2033.获取单值网格的最小操作数
# 难度：MEDIUM
# 最后提交：2022-09-01 14:42:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        h = []
        for i in range(m):
            for j in range(n):
                if (grid[i][j] - grid[0][0]) % x:
                    return -1
                h.append(grid[i][j])
        h.sort()
        a = h[(m*n)//2]
        ans = 0
        for i in h:
            ans += abs(i-a) // x
        return ans
        