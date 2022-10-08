# 题目：1460.通过翻转子数组使两个数组相等
# 难度：EASY
# 最后提交：2022-08-24 02:52:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)