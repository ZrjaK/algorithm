# 题目：1975.最大方阵和
# 难度：MEDIUM
# 最后提交：2022-09-09 11:13:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        h = []
        for i in matrix:
            for j in i:
                h.append(j)
        h.sort(key=lambda x:abs(x))
        c = 0
        for i in h:
            if i < 0:
                c += 1
        if c % 2:
            return -abs(h[0]) + sum([abs(i) for i in h[1:]])
        else:
            return sum([abs(i) for i in h])