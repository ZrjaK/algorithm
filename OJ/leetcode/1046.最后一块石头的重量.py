# 题目：1046.最后一块石头的重量
# 难度：EASY
# 最后提交：2021-11-06 13:57:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) != 1:
            max1 = max(stones)
            stones.remove(max1)
            max2 = max(stones)
            stones.remove(max2)
            stones.append(max1-max2)
        return stones[0]