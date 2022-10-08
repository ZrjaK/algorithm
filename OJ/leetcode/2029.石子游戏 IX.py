# 题目：2029.石子游戏 IX
# 难度：MEDIUM
# 最后提交：2022-09-09 11:25:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        d = [0] * 3
        for i in stones:
            d[i%3] += 1
        if d[0] % 2 == 0:
            return d[1] > 0 and d[2] > 0
        return d[2] > d[1] + 2 or d[1] > d[2] + 2