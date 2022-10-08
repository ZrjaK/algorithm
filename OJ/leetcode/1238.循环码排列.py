# 题目：1238.循环码排列
# 难度：MEDIUM
# 最后提交：2022-08-26 03:18:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = [start]
        for i in range(n):
            res = res + [j^1<<i for j in res][::-1]
        return res