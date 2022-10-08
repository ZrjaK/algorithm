# 题目：1619.删除某些元素后的数组均值
# 难度：EASY
# 最后提交：2022-09-14 00:01:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        arr = arr[len(arr)//20:-len(arr)//20]
        return sum(arr) / len(arr)