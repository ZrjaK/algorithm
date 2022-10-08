# 题目：1582.二进制矩阵中的特殊位置
# 难度：EASY
# 最后提交：2022-09-04 00:38:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rs = [sum(i) for i in mat]
        cs = [sum([mat[i][j] for i in range(m)]) for j in range(n)]
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == rs[i] == cs[j] == 1:
                    res += 1
        return res