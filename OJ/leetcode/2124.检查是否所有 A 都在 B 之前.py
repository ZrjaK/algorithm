# 题目：2124.检查是否所有 A 都在 B 之前
# 难度：EASY
# 最后提交：2022-04-08 11:39:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkString(self, s: str) -> bool:
        return list(s) == sorted(list(s))