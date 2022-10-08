# 题目：剑指 Offer 58 - II.左旋转字符串
# 难度：EASY
# 最后提交：2022-10-03 20:34:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]