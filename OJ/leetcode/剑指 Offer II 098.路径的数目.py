# 题目：剑指 Offer II 098.路径的数目
# 难度：MEDIUM
# 最后提交：2022-10-10 09:18:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2, m-1)