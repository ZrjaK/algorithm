# 题目：1753.移除石子的最大得分
# 难度：MEDIUM
# 最后提交：2022-12-21 01:27:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        if a + b < c:
            return a + b
        if a + c < b:
            return a + c
        if b + c < a:
            return b + c
        return (a + b + c) // 2