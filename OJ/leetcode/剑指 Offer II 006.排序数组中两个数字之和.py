# 题目：剑指 Offer II 006.排序数组中两个数字之和
# 难度：EASY
# 最后提交：2022-10-04 10:23:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            t = bisect_right(numbers, target-numbers[i])
            if t > 0 and numbers[t-1] == target-numbers[i] and t-1 != i:
                return [i, t-1]