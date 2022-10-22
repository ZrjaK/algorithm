# 题目：1822.数组元素积的符号
# 难度：EASY
# 最后提交：2022-10-20 16:11:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        t = reduce(mul, nums)
        if t > 0:
            return 1
        elif t < 0:
            return -1
        else:
            return 0