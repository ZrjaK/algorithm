# 题目：1424.对角线遍历 II
# 难度：MEDIUM
# 最后提交：2022-08-30 18:18:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), max(len(i) for i in mat)
        h = []
        for i in range(m):
            for j in range(len(mat[i])):
                h.append((mat[i][j], i, j))
        h.sort(key=lambda x:(x[1]+x[2], -x[1]))
        return [i[0] for i in h]