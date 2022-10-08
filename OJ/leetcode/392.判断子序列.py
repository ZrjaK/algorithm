# 题目：392.判断子序列
# 难度：EASY
# 最后提交：2021-10-21 19:56:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        loc = -1
        for a in s:
            loc = t.find(a, loc + 1)
            if loc == -1:
                return False
        return True
