# 题目：498.对角线遍历
# 难度：MEDIUM
# 最后提交：2022-09-12 13:17:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        h = [[] for _ in range(m+n+1)]
        for i in range(m):
            for j in range(n):
                h[i+j].append(mat[i][j])
        for i in range(m+n):
            if i % 2 == 0:
                h[i] = h[i][::-1]
        res = []
        for i in h:
            for j in i:
                res.append(j)
        return res
