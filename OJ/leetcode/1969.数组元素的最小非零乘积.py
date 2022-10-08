# 题目：1969.数组元素的最小非零乘积
# 难度：MEDIUM
# 最后提交：2022-09-09 10:16:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        t = 2 ** p
        return pow(t - 2, (t-2)//2, int(1e9+7)) * (t - 1) % int(1e9+7)