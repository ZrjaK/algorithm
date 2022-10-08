# 题目：剑指 Offer II 069.山峰数组的顶部
# 难度：EASY
# 最后提交：2022-10-08 12:35:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(1, n-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                return i