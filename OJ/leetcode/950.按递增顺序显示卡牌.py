# 题目：950.按递增顺序显示卡牌
# 难度：MEDIUM
# 最后提交：2022-08-30 02:02:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        res = [deck[0]]
        for i in deck[1:]:
            res = res[1:] + res[:1]
            res.append(i)
        return res[::-1]

        