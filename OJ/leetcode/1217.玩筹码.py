# 题目：1217.玩筹码
# 难度：EASY
# 最后提交：2021-11-13 22:03:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(sum(1 for i in position if i%2==1),sum(1 for i in position if i%2==0))