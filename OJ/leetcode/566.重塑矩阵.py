# 题目：566.重塑矩阵
# 难度：EASY
# 最后提交：2021-10-22 23:28:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not len(mat) * len(mat[0]) == r * c:
            return mat
        new_nums = []
        for i in mat:
            new_nums += i
        res = []
        for i in range(0, len(new_nums), c):
            res.append(new_nums[i:i+c])
        return res