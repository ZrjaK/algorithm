# 题目：1574.删除最短的子数组使剩余数组有序
# 难度：MEDIUM
# 最后提交：2022-05-08 21:44:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = n-1, 0
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                l = i - 1
                break
        for i in range(n-1, 0, -1):
            if arr[i-1] > arr[i]:
                r = i
                break
        if l >= r:
            return 0
        ans = n-1
        c = r
        for i in range(l+1):
            while r < n and arr[i] > arr[r]:
                r += 1
            ans = min(ans, r-i-1)
        return min(ans, n-max(l, n-c))
