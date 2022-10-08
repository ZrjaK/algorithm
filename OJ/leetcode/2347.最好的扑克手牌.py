# 题目：2347.最好的扑克手牌
# 难度：EASY
# 最后提交：2022-07-23 22:57:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        for i in range(1, 14):
            if ranks.count(i) >= 3:
                return "Three of a Kind"
        for i in range(1, 14):
            if ranks.count(i) == 2:
                return "Pair"
        return "High Card"
    