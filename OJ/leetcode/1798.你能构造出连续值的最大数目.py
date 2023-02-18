# 题目：1798.你能构造出连续值的最大数目
# 难度：MEDIUM
# 最后提交：2023-02-04 02:42:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        x = 0
        for coin in coins:
            if coin > x + 1:
                break
            x += coin
        return x + 1