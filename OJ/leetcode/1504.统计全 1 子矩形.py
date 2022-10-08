# 题目：1504.统计全 1 子矩形
# 难度：MEDIUM
# 最后提交：2022-07-16 19:17:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        
        row = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if j == 0:
                    row[i][j] = mat[i][j]
                else:
                    row[i][j] = 0 if mat[i][j] == 0 else row[i][j - 1] + 1
        
        ans = 0
        for i in range(n):
            for j in range(m):
                col = row[i][j]
                for k in range(i, -1, -1):
                    col = min(col, row[k][j])
                    if col == 0:
                        break
                    ans += col
        
        return ans