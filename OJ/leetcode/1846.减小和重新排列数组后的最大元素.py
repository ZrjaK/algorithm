# 题目：1846.减小和重新排列数组后的最大元素
# 难度：MEDIUM
# 最后提交：2022-09-01 02:04:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        arr[0] = 1
        for i in range(1, n):
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]