# 题目：914.卡牌分组
# 难度：EASY
# 最后提交：2021-11-02 18:44:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck = Counter(deck)
        return any([all([c % i == 0 for c in deck.values()]) for i in range(2, 10001)])