# 题目：剑指 Offer 40.最小的k个数
# 难度：EASY
# 最后提交：2022-10-03 11:22:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]