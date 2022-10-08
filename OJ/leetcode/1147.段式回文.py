# 题目：1147.段式回文
# 难度：HARD
# 最后提交：2022-04-05 04:31:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestDecomposition(self, text: str) -> int:
        if text == "":
            return 0
        for i in range(1,len(text)):
            if text[:i] == text[-i:]:
                return 2 + self.longestDecomposition(text[i:-i])
        return 1