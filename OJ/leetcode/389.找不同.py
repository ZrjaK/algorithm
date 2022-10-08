# 题目：389.找不同
# 难度：EASY
# 最后提交：2021-10-21 19:47:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for c in t:
            if t.count(c)!=s.count(c):
                return c
        return ""