# 题目：2022.将一维数组转变成二维数组
# 难度：EASY
# 最后提交：2022-04-06 11:13:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        res = []
        l = r = 0
        while r < len(original):
            r += 1
            if r % n == 0:
                res.append(original[l:r])
                l = r
        return res