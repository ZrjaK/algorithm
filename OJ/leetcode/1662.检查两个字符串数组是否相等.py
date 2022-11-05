# 题目：1662.检查两个字符串数组是否相等
# 难度：EASY
# 最后提交：2022-11-01 00:16:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)