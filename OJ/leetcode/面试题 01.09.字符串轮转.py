# 题目：面试题 01.09.字符串轮转
# 难度：EASY
# 最后提交：2022-09-29 10:29:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in s1+s1