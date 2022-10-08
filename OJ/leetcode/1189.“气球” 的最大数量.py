# 题目：1189.“气球” 的最大数量
# 难度：EASY
# 最后提交：2021-11-13 21:32:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = collections.Counter(text)
        return min(d['b'], d['a'], d['l'] // 2, d['o'] // 2, d['n'])