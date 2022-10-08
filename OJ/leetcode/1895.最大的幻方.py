# 题目：1895.最大的幻方
# 难度：MEDIUM
# 最后提交：2022-09-12 20:56:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 每一行的前缀和
        rowsum = [[0] * n for _ in range(m)]
        for i in range(m):
            rowsum[i][0] = grid[i][0]
            for j in range(1, n):
                rowsum[i][j] = rowsum[i][j - 1] + grid[i][j]
        
        # 每一列的前缀和
        colsum = [[0] * n for _ in range(m)]
        for j in range(n):
            colsum[0][j] = grid[0][j]
            for i in range(1, m):
                colsum[i][j] = colsum[i - 1][j] + grid[i][j]

        # 从大到小枚举边长 edge
        for edge in range(min(m, n), 1, -1):
            # 枚举正方形的左上角位置 (i,j)
            for i in range(m - edge + 1):
                for j in range(n - edge + 1):
                    # 计算每一行、列、对角线的值应该是多少（以第一行为样本）
                    stdsum = rowsum[i][j + edge - 1] - (0 if j == 0 else rowsum[i][j - 1])
                    check = True
                    # 枚举每一行并用前缀和直接求和
                    # 由于我们已经拿第一行作为样本了，这里可以跳过第一行
                    for ii in range(i + 1, i + edge):
                        if rowsum[ii][j + edge - 1] - (0 if j == 0 else rowsum[ii][j - 1]) != stdsum:
                            check = False
                            break
                    if not check:
                        continue
                    
                    # 枚举每一列并用前缀和直接求和
                    for jj in range(j, j + edge):
                        if colsum[i + edge - 1][jj] - (0 if i == 0 else colsum[i - 1][jj]) != stdsum:
                            check = False
                            break
                    if not check:
                        continue
                    
                    # d1 和 d2 分别表示两条对角线的和
                    # 这里 d 表示 diagonal
                    d1 = d2 = 0
                    # 不使用前缀和，直接遍历求和
                    for k in range(edge):
                        d1 += grid[i + k][j + k]
                        d2 += grid[i + k][j + edge - 1 - k]
                    if d1 == stdsum and d2 == stdsum:
                        return edge

        return 1