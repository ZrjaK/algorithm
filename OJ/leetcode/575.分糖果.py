# 题目：575.分糖果
# 难度：EASY
# 最后提交：2021-10-22 23:40:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)