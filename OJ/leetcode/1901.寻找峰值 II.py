# 题目：1901.寻找峰值 II
# 难度：MEDIUM
# 最后提交：2022-05-16 16:03:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        i = j = 0
        while 1:
            up = mat[i-1][j] if i > 0 else -1
            down = mat[i+1][j] if i+1 < len(mat) else -1
            left = mat[i][j-1] if j > 0 else -1
            right = mat[i][j+1] if j+1 < len(mat[0]) else -1
            if mat[i][j] < up:
                i -= 1
                continue
            if mat[i][j] < down:
                i += 1
                continue
            if mat[i][j] < left:
                j -= 1
                continue
            if mat[i][j] < right:
                j += 1
                continue
            return [i, j]