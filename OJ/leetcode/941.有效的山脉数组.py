# 题目：941.有效的山脉数组
# 难度：EASY
# 最后提交：2021-11-03 11:57:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l, r = 0, len(arr) - 1
        while l < r and arr[l] < arr[l+1]: l += 1
        while r > l and arr[r] < arr[r-1]: r -= 1
        return l == r and l != 0 and r != len(arr) - 1