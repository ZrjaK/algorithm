# 题目：1018.可被 5 整除的二进制前缀
# 难度：EASY
# 最后提交：2021-11-05 20:38:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s = 0
        res = []
        for n in nums:
            s = s * 2 + n
            res.append(s % 5 == 0)
        return res