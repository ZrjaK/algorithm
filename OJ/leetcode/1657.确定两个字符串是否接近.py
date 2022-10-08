# 题目：1657.确定两个字符串是否接近
# 难度：MEDIUM
# 最后提交：2022-08-31 19:03:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(Counter(word1).keys()) == sorted(Counter(word2).keys()) and sorted(Counter(word1).values()) == sorted(Counter(word2).values())