# 题目：205.同构字符串
# 难度：EASY
# 最后提交：2021-10-21 11:22:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))