# 题目：1536.排布二进制网格的最少交换次数
# 难度：MEDIUM
# 最后提交：2022-09-07 10:28:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        h = [-1] * n
        for i in range(n):
            for j in range(n-1, -1, -1):
                if grid[i][j]:
                    h[i] = j
                    break
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if h[j] <= i:
                    ans += j-i
                    for k in range(j, i, -1):
                        h[k], h[k-1] = h[k-1], h[k]
                    break
            else:
                return -1
        return ans