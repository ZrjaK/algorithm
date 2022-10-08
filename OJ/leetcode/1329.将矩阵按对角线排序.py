# 题目：1329.将矩阵按对角线排序
# 难度：MEDIUM
# 最后提交：2022-08-30 15:19:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        i, j = m-1, 0
        while i > 0:
            x, y = i, j
            h = []
            while x < m and y < n:
                h.append(mat[x][y])
                x += 1
                y += 1
            x, y = i, j
            h = sorted(h)[::-1]
            while x < m and y < n:
                mat[x][y] = h.pop()
                x += 1
                y += 1
            i -= 1
        while j < n:
            x, y = i, j
            h = []
            while x < m and y < n:
                h.append(mat[x][y])
                x += 1
                y += 1
            x, y = i, j
            h = sorted(h)[::-1]
            while x < m and y < n:
                mat[x][y] = h.pop()
                x += 1
                y += 1
            j += 1
        return mat