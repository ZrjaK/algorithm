# 题目：953.验证外星语词典
# 难度：EASY
# 最后提交：2021-11-03 12:50:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: [order.index(x) for x in w])