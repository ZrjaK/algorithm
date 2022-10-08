# 题目：1785.构成特定和需要添加的最少元素
# 难度：MEDIUM
# 最后提交：2022-09-08 10:09:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        t = sum(nums) - goal
        res = abs(t) // limit
        return res + 1 if abs(t) % limit else res