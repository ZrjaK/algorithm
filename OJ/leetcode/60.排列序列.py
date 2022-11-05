# 题目：60.排列序列
# 难度：HARD
# 最后提交：2022-11-01 12:32:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(map(str, list(permutations(list(range(1, n+1))))[k-1]))