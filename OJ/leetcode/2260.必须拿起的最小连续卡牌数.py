# 题目：2260.必须拿起的最小连续卡牌数
# 难度：MEDIUM
# 最后提交：2022-05-01 10:36:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = {}
        for i in range(len(cards)):
            if cards[i] in d:
                d[cards[i]].append(i)
            else:
                d[cards[i]] = [i]
        ans = 1e99
        for t in d.values():
            a = 1e99
            for i in range(1,len(t)):
                a = min(a, t[i]-t[i-1]+1)
            ans = min(ans, a)
        if ans == 1e99:
            return -1
        return ans