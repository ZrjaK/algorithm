# 题目：剑指 Offer II 034.外星语言是否排序
# 难度：EASY
# 最后提交：2022-10-06 02:26:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return sorted(words, key=lambda x: [order.index(i) for i in x]) == words