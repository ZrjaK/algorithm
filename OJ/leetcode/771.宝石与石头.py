# 题目：771.宝石与石头
# 难度：EASY
# 最后提交：2021-10-24 12:55:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return [i in jewels for i in stones].count(True)