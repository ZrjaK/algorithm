# 题目：2068.检查两个字符串是否几乎相等
# 难度：EASY
# 最后提交：2022-12-09 08:50:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        return all(abs(word1.count(chr(i)) - word2.count(chr(i))) <= 3 for i in range(97, 97+26))