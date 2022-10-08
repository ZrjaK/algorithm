# 题目：面试题 01.02.判定是否互为字符重排
# 难度：EASY
# 最后提交：2022-09-27 09:21:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)