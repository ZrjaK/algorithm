# 题目：2397.被列覆盖的最多行数
# 难度：MEDIUM
# 最后提交：2022-09-03 22:38:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        for x in range(1<<n):
            if x.bit_count() > cols:
                continue
            t = 0
            for i in range(m):
                if all(mat[i][j] == 0 or 1<<j & x for j in range(n)):
                    t += 1
            ans = max(ans, t)
        return ans