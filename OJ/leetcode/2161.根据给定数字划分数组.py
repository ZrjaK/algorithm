# 题目：2161.根据给定数字划分数组
# 难度：MEDIUM
# 最后提交：2022-06-21 13:06:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a = [i for i in nums if i < pivot]
        b = [i for i in nums if i == pivot]
        c = [i for i in nums if i > pivot]
        res = a + b + c
        return res